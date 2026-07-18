#!/usr/bin/env python3
"""Kontroller kundevendt hoteltekst for de vigtigste Thailand Tours-regler."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


GENERIC_PHRASES = (
    "hotellet tilbyder",
    "faciliteter for enhver smag",
    "bredt udvalg",
    "bred vifte",
    "noget for enhver smag",
    "perfekt til alle",
    "paradis på jord",
    "du vil elske",
    "uforglemmelig ferie venter",
    "med sin beliggenhed",
    "uanset om du ønsker",
    "der er rig mulighed for",
    "her venter",
)

SALES_AWAY_PHRASES = (
    "anbefaler vi et andet hotel",
    "anbefale et hotel længere",
    "vælg et andet hotel",
    "peger vi hellere mod",
    "passer et andet hotel bedre",
)


def visible_text(source: str) -> str:
    without_comments = re.sub(r"<!--.*?-->", " ", source, flags=re.DOTALL)
    without_tags = re.sub(r"<[^>]+>", " ", without_comments)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def check(text: str, hotel_name: str | None) -> list[str]:
    issues: list[str] = []
    lowered = text.casefold()

    if re.search(r"\b(?:I|jer|jeres)\b", text):
        issues.append("Brug du-form. Teksten indeholder I, jer eller jeres.")
    if "—" in text or "–" in text:
        issues.append("Teksten indeholder em dash eller en dash.")

    for phrase in GENERIC_PHRASES:
        if phrase in lowered:
            issues.append(f"Generisk eller forbudt formulering: {phrase!r}.")

    ending = lowered[-900:]
    for phrase in SALES_AWAY_PHRASES:
        if phrase in ending:
            issues.append(f"Afslutningen sælger kunden væk: {phrase!r}.")

    first_sentence = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)[0]
    if hotel_name:
        machine_opening = rf"^{re.escape(hotel_name)}\s+ligger\b"
        if re.search(machine_opening, first_sentence, flags=re.IGNORECASE):
            issues.append("Første sætning bruger den maskinelle formel '{hotelnavn} ligger...'.")
    elif re.match(r"^[^.?!]{1,80}\bligger\s+i\b", first_sentence, flags=re.IGNORECASE):
        issues.append("Første sætning ligner den maskinelle formel '{hotelnavn} ligger i...'.")

    if first_sentence.count(",") >= 3:
        issues.append("Første sætning er for pakket. Vælg én konkret indgang.")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="Fil med hoteltekst. Udelad for stdin.")
    parser.add_argument("--hotel-name", help="Hotelnavn til kontrol af åbningsformlen.")
    args = parser.parse_args()

    source = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
    text = visible_text(source)
    issues = check(text, args.hotel_name)

    if issues:
        print("Hotelteksten skal rettes:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Hotelteksten består den automatiske ToV-kontrol.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

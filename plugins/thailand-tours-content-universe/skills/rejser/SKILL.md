---
name: rejser
description: Bruges når Thailand Tours skal skrive, omskrive eller kvalitetstjekke rejseoutput i WordPress/Gutenberg-format, med overblik, inkluderet-boks, kort, rejseprogram, hoteller, pris, lignende rejser og trustbar.
---

# Rejser

Brug denne skill, når opgaven handler om rejser, rundrejser, kombinationsrejser, pakkerejser eller rejseprogrammer for Thailand Tours.

## Hvornår skillen bruges

- Nye rejse- eller rundrejsetekster i WordPress/Gutenberg-format.
- Omskrivning af eksisterende rejsesider.
- Rejseprogrammer med dagsblokke, destinationer, hoteller, transfer og pris.
- Kvalitetstjek af rejseoutput før publicering.

## Referencefiler

Læs kun det nødvendige:

- `references/rejse-output-format.md` for den faste WordPress/Gutenberg-struktur.
- `../tekstomskrivning/references/tone-of-voice.md` for Thailand Tours-stemmen.
- `../tekstomskrivning/references/rewrite-rules.md` for bevaringsregler.
- `../tekstomskrivning/references/banned-patterns.md` for fraser, tegn og tiltale der skal undgås.
- `../tekstomskrivning/references/quality-checklist.md` før aflevering ved større eller publiceringsklar tekst.

## Arbejdsgang

1. Afgør om kilden er rå rejseinfo, eksisterende WordPress-output eller en blanding.
2. Bevar WordPress-kommentarer, group ids, class names, block ids, custom blocks, shortcodes, billeddata, hotel-id'er, prisblokke, sliders og placeholders.
3. Bevar tekniske felter i `pan/trip-day-block`, især `blockId`, `durationDays`, `headline`, `recommendations`, `mediaID`, `mediaPreviewURL` og `hotelID`.
4. Udfyld eller omskriv kun kundevendt tekst: overblik, anbefaling, inkluderet-liste, korttekst, dagsprogram, hoteltekst, prisnær tekst og lignende rejser.
5. Brug `I`, `jer` og `jeres`. Omskriv `du`, `dig`, `din`, `dit` og `dine` i kundevendt prosa.
6. Gør rejsen konkret: rækkefølge, antal nætter, transfer, tempo, oplevelser, strand/by/natur, hvem rejsen passer til og praktiske forbehold.
7. Ved fly, indrejse, visum, sundhed, sikkerhed og aktuelle regler skal officielle kilder tjekkes, før teksten afleveres som fakta.
8. Kør slutkontrol for ændrede fakta, forbudte fraser, `du`-form, tankestreger og ukontrollerede tidsfølsomme oplysninger.

## Done-kriterier

Rejseoutput er færdigt, når:

- Gutenberg-strukturen er intakt.
- Alle centrale blokke er bevaret: overblik, inkluderet-boks, kort, rejseprogram, kontaktblok, hoteller, pris, lignende rejser og trustbar.
- Links, block ids, image ids, hotel ids, slider ids, prisrækker og custom blocks er bevaret.
- Rejseprogrammet har tydelig rækkefølge, tempo og praktisk logik.
- Kunden forstår hvem rejsen passer til, og hvad de vigtigste valg/fravalg er.
- Der er ingen `du/dig/din/dit/dine` i kundevendt prosa.
- Der er ingen em dash eller en dash.
- Tidsfølsomme fakta er verificeret eller markeret til verificering.

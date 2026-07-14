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
5. Skriv altid kundevendt rejsetekst i `du`-form med `du`, `dig`, `din`, `dit` og `dine`. Omskriv `I`, `jer` og `jeres` i al kundevendt prosa.
6. Gør rejsen konkret: rækkefølge, antal nætter, transfer, tempo, oplevelser, strand/by/natur, hvem rejsen passer til og praktiske forbehold.
7. Ved fly, indrejse, visum, sundhed, sikkerhed og aktuelle regler skal officielle kilder tjekkes, før teksten afleveres som fakta.
8. Kør slutkontrol for ændrede fakta, forbudte fraser, `I/jer/jeres`-form, tankestreger og ukontrollerede tidsfølsomme oplysninger.

## Tiltale i rejser

Rejser skal altid skrives direkte til kunden i `du`-form. Brug derfor entalsformen konsekvent, også når kilden er skrevet i flertal.

Omskriv især:

- `I oplever` til `du oplever`
- `I får` til `du får`
- `jeres rejse` til `din rejse`
- `jeres hotel` til `dit hotel`
- `jeres dage` til `dine dage`
- `I kan vælge` til `du kan vælge`

Gode rejseformuleringer:

- `Du begynder rejsen i Bangkok, hvor tempoet er højt, før dagene bliver roligere mod stranden.`
- `Rejsen passer især til dig, der vil have en tydelig rute uden at skifte hotel for ofte.`
- `Hvis du ønsker mere strandtid og færre skift, bør programmet kortes ned eller justeres.`

Undgå i kundevendt output:

- `I begynder rejsen i Bangkok.`
- `Jeres rejse slutter ved stranden.`
- `Her kan I vælge mellem flere hoteller.`

Hvis der findes `I`, `jer` eller `jeres` som direkte kundetiltale i færdigt rejseoutput, er outputtet ikke klar til aflevering.

## Done-kriterier

Rejseoutput er færdigt, når:

- Gutenberg-strukturen er intakt.
- Alle centrale blokke er bevaret: overblik, inkluderet-boks, kort, rejseprogram, kontaktblok, hoteller, pris, lignende rejser og trustbar.
- Links, block ids, image ids, hotel ids, slider ids, prisrækker og custom blocks er bevaret.
- Rejseprogrammet har tydelig rækkefølge, tempo og praktisk logik.
- Kunden forstår hvem rejsen passer til, og hvad de vigtigste valg/fravalg er.
- Kundevendt prosa bruger konsekvent `du`, `dig`, `din`, `dit` og `dine`.
- Der er ingen `I/jer/jeres` som direkte kundetiltale i kundevendt prosa, heller ikke i overblik, dagsprogram, hotelafsnit, prisnær tekst eller lignende rejser.
- Der er ingen em dash eller en dash.
- Tidsfølsomme fakta er verificeret eller markeret til verificering.

---
name: destinationer
description: Bruges når Thailand Tours skal skrive, omskrive eller kvalitetstjekke destinationsoutput i WordPress/Gutenberg-format, med intro, rejsesøgning, underdestinationer, sæsonafsnit, fakta-accordions, kort, hotel-slider, inspiration og trustbar.
---

# Destinationer

Brug denne skill, når opgaven handler om destinationstekster, rejsemålssider, områdeguider eller landingsside-output for Thailand Tours.

## Hvornår skillen bruges

- Nye destinationstekster i WordPress/Gutenberg-format.
- Omskrivning af eksisterende destinationssider.
- Destinationer med rejse-søgning, underdestinationer, sæson, fakta, kort, hoteller og inspiration.
- Kvalitetstjek af destinationsoutput før publicering.

## Referencefiler

Læs kun det nødvendige:

- `references/destination-output-format.md` for den faste WordPress/Gutenberg-struktur.
- `../tekstomskrivning/references/tone-of-voice.md` for Thailand Tours-stemmen.
- `../tekstomskrivning/references/rewrite-rules.md` for bevaringsregler.
- `../tekstomskrivning/references/banned-patterns.md` for fraser, tegn og tiltale der skal undgås.
- `../tekstomskrivning/references/quality-checklist.md` før aflevering ved større eller publiceringsklar tekst.

## Arbejdsgang

1. Afgør om kilden er rå destinationsinfo, eksisterende WordPress-output eller en blanding.
2. Bevar WordPress-kommentarer, group ids, class names, block ids, shortcodes, slider blocks, archive blocks, accordion blocks, map shortcodes, links og placeholders.
3. Bevar placeholders som `[post_title]`, `[year]`, `[site_title]`, `[year offset=...]` og shortcodes som `[ez-toc]`.
4. Udfyld eller omskriv kun kundevendt tekst: intro, rejse-søgning, områdebeskrivelse, sæson, fakta, FAQ/accordions, korttekst, hoteltekst og pakkerejseafsnit.
5. Brug `I`, `jer` og `jeres`. Omskriv `du`, `dig`, `din`, `dit` og `dine` i kundevendt prosa.
6. Gør destinationen konkret: zoner, strande, logistik, sæson, målgrupper, fravalg, transport, mad, oplevelser og praktiske forbehold.
7. Ved visum, indrejse, sundhed, sikkerhed og aktuelle regler skal officielle kilder tjekkes, før teksten afleveres som fakta.
8. Kør slutkontrol for ændrede fakta, forbudte fraser, `du`-form, tankestreger og ukontrollerede tidsfølsomme oplysninger.

## Done-kriterier

Destinationsoutput er færdigt, når:

- Gutenberg-strukturen er intakt.
- Alle centrale blokke er bevaret: intro, rejser, rejsemål, beskrivelse, fakta, kort, hoteller, inspiration og trustbar.
- Links, shortcodes, placeholders og block ids er bevaret.
- Teksten forklarer destinationens forskelle, sæson og praktiske logistik.
- Kunden forstår hvem destinationen passer til, og hvem den ikke passer til.
- Der er ingen `du/dig/din/dit/dine` i kundevendt prosa.
- Der er ingen em dash eller en dash.
- Tidsfølsomme fakta er verificeret eller markeret til verificering.

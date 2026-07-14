---
name: hoteltekster
description: Bruges når Thailand Tours skal skrive, omskrive eller kvalitetstjekke hoteloutput i WordPress/Gutenberg-format, med showcase, billedgalleri, hotel-description-block, kort, attraktioner/afstande og rejse-slider.
---

# Hoteltekster

Brug denne skill, når opgaven handler om hoteltekster for Thailand Tours.

## Hvornår skillen bruges

- Nye hotelbeskrivelser i WordPress/Gutenberg-format.
- Omskrivning af eksisterende hotelblokke.
- Hoteltekster med billedgalleri, features, kort, attraktioner og afstande.
- Kvalitetstjek af hoteloutput før publicering.

## Referencefiler

Læs kun det nødvendige:

- `references/hotel-output-format.md` for den faste WordPress/Gutenberg-struktur.
- `../tekstomskrivning/references/tone-of-voice.md` for Thailand Tours-stemmen.
- `../tekstomskrivning/references/rewrite-rules.md` for bevaringsregler.
- `../tekstomskrivning/references/banned-patterns.md` for fraser, tegn og tiltale der skal undgås.
- `../tekstomskrivning/references/hotel-source-policy.md` for hotelkilder, Expedia-faktatjek, billedvalg og batchregler.
- `../tekstomskrivning/references/quality-checklist.md` før aflevering ved større eller publiceringsklar tekst.

## Arbejdsgang

1. Afgør om kilden er rå hotelinfo, en eksisterende WordPress-blok eller en blanding.
2. Bevar WordPress-kommentarer, block ids, custom blocks, image ids, media URLs, feature JSON, koordinater, slider ids og class names, medmindre opgaven udtrykkeligt beder om ændringer.
3. Udfyld eller omskriv kun kundevendt tekst: hotelbeskrivelse, afsnitsoverskrifter, værelsesbeskrivelser, kort forklaring, attraktioner og afstande.
4. Brug `du`, `dig`, `din`, `dit` og `dine`. Omskriv `I`, `jer` og `jeres` i kundevendt prosa.
5. Gør hotellet konkret: beliggenhed, strand/by/ro, værelsestyper, mad, pool/spa, målgruppe, fravalg og praktiske forbehold.
6. Bevar fakta om hotelnavn, antal værelser, værelsestyper, m2, kapacitet, faciliteter, afstande, koordinater og destination.
7. Brug hotellets egen side og Expedia som primære faktakilder. Brug etablerede rejsebureauer som sekundære kilder, og brug ikke Trustpilot eller Booking.com.
8. Ved batch skal hoteller med Thailand Tours-link springes over, medmindre brugeren eksplicit beder om dem.
9. Kør slutkontrol for ændrede fakta, forbudte fraser, `I/jer/jeres`-form og tankestreger.

## Done-kriterier

Hoteloutput er færdigt, når:

- Gutenberg-strukturen er intakt.
- Hotel-description-block indeholder en rådgivende, konkret hoteltekst.
- Kort og attraktioner/afstande er bevaret eller tydeligt markeret til verificering.
- Værelsesafsnit forklarer forskelle uden at opfinde fakta.
- Teksten hjælper kunden med både at vælge og fravælge hotellet.
- Kilder, source URLs og usikre fakta er dokumenteret i fact_check ved draftarbejde.
- Der er ingen `I/jer/jeres` som direkte kundetiltale i kundevendt prosa.
- Der er ingen em dash eller en dash.

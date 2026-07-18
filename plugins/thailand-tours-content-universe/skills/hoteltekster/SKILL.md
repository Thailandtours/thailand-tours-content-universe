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
- `references/hotel-golden-examples.md` for hoteltypens register, gode åbninger og salgsstærke afslutninger.
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
5. Vælg register efter hoteltypen. Et praktisk byhotel skal lyde konkret og urbant. Et strandresort må gerne være mere sanseligt. Kopiér ikke luksusresortets billedsprog over på et funktionelt byhotel.
6. Gør hotellet konkret: beliggenhed, strand/by/ro, værelsestyper, mad, pool/spa, målgruppe og praktiske forbehold.
7. Start med en observation, kontrast eller brugbar rejseindsigt. Start ikke med `{hotelnavn} ligger i...`, en geografisk deklaration eller en liste over faciliteter.
8. Hold introen fokuseret. Brug højst tre centrale fakta, og gem detaljer om værelser, pool, mad og transport til deres egne afsnit.
9. Beskriv et væsentligt kompromis som forventningsafstemning inde i teksten. Slut positivt med hotellets stærkeste match og send aldrig kunden videre til et andet hotel, medmindre opgaven udtrykkeligt er en sammenligning.
10. Bevar fakta om hotelnavn, antal værelser, værelsestyper, m2, kapacitet, faciliteter, afstande, koordinater og destination.
11. Brug hotellets egen side og Expedia som primære faktakilder. Brug etablerede rejsebureauer som sekundære kilder, og brug ikke Trustpilot eller Booking.com.
12. Ved batch skal hoteller med Thailand Tours-link springes over, medmindre brugeren eksplicit beder om dem.
13. Kør `python scripts/check_hotel_tov.py {fil} --hotel-name "{hotelnavn}"` på færdige udkast, når outputtet findes som fil.
14. Kør slutkontrol for ændrede fakta, forbudte fraser, `I/jer/jeres`-form, tankestreger, maskinelle åbninger og salgsnegative afslutninger.

## Done-kriterier

Hoteloutput er færdigt, når:

- Gutenberg-strukturen er intakt.
- Hotel-description-block indeholder en rådgivende, konkret hoteltekst.
- Kort og attraktioner/afstande er bevaret eller tydeligt markeret til verificering.
- Værelsesafsnit forklarer forskelle uden at opfinde fakta.
- Teksten hjælper kunden med at vurdere hotellets match uden at sælge kunden væk fra siden.
- Et væsentligt kompromis er forklaret ærligt, men teksten slutter på hotellets positive match.
- Kilder, source URLs og usikre fakta er dokumenteret i fact_check ved draftarbejde.
- Der er ingen `I/jer/jeres` som direkte kundetiltale i kundevendt prosa.
- Der er ingen em dash eller en dash.

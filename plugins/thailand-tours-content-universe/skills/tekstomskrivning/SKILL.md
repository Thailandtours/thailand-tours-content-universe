---
name: tekstomskrivning
description: Bruges når rejsetekster for Thailand Tours skal omskrives eller videreføres i fælles tone-of-voice, herunder hoteller, destinationer, landesider og praktisk rejseinformation, med bevarelse af fakta, metadata, struktur og kvalitetstjek.
---

# Tekstomskrivning

Brug denne skill, når en rejsetekst skal omskrives til Thailand Tours / Lotus-lignende tone of voice, uden at miste fakta, struktur eller praktisk værdi.

## Hvornår skillen bruges

- Hoteltekster, destinationstekster og landesider.
- Tekster der føles robotiske, katalogagtige, for generiske eller svære at læse.
- Omskrivning hvor fakta, features, metadata og tekniske felter skal bevares.
- Rejseinformation med faste kategorier som visum, klima, transport, pakkeliste og nødsituationer.

## Referencefiler

Læs kun det nødvendige:

- `references/tone-of-voice.md` for stemme, rytme og tiltale.
- `references/rewrite-rules.md` for arbejdsgang og bevaringsregler.
- `references/banned-patterns.md` for formuleringer der skal undgås.
- `references/quality-checklist.md` før aflevering, især ved større batches.
- `references/hotel-source-policy.md` for hotelkilder, Expedia-faktatjek, billedvalg og batchregler.
- `references/hotel-output-format.md` for hotelstruktur.
- `references/hotel-template.md` som skabelon til ny hoteltekst.
- `references/examples-before-after.md` for konkrete omskrivningsmønstre.

## Arbejdsgang

1. Identificér teksttype: hotel, destination, landeside eller praktisk rejseinfo.
2. Find låste felter: frontmatter, faktafelter, features, adresse, afstande, priser, datoer, rating, destination og hotelnavn.
3. Omskriv kun den læsbare prosa, medmindre opgaven siger noget andet.
4. Gør åbningen konkret og sanselig, men ikke poetisk for poetikkens skyld.
5. Brug korte og lange sætninger i bevidst rytme.
6. Tilføj rådgivning: hvem passer det til, hvornår skal man vælge noget andet, hvad misforstår gæster ofte.
7. Kontrollér til sidst for forbudte mønstre, `I/jer/jeres`-form, tankestreger og ændrede fakta. Ved større opgaver bruges `references/quality-checklist.md`.

## Særligt for hotelkilder og batches

Ved hoteltekster og hotelmetadata skal `references/hotel-source-policy.md` bruges.

Kort regel:

- Brug hotellets egen side og Expedia som primære faktakilder.
- Brug Expedia som billedleverandør, download minimum 20 egnede billeder, og upload dem til WordPress med dansk SEO-metadata, når WP-adgang er tilgængelig.
- Expedia og aftalte leverandører behandles som godkendte billedleverandører med brugsret for Thailand Tours.
- Brug etablerede rejsebureauer som C&C Travel, Solfaktor, Unique Travel, Jysk Rejsebureau og lignende som sekundære kilder.
- Brug ikke Trustpilot eller Booking.com som faktakilder.
- Spring hoteller over i batch, hvis de allerede har Thailand Tours-link eller Thailand Tours-domæne i tekst, kildefelter eller websitefelter.
- Skriv altid draft-first ved batch: tekst, proposed metadata og galleri må ikke ændre live hoteldata direkte.

## Særligt for landesider og indrejsekrav

Indrejse, visum, vaccinationer, ankomstformularer, turistgebyrer, pasregler og nødnumre er tidsfølsomme. Brug altid aktuelle officielle kilder, typisk:

- Udenrigsministeriets rejsevejledninger og pas/visum-sider.
- Landets officielle immigration, eVisa, ambassade eller myndighedsportal.
- Officielle turist- eller sundhedsmyndigheder, når de beskriver obligatoriske formularer eller gebyrer.

Skriv kundevendt:

- Først kort konklusion.
- Derefter punktopdelt krav for krav.
- Forklar hvad kunden skal gøre før afrejse, ved ankomst og under opholdet.
- Undgå juridisk sprog, men vær præcis om tidsfrister, pasgyldighed, gebyrer og formularer.
- Tilføj altid en note om at regler kan ændre sig og bør tjekkes før betaling og afrejse.

## Done-kriterier

En omskrivning er færdig, når:

- Fakta og metadata er bevaret.
- Teksten kan læses højt uden at lyde som et katalog.
- Kunden forstår forskellen på stedet og alternativerne.
- Der er ingen `I/jer/jeres` som direkte kundetiltale i kundevendt prosa.
- Der er ingen em dash eller en dash.
- Der er ingen forbudte OTA-fraser.
- Praktiske krav er forklaret forståeligt og med forbehold, hvor regler kan ændre sig.

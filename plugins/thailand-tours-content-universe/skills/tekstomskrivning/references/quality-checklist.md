# Quality Checklist

Brug denne tjekliste før aflevering af omskrevne rejsetekster. Den er især vigtig ved batches, hvor små stilfejl ellers kan brede sig.

## 1. Struktur

- Kun én H1.
- Frontmatter/YAML er bevaret, hvis kilden havde det.
- Markdown-struktur matcher kilden eller den aftalte skabelon.
- Hoteltekster har typisk 4-6 fede mellemoverskrifter.
- Destinationstekster har typisk 5-8 fede mellemoverskrifter.
- Adresse-, afstands- og faktablokke er bevaret, hvis de fandtes i kilden.

## 2. Fakta

- Hotelnavne, destinationsnavne, lande, adresser og koordinater er ikke ændret.
- Ratings, antal værelser, værelsestyper, faciliteter og afstande er bevaret.
- Der er ikke tilføjet nye faciliteter, services eller claims uden kilde.
- Hotellets egen side er brugt som primær kilde ved hoteltekster, når den findes.
- Expedia er brugt til faktatjek af faciliteter og services ved hoteltekster, når den findes.
- Expedia er brugt som billedkilde til hotelgalleriet, når hotellet findes på Expedia.
- Expedia og aftalte leverandører behandles som godkendte billedleverandører med brugsret for Thailand Tours.
- Relevante rejsebureau-kilder er brugt som sekundære kilder, ikke som tekst der kopieres.
- Trustpilot og Booking.com er ikke brugt som faktakilder.
- Afstande og transporttider er skrevet med `ca.`, hvis de ikke er kildeverificeret.
- Usikre oplysninger er markeret som noget der skal verificeres, ikke skrevet som fakta.

## 3. Tone

- Teksten lyder som rådgivning fra et rejsebureau, ikke som OTA-katalog.
- Åbningen starter med en konkret detalje, kontrast eller rejseindsigt.
- Teksten forklarer hvad stedet betyder i praksis for kunden.
- Teksten hjælper også kunden med at fravælge stedet, hvis det ikke passer.
- Superlativer er undgået eller forankret i konkrete forhold.

## 4. Tiltale

- Kundevendt tekst bruger `I`, `jer` og `jeres`.
- Kundevendt tekst bruger ikke `du`, `dig`, `din`, `dit` eller `dine`.
- Direkte citater eller låste felter må kun bevares, hvis de ikke er del af brødteksten.

## 5. Forbudte tegn og formuleringer

- Ingen em dash: `—`.
- Ingen en dash: `–`.
- Ingen generiske OTA-fraser som `hotellet tilbyder`, `destinationen tilbyder`, `bredt udvalg`, `bred vifte`, `noget for enhver smag` eller `perfekt til alle`.
- Ingen vejrgarantier, sundhedsråd eller visumråd uden aktuel officiel kilde.

## 6. Hoteltekster

- Hotellet er ikke batch-omskrevet, hvis det allerede har Thailand Tours-link, medmindre brugeren bad om det.
- Introen forklarer hotellets klare rolle.
- Værelsesafsnit forklarer forskel på kategorier uden at opfinde facts.
- Pool, strand, spa, mad og børn/familie nævnes kun, hvis kilden understøtter det.
- Faciliteter fra live data er tjekket mod hotellets egen side og Expedia.
- Kildekonflikter er lagt i `fact_check.needs_review`.
- Billedgalleri har minimum 20 egnede Expedia-billeder, når Expedia har nok brugbare billeder.
- Expedia-billeder har Expedia som `source_url` eller tydelig billedkilde.
- Billeder med synlige ansigter eller personer i fokus er fravalgt, hvor det er muligt.
- Billeder er downloadet og uploadet til WordPress-mediebiblioteket, når WP-adgang er tilgængelig.
- WordPress `media_id`, endelig fil-URL, upload-sti, original `source_url`, billedtype og alt-tekst er registreret.
- Filnavne, titler, alt-tekster og beskrivelser er skrevet SEO-klart på dansk.
- Billedgalleri bruger Expedia/officielle hotel-/rejsebureau-URL'er, og ikke Booking.com eller Trustpilot.
- Slutningen har en klar `Vælg {hotelnavn} hvis...`-vurdering, når formatet tillader det.

## 7. Destinationer og lande

- Destinationstekster forklarer zoner, strande, logistik, sæson og målgruppe.
- Landetekster prioriterer praktisk klarhed over stemningssprog.
- Indrejse, visum, vaccinationer, turistgebyrer, pasregler og nødnumre tjekkes mod aktuelle officielle kilder.
- Regler beskrives med forbehold om, at de kan ændre sig før afrejse.

## 8. Rejser

- Rejsetekster er skrevet konsekvent til `I`, `jer` og `jeres`.
- Overblik, dagsprogram, hotelafsnit, prisnær tekst og lignende rejser bruger ikke `du`, `dig`, `din`, `dit` eller `dine`.
- Rejsens rækkefølge, tempo, antal dage, antal nætter og transfer er forklaret konkret.
- Det er tydeligt, hvad der er inkluderet, og hvad der blot er anbefalinger eller muligheder på egen hånd.
- Rejsen hjælper kunden med at vælge og fravælge ud fra tempo, skift, strandtid, byliv, natur og praktiske forbehold.

## 9. Slutkontrol

- Læs første og sidste afsnit højt. De skal lyde som samme brand.
- Søg efter `du`, `dig`, `din`, `dit`, `dine`, `—`, `–` og de forbudte fraser.
- Sammenlign kilden og output for faktaændringer.
- Markér eventuelle åbne verificeringspunkter i stedet for at skjule usikkerhed.

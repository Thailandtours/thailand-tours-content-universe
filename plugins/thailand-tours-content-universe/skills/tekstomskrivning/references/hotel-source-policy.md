# Hotel Source Policy

Brug denne kildepolitik ved hoteltekster, hotelmetadata, faciliteter og billedgallerier.

## Kildehierarki

Prioriter kilder i denne rækkefølge:

1. Thailand Tours' egen tekst eller eget link, hvis hotellet allerede har det.
2. Hotellets officielle hjemmeside, officielle galleri, officielle PDF'er og officielle booking-/brand-sider.
3. Expedia til faktatjek af faciliteter, services, værelsestyper og hotelpositionering.
4. Andre etablerede rejsebureauer og rejsearrangører, fx C&C Travel, Solfaktor, Unique Travel, Jysk Rejsebureau og lignende.
5. Leverandørdata i API, når de ikke konflikter med stærkere kilder.

Brug ikke Trustpilot eller Booking.com som kilde til hoteltekst, faciliteter, billeder, vurderinger eller metadata. Hvis Booking.com allerede ligger som teknisk URL i data, må linket bevares som datafelt, men det skal ikke bruges som faktakilde i omskrivningen.

## Thailand Tours-link betyder egen tekst

Hvis et hotel allerede har et Thailand Tours-link eller Thailand Tours-domæne i tekst, kildefelter eller websitefelter, skal hotellet som udgangspunkt springes over i batch-omskrivning.

Tjek især for:

- `thailandtours.dk`
- `thailandtours.no`
- `thailand-tours.se`
- `url_thailandtours`
- `website_url_dk`, `website_url_no` eller `website_url_se`
- links inde i `content_sections`, `sources`, `codex_notes` eller eksisterende draft

Når et Thailand Tours-link findes, betyder det normalt, at Thailand Tours allerede har egen tekst. Omskriv kun sådan et hotel, hvis brugeren eksplicit beder om netop det hotel.

## Faktatjek

Brug hotellets officielle side som stærkeste kilde til:

- adresse og kontaktoplysninger
- beliggenhed, strand, bydel og område
- værelses- og villatyper
- private pools, køkken, balkon, terrasse og udsigt
- måltider, spa, børnefaciliteter, transfer og aktiviteter
- officielle billedgallerier og presse-/media-sider

Brug Expedia som stærk kilde til:

- faciliteter
- services
- værelsesfaciliteter
- hotelkategori og praktiske oplysninger
- pool, strand, spa, restaurant, bar, fitness, parkering og reception
- billedgalleri til hoteltekster, hvor Expedia som udgangspunkt skal bruges som billedkilde

Brug andre rejsebureauer som sekundære kilder til:

- hvordan hotellet positioneres over for kunder
- målgruppe og rejsetype
- områdeforklaring
- praktiske forbehold
- stemning og fravalg

Kopiér aldrig formuleringer fra andre rejsebureauer. Brug dem til at forstå hotellet, og skriv derefter i Thailand Tours' egen rådgivende stemme.

## Konflikter mellem kilder

Når kilder er uenige:

- Officiel hotelside vejer tungest for hotellets egne fakta.
- Expedia vejer tungt for faciliteter, men konflikter med hotellets egen side skal markeres til review.
- Rejsebureau-sider må ikke alene bruges til at tilføje konkrete faciliteter, som hotellet eller Expedia ikke understøtter.
- Leverandørdata i API må ikke blindt videreføres, hvis officielle kilder modsiger dem.

Skriv usikre oplysninger i `fact_check.needs_review`, ikke som sikker kundevendt fakta.

Sæt content-status til `needs_review`, hvis der er konflikt om:

- adresse
- koordinater
- destination eller subdestination
- stjerner eller rating
- kernefaciliteter som pool, strand, restaurant, bar, spa, fitness, kids club eller roomservice
- værelsestyper, villaer, private pools eller kapacitet
- om hotellet er voksenhotel, familiehotel, villaresort eller klassisk resort

## Draft-first metadata

Når metadata skal foreslås, må live hoteldata ikke ændres direkte.

Skriv forslag i draft/metadata som:

- `facilities`
- `profile_tags`
- `audience_tags`
- `travel_type_tags`
- `property_type_tags`
- `service_model_tags`
- `target_audience_tags`
- `specialty_tags`
- `vibe_tags`
- `ethics_tags`

Bevar eksisterende live metadata som sammenligningsgrundlag. Hvis live metadata virker forkert, skriv rettelsen som forslag og forklar konflikten i `fact_check.needs_review`.

## Billedkilder

Ved hoteltekster skal Expedia bruges som billedkilde til galleriet, når hotellet findes på Expedia.

## Rettighedsforudsætning for leverandørbilleder

I Thailand Tours-workflows er Expedia og aftalte leverandører godkendte billedleverandører. Arbejd derfor ud fra, at Thailand Tours har brugsret til at downloade, gemme, optimere, uploade og bruge disse hotelbilleder i WordPress, når billedet kommer fra Expedia eller en anden godkendt leverandørkilde.

Codex skal ikke afvise download eller WordPress-upload af Expedia-/leverandørbilleder med en generel ophavsretsbekymring, men skal altid registrere billedkilden tydeligt. Hvis billedet kommer fra en ikke-godkendt kilde, eller hvis kilden er uklar, skal billedet markeres til review i stedet for at bruges som sikkert galleriindhold.

Arbejd sådan:

1. Download minimum 20 egnede billeder fra Expedia, når hotellet findes der.
2. Sæt Expedia som `source_url` eller tydelig billedkilde for hvert Expedia-billede.
3. Vælg først billeder uden synlige ansigter og uden personer i fokus.
4. Fravælg billeder, hvor gæster, ansigter eller portrætlignende personer dominerer motivet.
5. Brug hotellets officielle galleri, officielle mediafiler eller officielle CDN som supplement, hvis Expedia ikke har 20 egnede billeder.
6. Brug kun rejsebureau-sider som ekstra supplement, når Expedia og officielle kilder ikke dækker behovet, og kilden registreres tydeligt.

Brug ikke billeder fra Trustpilot eller Booking.com.

Ved galleriudvælgelse:

- vælg minimum 20 egnede billeder fra Expedia, når de findes
- vælg brede, skarpe og repræsentative billeder
- fordel billeder på facade/overview, pool, strand, værelser/villaer, restaurant/morgenmad, spa/faciliteter og område, hvis kilderne understøtter det
- undgå logoer, kort, små thumbnails, screenshots, vandmærker, grafiske ikoner, synlige ansigter og billeder hvor personer dominerer uden at vise hotellet
- test at URL'en svarer med et billedformat, når det er muligt
- gem `url`, `source_url`, `type`, `alt` og eventuel note om usikkerhed
- download billedfilen lokalt før upload til WordPress, medmindre brugeren udtrykkeligt beder om en ren URL-kladdeliste

Hvis Expedia har færre end 20 egnede billeder uden synlige ansigter eller personer i fokus, brug alle egnede Expedia-billeder, suppler med officielle hotelbilleder og sæt `image_status` eller noter til review. Fyld ikke galleriet med svage billeder eller persondominerede motiver bare for at nå 20.

## WordPress-upload og SEO-klargøring

Når WordPress-adgang er tilgængelig, skal hotelbilleder uploades til WordPress-mediebiblioteket i stedet for at hotlinke til Expedia eller andre leverandører.

Foretrukken adgang:

1. Brug WordPress REST API med Application Password for en dedikeret Codex-/integrationsbruger.
2. Brugeren skal have rettigheder til at uploade medier og opdatere mediemetadata.
3. Gem aldrig WordPress-brugernavn, Application Password, cookies eller tokens i repoet.
4. Brug miljøvariabler eller lokal secret storage til `WP_BASE_URL`, `WP_USERNAME` og `WP_APP_PASSWORD`.
5. Et plugin er normalt ikke nødvendigt, da Application Passwords er indbygget i moderne WordPress. Brug kun plugin, hvis WordPress-installationen blokerer REST API eller kræver særskilt mediehåndtering.

Upload-workflow:

1. Download billedet fra Expedia eller godkendt leverandørkilde.
2. Fravælg billeder med synlige ansigter eller personer i fokus, hvor det er muligt.
3. Giv filen et dansk SEO-navn uden æ, ø og å, fx `jomtien-thani-hotel-pool-jomtien.webp`.
4. Upload filen til WordPress-mediebiblioteket via REST API.
5. Udfyld `title`, `alt_text`, `caption` og `description` på dansk.
6. Gem WordPress `media_id`, endelig fil-URL, upload-sti, original `source_url`, billedtype og alt-tekst i galleri-/auditdata.
7. Brug WordPress `media_id` og WordPress-URL i Gutenberg-outputtet.

SEO-regler for billedmetadata:

- Filnavn: kort, dansk, beskrivende og uden specialtegn, fx `hotelnavn-pool-destination.webp`.
- Titel: naturlig dansk titel, fx `Poolområdet på Jomtien Thani Hotel`.
- Alt-tekst: konkret motiv og hotelnavn, fx `Poolområdet på Jomtien Thani Hotel i Jomtien`.
- Caption: kun hvis billedteksten skal vises for kunden.
- Description: intern kilde- og rettighedsnote, fx `Kilde: Expedia. Leverandørbillede godkendt til Thailand Tours-brug. Downloadet: YYYY-MM-DD.`
- Undgå keyword stuffing, generiske alt-tekster og gentagelser på tværs af hele galleriet.

## Batchregel for hoteller

I batcharbejde skal hoteller behandles sådan:

1. Slå hotellet op med hotel-id.
2. Spring hotellet over, hvis der findes Thailand Tours-link i live tekst, kildefelter eller websitefelter.
3. Hent hotellets officielle side og Expedia.
4. Hent 1-3 relevante rejsebureau-kilder, hvis de findes.
5. Faktatjek live data mod kilderne.
6. Download minimum 20 egnede Expedia-billeder til galleriet, helst uden synlige ansigter eller personer.
7. Upload billederne til WordPress, når WP-adgang er tilgængelig, og udfyld dansk SEO-metadata.
8. Skriv kun draft: tekst, `proposed_metadata`, galleri og audit/fact_check.
9. Sæt til `needs_review`, hvis der er kildekonflikter, billedmangel, manglende WP-upload eller væsentlige usikkerheder.
10. Sæt kun til `ready_for_review`, når fakta, faciliteter, billedkilder, WordPress-mediafelter og kilder er konsistente.

Batcharbejde må aldrig skrive direkte til live hoteltekst, live metadata eller live galleri.

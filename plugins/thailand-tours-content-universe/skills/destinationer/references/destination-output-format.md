# Destination Output Format

Destinationstekster skrives som WordPress/Gutenberg-output. Strukturen er typisk en lang side med flere faste sektioner:

1. Intro.
2. Rejsesøgning og kontaktblok.
3. Rejsemål/underdestinationer.
4. Redaktørstyrede indholdssektioner med media-text og foldout.
5. Sæson og bedste rejsetid.
6. Fakta og information i accordion-blokke.
7. Kort.
8. Udvalgte hoteller.
9. Pakkerejse-afsnit.
10. Inspiration og trustbar.

## 1. Intro

Introen ligger normalt i:

```html
<div id="intro" class="wp-block-group content-entry-group">
  <h1>Rejser til [post_title] [year]</h1>
  <p><strong>{kort positionerende intro}</strong></p>
  <p>{uddybende introduktion}</p>
</div>
```

Bevar:

- `id="intro"`.
- H1-strukturen.
- Placeholders som `[post_title]` og `[year]`.
- Links i introen, hvis de findes.

Introen skal:

- Starte konkret og rådgivende.
- Forklare hvorfor destinationen er værd at vælge.
- Undgå generiske paradisfraser.
- Bruge `I`, `jer` og `jeres`, ikke `du`.

## 2. Rejsesøgning

Rejsesøgningen ligger normalt i:

```html
<div id="rejser" class="wp-block-group search-travel-group">
  <h2>Din ferie på {destination} starter hos [site_title]</h2>
  <p>{kort salgs- og rådgivningstekst}</p>
  <!-- wp:pan/travel-search-block {"blockId":"..."} /-->
  <!-- wp:pan/contact-info-block {"blockId":"...","userID":"..."} /-->
</div>
```

Bevar:

- `id="rejser"`.
- `pan/travel-search-block`.
- `pan/contact-info-block`.
- `blockId`.
- `userID`.
- `[site_title]`.

## 3. Rejsemål/underdestinationer

Sektionen har normalt:

```html
<div id="rejsemaal" class="wp-block-group">
  <p>[ez-toc]</p>
  <h2>Skønne rejsemål på {destination}</h2>
  <p>{overblik over områder, strande eller byer}</p>
  <!-- wp:pan/travel-archive-block {"elementType":"destinations",...} /-->
</div>
```

Bevar:

- `[ez-toc]`.
- `pan/travel-archive-block`.
- `elementType`.
- `filterSection`.
- `resultsPerLoad`.

Teksten skal forklare forskelle mellem områder:

- Roligt vs. livligt.
- Familie vs. par.
- Strand vs. by.
- Logistik og afstande.
- Hvem bør vælge hvilket område.

## 4. Indholdssektioner og media-text

Destinationstekster bruger ofte `wp:media-text` og grupper som:

```html
<div id="beskrivelse" class="wp-block-group travel-destination-title-group">
  <h3>{konkret overskrift}</h3>
  <p>{beskrivelse}</p>
</div>
```

Og:

```html
<div class="wp-block-group travel-decription-group foldout-group">
  <!-- wp:media-text ... -->
</div>
```

Bevar:

- `mediaId`.
- `mediaLink`.
- `mediaType`.
- `mediaWidth`.
- `mediaSizeSlug`.
- image `src`, `alt`, `class`.
- foldout classes.

Omskriv tekst, men ikke billeddata eller tekniske felter.

## 5. Sæson og bedste rejsetid

Sæsonsektionen har ofte:

```html
<h2>Hvornår er det bedst at rejse til {destination}?</h2>
```

Og månedsspecifikke afsnit:

```html
<h3>Rejser til {destination} i januar [year offset=11]</h3>
```

Bevar:

- `[year]`.
- `[year offset=...]`.
- Media-text struktur.
- Eventuelle billeder og billed-alt.

Skriv sæson praktisk:

- Bedste rejsetid.
- Regntid/tørtid.
- Havforhold, bølger, bådture og snorkling.
- Højsæson og bookingbehov.
- Lavsæsonens fordele og ulemper.

Undgå vejrgarantier. Skriv `typisk`, `som regel`, `kan påvirke` og `ofte`, når vejret varierer.

## 6. Fakta og information

Faktaområdet starter typisk med:

```html
<h2 id="fakta">Fakta og information om {destination}</h2>
```

Efterfulgt af:

```html
<div class="wp-block-group accordions-list-group">
  <!-- wp:pan/simple-accordion-block {"blockId":"...","headline":"Information"} -->
  ...
  <!-- /wp:pan/simple-accordion-block -->
</div>
```

Bevar:

- `id="fakta"`.
- `accordions-list-group`.
- `pan/simple-accordion-block`.
- `blockId`.
- `headline`.
- Links og target/rel-attributter.

Typiske accordion-headlines:

- `Information`.
- `Området`.
- `Hvad spiser og drikker man på {destination}?`
- `Hvordan er strandene på {destination}?`
- `Er {destination} et børnevenligt rejsemål?`
- `Hvor skal man bo på {destination}?`
- `Hvilke aktiviteter og seværdigheder er der?`
- `Hvordan er vejret på {destination}?`
- `Hvordan foregår flyrejsen til {destination}?`
- `Hvordan med transfer på {destination}?`
- `Hvordan med markeder og shopping på {destination}?`
- `Hvordan er nattelivet på {destination}?`
- `Hvordan kommer man rundt på {destination}?`
- `Kan man dyrke sport og træning på {destination}?`
- `Hvilke udflugter kan man komme på?`
- `Hvem rejser til {destination}?`

## 7. Kort

Kortsektionen har normalt:

```html
<div id="kort" class="wp-block-group destination-map-group">
  <h2>Kort over [post_title] med hoteller</h2>
  <p>{kort forklaring}</p>
  [mapster_wp_map id="..."]
</div>
```

Bevar:

- `id="kort"`.
- `destination-map-group`.
- `[post_title]`.
- `[mapster_wp_map id="..."]`.

## 8. Udvalgte hoteller

Hotel-sektionen har normalt:

```html
<div id="hoteller" class="wp-block-group featured-hotels-group">
  <h2><a href="{hoteloversigt}">Udvalgte hoteller på {destination}</a></h2>
  <p>{kort rådgivningstekst}</p>
  <!-- wp:pan/travel-offerings-slider-block {"elementType":"hotels","selectedElements":[]} /-->
</div>
```

Bevar:

- `id="hoteller"`.
- `featured-hotels-group`.
- Hotel-link.
- `pan/travel-offerings-slider-block`.
- `blockId`, `elementType` og `selectedElements`.

## 9. Pakkerejse-afsnit

Pakkerejse-afsnittet har normalt en centreret H2 og 2-3 paragraffer om pakkerejse, rejsegaranti, fly, hotel og transfer.

Skriv kundevendt og konkret:

- Hvad er inkluderet?
- Hvorfor er det trygt?
- Hvordan hjælper Thailand Tours?
- Hvilke lufthavne eller rejseformer er relevante, hvis kilden nævner dem?

## 10. Inspiration og trustbar

Bevar altid de afsluttende blokke, hvis de findes:

```html
<div id="inspiration" class="wp-block-group">
  <!-- wp:pan/featured-blog-posts-v2-block /-->
</div>

<!-- wp:pan/trust-bar-block {"blockId":"..."} /-->
```

## Bevar altid

- WordPress block comments.
- `id`, `className`, `blockId`, `mediaId`, `mediaLink`, `mediaType`, `mediaSizeSlug`, `selectedElements`, `elementType`, `userID` og shortcode ids.
- Placeholders: `[post_title]`, `[year]`, `[site_title]`, `[year offset=...]`.
- Shortcodes: `[ez-toc]`, `[mapster_wp_map id="..."]`.
- Links, href, target og rel-attributter.
- Destinationens navn, områder, strande, lufthavne, afstande, sæsoner og praktiske fakta.

## Omskriv typisk

- Intro.
- Rejsesøgningstekst.
- Beskrivelse af rejsemål/områder.
- Media-text brødtekst.
- Sæsonafsnit.
- Accordion-tekst.
- Kortforklaring.
- Hotel- og pakkerejsetekst.
- `du`-form til `I`/`jer`/`jeres`.

## Kvalitetstjek for destinationer

- Er Gutenberg-strukturen stadig intakt?
- Er alle custom blocks og shortcodes bevaret?
- Er placeholders bevaret?
- Er links bevaret?
- Er destinationens zoner, sæson og praktiske logistik forklaret konkret?
- Er der tydelig rådgivning om hvem destinationen passer til?
- Er alle `du/dig/din/dit/dine` omskrevet?
- Er der ingen `—` eller `–`?
- Er visum, sundhed, sikkerhed og aktuelle regler verificeret eller markeret til verificering?

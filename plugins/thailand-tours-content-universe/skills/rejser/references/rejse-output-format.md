# Rejse Output Format

Rejsetekster skrives som WordPress/Gutenberg-output. Strukturen bruges til rejser, rundrejser, kombinationsrejser og pakkerejser.

En rejse har typisk:

1. Overblik.
2. Inkluderet-boks med prisvisning.
3. Kort over rejsen.
4. Rejseprogram med `pan/trip-day-block`.
5. Kontaktblok.
6. Anbefalede hoteller.
7. Prisblok.
8. Lignende rejser.
9. Trustbar.

## 1. Overblik

Overblikket ligger normalt i:

```html
<div id="overblik" class="wp-block-group content-entry-group">
  <h2>Rundrejse til {destinationer} - {antal dage} dage</h2>
  <p class="has-text-align-center">{kort rejsebeskrivelse}</p>
</div>
```

Bevar:

- `id="overblik"`.
- `content-entry-group`.
- H2-strukturen.
- Rejsens navn, destinationer og antal dage.
- Eksisterende links, hvis de findes.

Overblikket skal:

- Forklare rejsens rute og logik.
- Gøre tempo, kombination og målgruppe tydelig.
- Nævne de vigtigste destinationer i korrekt rækkefølge.
- Slutte med en tydelig anbefaling, hvis kilden bruger formatet `Vi vil anbefale jer denne rejse, hvis...`.
- Bruge `I`, `jer` og `jeres`, ikke `du`.

## 2. Inkluderet-boks og prisvisning

Inkluderet-boksen ligger ofte i en full-bleed barsektion:

```html
<div class="wp-block-uagb-container pan-barsection full-bleed-bg ...">
  <div class="wp-block-uagb-container pan-barsection--popout ...">
    <h3>Rejsen inkluderer</h3>
    <ul>
      <li>Fly Danmark-Bangkok t/r</li>
      <li>Alle skatter og afgifter</li>
      <li>{nætter og inkluderede dele}</li>
    </ul>
    <!-- wp:pan/travel-price-display-block /-->
  </div>
</div>
```

Bevar:

- `pan-barsection`.
- `pan-barsection--popout`.
- `pan-barsection--content`.
- `pan/travel-price-display-block`.
- Separatorblokke og farveklasser.
- Alle konkrete inkluderede elementer, nætter, måltider, transfer, skatter og rejsegaranti.

Omskriv kun kundevendt tekst i listen, hvis sproget skal ensrettes. Ændr ikke tal, nætter eller inkluderede elementer uden kilde.

## 3. Tags og kort

Den højre del af barsektionen indeholder ofte tags, kortoverskrift og kortbillede:

```html
<!-- wp:pan/travel-tags-block {"blockId":"...","taxonomyType":"travel-categories"} /-->
<h3>Kort over rejsen</h3>
<p>Klik på kortet og få det vist i stor størrelse</p>
<figure class="wp-block-image size-full pan-map-preview">
  <img src="..." alt="" class="wp-image-..."/>
</figure>
```

Bevar:

- `pan/travel-tags-block`.
- `blockId`.
- `taxonomyType`.
- `pan-map-preview`.
- Image `id`, `src`, `alt` og `class`.

Kortteksten må gerne gøres mere informativ, men billeddata må ikke ændres.

## 4. Rejseprogram

Rejseprogrammet ligger normalt i:

```html
<div id="rejseprogram" class="wp-block-group travel-program-group">
  <h2>Rejseprogram</h2>
  <!-- wp:pan/trip-day-block {"blockId":"...","durationDays":"2-6","headline":"...","recommendations":"...","mediaID":...,"hotelID":"..."} -->
  <p>{programtekst}</p>
  <!-- /wp:pan/trip-day-block -->
</div>
```

Bevar:

- `id="rejseprogram"`.
- `travel-program-group`.
- Alle `pan/trip-day-block`.
- `blockId`.
- `durationDays`.
- `headline`.
- `content`.
- `recommendations`.
- `mediaID`, `mediaID2`, `mediaID3` osv.
- `mediaPreviewURL`, `mediaPreviewURL2`, `mediaPreviewURL3` osv.
- `hotelID`.
- Tomme paragraffer, hvis de bruges af blokstrukturen.

Rejseprogrammet skal:

- Følge rejsens faktiske rækkefølge.
- Forklare transfer og skift mellem destinationer.
- Beskrive oplevelser konkret uden at love bestemte oplevelser, hvis de ikke er inkluderet.
- Skelne mellem inkluderet program, anbefalinger og muligheder på egen hånd.
- Give kunden fornemmelse af tempo, variation og hvorfor hvert stop er med.

## 5. Typiske dagsblokke

### Afrejse

Første dagsblok handler ofte om afrejse fra Danmark.

Bevar fly- og lufthavnsinfo, men skriv med forbehold:

- Rejsen kan typisk starte fra relevante lufthavne, hvis kilden nævner dem.
- Stop, flytid, klasse og opgraderinger må ikke garanteres uden kilde.
- Skriv at Thailand Tours hjælper med sammensætningen, hvis det fremgår af kilden.

### Destinationer undervejs

Destinationens blok skal normalt indeholde:

- Ankomst eller transfer.
- Hvor længe opholdet varer.
- Hvad området er kendt for.
- Konkrete oplevelser og anbefalinger.
- Praktiske forbehold om afstande, transport, sæson eller aktivitetsniveau.
- Hotelrelation, hvis `hotelID` findes.

### Hjemrejse og ankomst

Sidste blokke handler ofte om hjemrejse eller ankomst til Danmark.

Skriv kort og roligt. Bevar eventuelle flybilleder og tekniske felter.

## 6. Kontaktblok

Efter rejseprogrammet ligger ofte:

```html
<!-- wp:pan/contact-info-block {"blockId":"...","userID":"..."} /-->
```

Bevar:

- `pan/contact-info-block`.
- `blockId`.
- `userID`.

## 7. Anbefalede hoteller

Hotel-sektionen har normalt:

```html
<div id="hoteller" class="wp-block-group featured-hotels-group">
  <h2>Anbefalede hoteller på rejsen</h2>
  <p>{kort tekst}</p>
  <!-- wp:pan/travel-offerings-slider-block {"elementType":"hotels","selectedElements":["..."]} /-->
</div>
```

Bevar:

- `id="hoteller"`.
- `featured-hotels-group`.
- `tag_hoteller`.
- `pan/travel-offerings-slider-block`.
- `blockId`.
- `elementType`.
- `selectedElements`.

Teksten skal forklare, at hoteller kan tilpasses, hvis det er korrekt for rejsen.

## 8. Prisblok

Prisområdet har normalt:

```html
<div id="pris" class="wp-block-group">
  <!-- wp:pan/travel-price-list-block {"blockId":"...","rows":[...],"rowCount":"..."} /-->
</div>
```

Bevar:

- `id="pris"`.
- `pan/travel-price-list-block`.
- `blockId`.
- `rows`.
- `rowCount`.
- Alle datoer, prisværdier og brandfelter.

Ændr aldrig priser, datoer eller rækkeantal uden en eksplicit kilde.

## 9. Lignende rejser

Sektionen ligger ofte til sidst:

```html
<h2 id="ligende-rejser">Lignende rejser</h2>
<!-- wp:pan/travel-offerings-slider-block {"elementType":"travels","selectedElements":["..."]} /-->
```

Bevar:

- H2 id, også hvis den eksisterende stavning er `ligende-rejser`.
- `pan/travel-offerings-slider-block`.
- `elementType="travels"`.
- `selectedElements`.

## 10. Trustbar

Bevar altid trustbar-blokken, hvis den findes:

```html
<!-- wp:pan/trustpilot-bar-block {"blockId":"..."} /-->
```

## Bevar altid

- WordPress block comments.
- `id`, `className`, `block_id`, `blockId`, `userID`, `taxonomyType`, `hotelID`, `selectedElements`, `elementType`, `rowCount` og `rows`.
- `durationDays`, `headline`, `content`, `recommendations`, `mediaID`, `mediaPreviewURL` og alle nummererede varianter.
- Image `id`, `src`, `alt`, `class`, `sizeSlug` og `linkDestination`.
- Prisdata, datoer, antal nætter, antal måltider, transferformer og inkluderede elementer.
- Destinationernes rækkefølge og rejsens antal dage.

## Omskriv typisk

- Overblik.
- Anbefalingsafsnit.
- Tekst under kort.
- Dagsprogrammer.
- Kundevendte hotel- og prisafsnit.
- `du`-form til `I`/`jer`/`jeres`.

## Kvalitetstjek for rejser

- Er Gutenberg-strukturen stadig intakt?
- Er alle custom blocks, block ids og billeddata bevaret?
- Er alle prisrækker, datoer og beløb uændrede?
- Er rejsens destinationer, antal dage og nætter uændrede?
- Er transfer og tempo forklaret konkret?
- Er det tydeligt, hvad der er inkluderet, og hvad der blot er forslag?
- Er der tydelig rådgivning om hvem rejsen passer til?
- Er alle `du/dig/din/dit/dine` omskrevet?
- Er der ingen `—` eller `–`?
- Er fly, indrejse, visum, sundhed, sikkerhed og aktuelle regler verificeret eller markeret til verificering?

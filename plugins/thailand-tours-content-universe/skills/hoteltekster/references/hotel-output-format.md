# Hotel Output Format

Hoteltekster skrives som WordPress/Gutenberg-output. Strukturen består typisk af tre hoveddele:

1. Showcase med billedgalleri og `pan/hotel-description-block`.
2. Kort og attraktioner/afstande.
3. Rejse- eller inspirationsslider nederst.

## 1. Showcase

Bevar den ydre container med `id="showcase"` og classes som:

```html
pan-unit-showcase hotel-description tag_kort
```

Showcase består normalt af:

- Venstre side: `uagb/image-gallery` med `mediaGallery`, `mediaIDs`, billed-URL'er, image ids og lightbox-indstillinger.
- Højre side: `pan/hotel-description-block` med `blockId` og `selectedFeaturesJSON`.

Bevar altid:

- `block_id`
- `mediaGallery`
- `mediaIDs`
- billed-URL'er
- `pan/hotel-description-block`
- `blockId`
- `selectedFeaturesJSON`
- feature ids og labels
- class names

Omskriv ikke billeddata, feature JSON eller tekniske felter, medmindre opgaven specifikt beder om det.

## 2. Hotelbeskrivelsen

Hotelteksten ligger inde i:

```html
<!-- wp:pan/hotel-description-block {...} -->
  <!-- wp:paragraph -->
  <p>{hoteltekst}</p>
  <!-- /wp:paragraph -->
<!-- /wp:pan/hotel-description-block -->
```

Hotelbeskrivelsen bør normalt indeholde:

- En konkret åbning, der forklarer hotellets rolle og første indtryk.
- 4-7 afsnit med fede indledninger i samme paragraf: `<strong>{mellemoverskrift}</strong><br>`.
- Et afsnit om beliggenhed og praktisk base.
- Et afsnit om hotellets stemning, niveau og målgruppe.
- Et afsnit om pool, strand, spa, mad eller aktiviteter, hvis kilden understøtter det.
- Et tydeligt værelsesafsnit med de vigtigste kategorier.
- En afsluttende vurdering: hvem skal vælge hotellet, og hvem bør vælge noget andet.

God afsnitsform:

```html
<!-- wp:paragraph -->
<p><strong>Strand foran, jungle bagved</strong><br>I får en rolig base, hvor stranden er tæt på hverdagen, men hvor hotellet stadig føles trukket tilbage fra øens mere travle områder.</p>
<!-- /wp:paragraph -->
```

Undgå:

```html
<p>Hotellet tilbyder et bredt udvalg af faciliteter og er perfekt til alle.</p>
```

## 3. Værelsesafsnit

Værelsesafsnit kan ligge som en samlet sektion med flere paragraffer.

Bevar:

- Værelsesnavne.
- Størrelser i m2.
- Kapacitet.
- Sengestørrelser.
- Udsigt.
- Balkon/terrasse.
- Pool, køkken, opholdsrum eller direkte strandadgang, hvis kilden nævner det.

Forklar forskellen mellem kategorierne i kundesprog:

- Hvem skal vælge standardværelse?
- Hvornår giver suite mening?
- Hvornår er villa eller poolvilla pengene værd?
- Hvad betyder beliggenheden i praksis?

Opfind aldrig nye værelsestyper, faciliteter eller udsigter.

## 4. Kort og attraktioner

Kortsektionen har normalt:

```html
<div id="kort" class="wp-block-uagb-container pan-map-and-attractions full-bleed ...">
  <!-- wp:pan/hotel-map-block {"schemaVersion":"1","lat":...,"lng":...,"zoom":...} /-->
  <h3>Attraktioner og afstande til hotellet</h3>
  <ul>{afstande og attraktioner}</ul>
</div>
```

Bevar:

- `id="kort"`.
- `pan/hotel-map-block`.
- `lat`, `lng` og `zoom`.
- Attraktionsnavne.
- Afstande.
- Lufthavne og havne.

Skriv afstandspunkter kort og konkret:

```html
<li><strong>{sted}: </strong>{kort forklaring} - ca. {afstand}</li>
```

Hvis afstande ikke er verificeret, brug `ca.` eller marker punktet til verificering.

## 5. Rejse-slider nederst

Bevar nederste gruppe med `id="rejser"` og `pan/travel-offerings-slider-block`.

Typisk struktur:

```html
<div id="rejser" class="wp-block-group content-entry-group">
  <h2>{slideroverskrift}</h2>
  <!-- wp:pan/travel-offerings-slider-block {"blockId":"...","elementType":"blogposts","selectedElements":[...]} /-->
</div>
```

Bevar:

- `blockId`
- `elementType`
- `selectedElements`

Overskriften kan omskrives, hvis den skal passe til destinationen:

- `Lær {destination} bedre at kende`
- `Rejser med ophold på {hotelnavn}`
- `Inspiration til {område}`

## Bevar altid

- WordPress block comments.
- Custom blocks fra `pan/` og `uagb/`.
- `id`, `className`, `block_id`, `blockId`, `mediaId`, `mediaIDs`, `mediaGallery`, `selectedFeaturesJSON`, `lat`, `lng`, `zoom` og `selectedElements`.
- Hotelnavn, destination, adresse, koordinater, attraktioner, afstande, værelsestyper, m2, features og faciliteter.

## Omskriv typisk

- Intro.
- Kundevendt hotelbeskrivelse.
- Fede mellemoverskrifter inde i brødteksten.
- Forklaring af værelsestyper.
- Attraktionsbeskrivelser, hvis de er generiske eller uklare.
- `du`-form til `I`/`jer`/`jeres`.

## Kvalitetstjek for hoteller

- Er Gutenberg-strukturen stadig intakt?
- Er billedgalleri, feature JSON, kort og slider bevaret?
- Er hotelnavn, værelsesnavne, m2, afstande og faciliteter uændrede?
- Starter teksten konkret, ikke som en generisk hotelannonce?
- Forklarer teksten hvem hotellet passer til, og hvem det ikke passer til?
- Er alle `du/dig/din/dit/dine` omskrevet?
- Er der ingen `—` eller `–`?
- Er usikre afstande eller facts markeret til verificering?

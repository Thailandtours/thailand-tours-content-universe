# Udflugt Output Format

Udflugter skrives som WordPress/Gutenberg-output. Strukturen består typisk af tre hoveddele:

1. Pris- og infoboks med inkluderet, ikke inkluderet, afgang og pris.
2. Beskrivelse af turen med intro, billede/tekst, dagsprogram og praktiske detaljer.
3. Rejse-slider nederst med relevante rejser.

## 1. Pris- og infoboks

Bevar containeren med `id="pris"` og de eksisterende Gutenberg-kommentarer/classes, når du omskriver en eksisterende side.

Venstre boks har normalt:

```html
<h3>Turen inkluderer</h3>
<ul>
  <li>{inkluderet punkt}</li>
  <li>{inkluderet punkt}</li>
</ul>

<p><strong>Ikke inkluderet i prisen</strong></p>
<ul>
  <li>{ikke inkluderet punkt}</li>
</ul>

<p><strong>Afgang og tider</strong></p>
<ul>
  <li>{afgang og tidspunkt}</li>
</ul>

<p><strong>{prislinje}</strong><br>{prisforbehold}</p>
```

Skriv inkluderede elementer konkret og faktuelt:

- Transportform.
- Guide.
- Entréer eller aktiviteter.
- Måltider.
- Overnatning, hvis relevant.
- Særlige både, tog, transfer eller lokale transportmidler.

Skriv ikke `bredt udvalg`, `mange spændende oplevelser` eller andre generiske fyldfraser.

## 2. Kortsektion

Højre boks har normalt:

```html
<h3>Startpunktet for turen</h3>
<!-- wp:mapster/mapster-select-map-block {"map_id":"...","className":"pan-map-preview"} /-->
```

Bevar `map_id`, block markup og class names, medmindre opgaven beder om et nyt kort.

## 3. Beskrivelse af turen

Beskrivelsesgruppen har normalt:

```html
<div id="beskrivelse" class="wp-block-group activity-description-group">
  <h2>Beskrivelse af turen</h2>
  {intro, billede/tekst og dagsprogram}
</div>
```

Introen skal:

- Starte konkret med turens rytme, afgang, landskab, transport eller første oplevelse.
- Forklare hvad turen giver i praksis.
- Nævne varighed og tempo, hvis det er relevant.
- Bruge `I`, `jer` og `jeres`, ikke `du`.

God retning:

```markdown
I bliver hentet tidligt, så Bangkok kan slippe sit greb, mens landskabet åbner sig mod kanaler, flod og jungle.
```

Undgå:

```markdown
På denne spændende tur vil du opleve mange fantastiske seværdigheder.
```

## 4. Dagsprogram

Brug `Dag 1`, `Dag 2`, `Dag 3` osv. som H3, når turen strækker sig over flere dage.

Hvert dagsafsnit skal normalt forklare:

- Hvor dagen starter.
- Transport og ca. køretid, hvis kilden har det.
- Dagens vigtigste stop i rigtig rækkefølge.
- Måltider og overnatning.
- Praktiske forhold: gang, badetøj, trapper, varme, tidlig afgang, trafik, retur.

Skriv historiske og kulturelle afsnit respektfuldt og præcist. Ved krigshistorie, mindesteder og museer skal tonen være rolig og faktuel, ikke dramatisk for effektens skyld.

## 5. Rejse-slider nederst

Bevar nederste gruppe med `id="rejser"` og den eksisterende slider-block.

Overskriften følger normalt:

```html
<h2>Rejser i {område eller destination}</h2>
<!-- wp:pan/travel-offerings-slider-block {"blockId":"..."} /-->
```

Bevar `blockId`, hvis outputtet bygger på en eksisterende side.

## Bevar altid

- WordPress block comments.
- `id`, `className`, `block_id`, `map_id`, `mediaId`, `mediaLink`, `mediaType`, `blockId` og custom block markup.
- Pris, minimumsantal, måltider, afgang, retur, inkluderede elementer og ikke inkluderede elementer.
- Destinationer, attraktioner, museer, transportformer og historiske fakta.

## Omskriv typisk

- Intro.
- Brødtekst.
- Dagsprogram.
- Generiske beskrivelser.
- Uklare praktiske forklaringer.
- `du`-form til `I`/`jer`/`jeres`.

## Kvalitetstjek for udflugter

- Er strukturen stadig gyldig WordPress/Gutenberg-output?
- Er pris og inkluderet/ikke inkluderet bevaret?
- Er dagsprogrammet i rigtig rækkefølge?
- Er tempo, transport og måltider forståelige?
- Er tonen rådgivende og konkret?
- Er alle `du/dig/din/dit/dine` omskrevet?
- Er der ingen `—` eller `–`?
- Er usikre tider/priser markeret til verificering?

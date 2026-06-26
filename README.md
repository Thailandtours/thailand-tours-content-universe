# Thailand Tours Content Universe

Dette repo er master for Thailand Tours' fælles Codex-plugin til tekstomskrivning.

Plugin'et indeholder en `tekstomskrivning`-skill med fælles tone-of-voice, omskrivningsregler, forbudte formuleringer, outputformater, eksempler og kvalitetstjek.

## Det vigtigste at redigere

- `plugins/thailand-tours-content-universe/skills/tekstomskrivning/references/tone-of-voice.md`
- `plugins/thailand-tours-content-universe/skills/tekstomskrivning/references/rewrite-rules.md`
- `plugins/thailand-tours-content-universe/skills/tekstomskrivning/references/examples-before-after.md`
- `plugins/thailand-tours-content-universe/skills/tekstomskrivning/references/banned-patterns.md`
- `plugins/thailand-tours-content-universe/skills/tekstomskrivning/references/quality-checklist.md`

## Opdateringsprincip

Ret kun masterversionen her, når ændringen skal gælde for hele teamet.

Efter ændringer:

1. Opdater relevante referencefiler.
2. Kør plugin-validering.
3. Bump versionen i `plugins/thailand-tours-content-universe/.codex-plugin/plugin.json`.
4. Commit og push til GitHub.
5. Bed teamet opdatere plugin'et og starte en ny Codex-tråd.

## Plugin marketplace

Repoets marketplace ligger her:

```text
.agents/plugins/marketplace.json
```

Plugin-kilden ligger her:

```text
plugins/thailand-tours-content-universe/
```


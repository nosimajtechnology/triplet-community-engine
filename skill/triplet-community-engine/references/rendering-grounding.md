# Reference-Grounded PS2 Fidelity

Gameplay fidelity comes from inspected original-build images, not retro keywords or post-applied filters.

## Resolve the active build

Resolve once in this order:

1. **User** — explicit game, console, platform, year, or rendering instruction
2. **Inherited** — latest approved frame or storyboard
3. **Engine** — a deliberate PS2 title/build chosen to fit the environment and action
4. **Default** — sixth-generation PS2 game-world construction

Record internally:

```text
ERA SELECTION SOURCE: user | inherited | Engine | default
TARGET BUILD: game / platform / year or PS2 sixth generation
GROUNDING REQUIRED: yes | no
```

Do not ask the user to choose when the concept can be routed confidently. Mention an Engine-selected build only when it materially affects the result.

## Research authentic captures

Before the first or genesis frame, retrieve and visually inspect three to five useful screenshots when available:

1. action and gameplay-camera reference
2. environment and architecture reference
3. geometry, texture, material, and lighting reference
4. optional NPC, vehicle, machinery, or prop reference
5. optional exact named-game/platform reference

Prefer identifiable original-platform gameplay captures, then original-platform in-engine cutscenes, then contemporary reviews, manuals, official archives, or reliable screenshot databases that clearly identify the game, platform, and release.

Reject remasters, remakes, HD collections, later ports, backward-compatible enhancements, emulator texture packs, widescreen hacks, fan patches, ReShade, mods, promotional art, box art, pre-rendered cinematics, fan renders, modern concept art, and captures whose platform cannot be reasonably identified. Inspect the images themselves; titles and prose are not visual inspection.

Do not commit or redistribute third-party screenshots in a public package.

## Assign narrow roles

```text
TRIPLET IDENTITY AUTHORITY — bundled turnaround; identity only.
APPROVED PROJECT AUTHORITY — wardrobe, props, environment, geography, light, and action state.
GAMEPLAY REFERENCE A — action camera, subject scale, and spacing only.
GAMEPLAY REFERENCE B — environment massing, asset density, and draw distance only.
GAMEPLAY REFERENCE C — geometry, textures, materials, lighting, shadows, and effects only.
SECONDARY CHARACTER AUTHORITY — one isolated block per character.
```

Never tell a model to blend every reference. Gameplay references cannot overwrite TripleT, a secondary identity, an approved outfit, or current scene state.

## Derive the rendering contract

Write a compact internal contract before prompting:

```text
ERA SELECTION SOURCE: [...]
TARGET BUILD: [...]
SOURCE QUALITY: [...]
REFERENCE ROLES: [...]
OBSERVED GEOMETRY: [...]
OBSERVED TEXTURES / FILTERING / UV: [...]
OBSERVED MATERIALS / LIGHTING / SHADOWS: [...]
OBSERVED ENVIRONMENT / EFFECTS / DRAW DISTANCE: [...]
OBSERVED CAMERA / SUBJECT SCALE / ANIMATION: [...]
CAPTURE CHARACTERISTICS: [aspect, resolution feel, aliasing, post-processing]
DECISIVE EXCLUSIONS: [wrong era, remasters, mods, modern cues]
IDENTITY PRESERVATION: [body, face, limbs, feet, grain, silhouette]
```

For a broad PS2 request, choose screenshot references that fit the premise rather than mechanically applying one universal GTA-style contract. A quiet plaza, horror corridor, racing street, and fighting-game arena require different environment density, cameras, lighting, and animation.

Named-game grounding transfers general rendering, environment density, and camera behavior only. Do not copy protected characters, faces, costumes, HUDs, logos, exact levels, signature props, moves, or shot compositions.

## Required workflow

```text
IDEA -> ACTIVE BUILD -> SCREENSHOT SEARCH -> VISUAL INSPECTION
-> REFERENCE ROLES -> RENDERING CONTRACT -> FIRST / GENESIS FRAME
-> IDENTITY + FIDELITY GATE -> USER APPROVAL -> NEXT OUTPUT
```

Keep the approved identity, geometry budget, texture density, material/lighting model, effects density, draw distance, camera grammar, and capture characteristics in every connected panel and animation prompt.

## Identity + fidelity gate

One major identity failure fails:

- wrong body silhouette, proportions, grain direction, face, limbs, feet, or club construction
- generic log/tree/plank character or unrelated mascot
- anatomy contamination from a human, game character, or secondary subject
- fused/duplicated prop or unrequested duplicate TripleT

Two or more era-fidelity failures fail:

- materials, wood, cloth, or equipment look substantially newer than the target
- geometry or environment density exceeds the inspected build
- debris, particles, crowds, vegetation, or effects exceed reference density
- unsupported volumetrics, global illumination, bokeh, or depth of field appear
- camera reads as modern concept art or photography instead of gameplay/in-engine footage
- noise, scanlines, or grading merely cover modern assets
- the result belongs to a different console generation

On failure:

1. do not present the frame as an approval candidate
2. lock all correct identity, action, composition, geography, and scene layers
3. apply one automatic narrow repair when isolated
4. regenerate from scratch when identity and rendering construction both fail
5. run the gate again
6. if the second attempt fails, state the limitation briefly and ask whether to try another grounded generation


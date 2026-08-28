# Continuity and Repair

## Scene-state ledger

Maintain this internally after every approved frame or storyboard:

```text
TRIPLET: body | face | grain | limbs | feet | expression | pose | condition
CLUB: present/absent | owner | position | orientation | condition
WARDROBE: garments | accessories
SECONDARIES: identity block | wardrobe | position | condition
WORLD: location | time | weather | light | damage | persistent marks
PROPS: owner | position | orientation | condition
GEOGRAPHY: screen direction | entrances/exits | camera side | landmarks
ACTION: completed | current | unresolved | next plausible beat
STYLE: target build | geometry | textures | materials | light | effects | camera | aspect
GROUNDING: screenshot set | reference roles | rendering contract | gate result
AUTHORITY: identity reference | latest approved image | approved shot/board
```

The latest approved state controls current wardrobe, props, scene, and action. The bundled turnaround continues to control TripleT's underlying identity.

## Shot construction

- give every shot one clear job
- vary wide, low/high angle, lateral action, insert/detail, close reaction, and consequence when useful
- avoid repeated medium three-quarter compositions
- maintain eyelines, screen direction, object ownership, relative positions, and action phase
- show causal transitions; do not teleport subjects or reset moved/damaged props
- keep motion readable; dynamic does not mean chaotic
- preserve the same PS2 construction across the entire sequence

## Approval locks

First-frame approval locks identity, wardrobe, club state, environment, reference set, rendering contract, geography, and current action.

Storyboard approval locks shot order and end-state. No panel may become sharper, denser, glossier, more cinematic, or more modern than the active build.

Animation must use the approved frame/storyboard as authority. Do not redesign characters, modernize materials, invent new props, add unrequested dialogue/text/music, or change the story during motion.

## Multi-character rules

- assign one identity block and reference role per character
- state left/right/foreground/background positions when geography matters
- describe contact points explicitly during interaction
- keep TripleT's wood, facial traits, proportions, and club isolated from other characters
- avoid merged bodies, shared eyes, duplicated props, or multiple TripleTs unless requested

## Narrow repair

Classify the smallest failed layer:

1. identity
2. anatomy/count
3. club ownership/count
4. continuity/state
5. geography/orientation
6. action readability
7. PS2 fidelity
8. camera variety
9. atmosphere/decorative detail

Repair the earliest failed layer first. Preserve approved layers in an explicit LOCK / CHANGE ONLY / DO NOT CHANGE block. Replace one failed panel instead of rebuilding the entire sequence whenever practical.


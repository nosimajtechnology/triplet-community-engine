# Model-Independent Prompt Adapters

## Core stack

```text
TRIPLET CANON
+ APPROVED SCENE STATE
+ MODE
+ SCREENSHOT-DERIVED PS2 RENDERING CONTRACT
+ SHOT OR MOTION LOGIC
= MODEL-NEUTRAL BRIEF
-> PROVIDER ADAPTER
```

Provider names must not alter canon, story, or continuity. Change only syntax, length, reference assignment, and verified controls.

Avoid generic language such as `cinematic lighting`, `volumetric`, `ultra-detailed`, `photoreal materials`, bokeh, or modern depth of field unless the inspected build supports it.

## Image generation

Include:

1. identity-reference assignment
2. protected construction and current expression
3. club presence/absence and ownership
4. wardrobe, action, and scene state
5. environment and composition
6. screenshot-derived rendering observations
7. lighting, camera, aspect ratio, and decisive exclusions

Assign each reference one role. Do not tell a model to blend all references.

## Image to video

Include:

1. approved start frame or storyboard as visual authority
2. duration and shot structure
3. one continuous action progression
4. character/object motion and contact points
5. camera movement per shot
6. continuity locks and final state
7. target PS2 motion/rendering behavior
8. decisive negatives: no redesign, duplicates, extra limbs, fused club, unrequested text/dialogue/music, or state resets

Keep appearance descriptions concise when the approved image already carries identity. Spend prompt budget on motion, geography, and continuity.

## Seedance

Use chronological shot beats with explicit transitions and a decisive endpoint. Keep camera movement dynamic but readable. Verify the current interface before naming exact duration, aspect, audio, or reference-slot controls.

## Kling

Favor a clear start image, action verb, subject motion, environment response, camera motion, and endpoint. Maintain explicit screen direction for multi-shot prompts. Verify current controls rather than assuming feature parity.

## Sora

Describe one coherent world-state and temporal progression. Use shot language only when the selected interface benefits from it. Verify current access, duration, reference, audio, and storyboard capabilities.

## Generic adapter

```text
INPUT: approved image/storyboard
DURATION: user requirement or flexible
ACTION: chronological motion beats
CAMERA: readable motivated movement
CONTINUITY: protected state and endpoint
STYLE: screenshot-derived PS2 behavior
NEGATIVES: only decisive failure prevention
```

Mark unsupported specifics `unverified or variable`.

## Prompt-length compression

When the user sets an exact limit, measure after final edits. Preserve in this order:

1. identity and anatomy
2. approved state and action progression
3. contact points and continuity
4. PS2 rendering contract
5. motion and camera
6. decisive negatives
7. atmosphere

Remove repetition and ornamental adjectives first. Report the exact final character count.

## Delivery format

```text
SETUP: [one line]
REFERENCES: [role for each input]
PROMPT: [copy-paste prompt]
FIELDS: [only verified interface settings]
CHARACTER COUNT: [when requested]
```


# Modes and Workflows

## Routing

| User intent | Mode |
| --- | --- |
| one picture, poster, cover, loading screen, fake screenshot | IMAGE |
| one quick motion beat, approximately 4-8 seconds | MINI |
| one contained story moment, approximately 8-15 seconds | SCENE |
| loop, ident, sting, transition, approximately 4-10 seconds | BUMPER |
| fictional product, service, PSA, or promo, approximately 8-15 seconds | FAKE AD |

Mode controls scope, not tone. Every mode can be deadpan, absurd, eerie, sincere, or energetic.

## Grounded prefix

Before generating any mode, resolve the active build. Unless the user explicitly requests a non-game style, follow [rendering-grounding.md](rendering-grounding.md) through screenshot inspection, role assignment, rendering contract, and the identity + fidelity gate. Do not show or expand a frame that fails.

## IMAGE

```text
IDEA -> PS2 BUILD -> GROUNDING -> ONE IMAGE -> GATE -> REPAIR OR VARIATION
```

Create one strong image. Do not add a storyboard or video prompt unless requested. If the user later says `animate this`, promote the approved image to project authority.

## MINI

```text
IDEA -> GROUNDING -> FIRST FRAME -> GATE -> APPROVAL
-> ONE MOTION BEAT -> VIDEO PROMPT
```

Use one action, one camera idea, and one decisive endpoint. Do not inflate a tiny gag into multiple unrelated shots.

## SCENE

```text
IDEA -> GROUNDING -> GENESIS FRAME -> GATE -> APPROVAL
-> 4-6 CONNECTED SHOTS OR ONE-TAKE BRIEF -> APPROVAL WHEN NEEDED
-> VIDEO PROMPT
```

Give every shot one job: hook, reveal, action, reaction, escalation, or payoff. Vary scale and perspective without breaking geography.

## BUMPER

```text
VISUAL HOOK -> SIMPLE ACTION -> IDENT / LOOP CLOSURE
```

Favor one iconic action and a clean final state. If exact typography matters, provide the copy separately or preserve clean end-card space.

## FAKE AD

```text
HOOK -> NEED -> FICTIONAL SOLUTION -> DEMONSTRATION -> PAYOFF / END CARD
```

Treat the impossible product or service seriously. Keep the offer readable. Use separate voiceover when exact wording matters; do not depend on generated typography or speech unless the user chooses that route.

## Output discipline

- generate when tooling is available and the user requested a visual
- return prompt-only output when requested or generation is unavailable
- never claim video was rendered when only a prompt was produced
- preserve the approved rendering contract in every later stage
- count the final prompt after editing when an exact limit applies


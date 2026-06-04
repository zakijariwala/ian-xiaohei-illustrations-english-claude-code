# QA Checklist

## Must Pass

- Is 16:9 horizontal format.
- Background is clean white.
- The active character is present.
- The character performs the core action — not just decoration.
- Did not recreate an old example composition — invented a new metaphor for this article.
- Image feels absurd, creative, and interesting.
- Clean and spacious — main subject doesn't exceed ~60% of canvas.
- One image explains only one core structure.
- Annotations are few, short, and legible.
- Orange used only for main paths or arrows.
- Red used only for key points, problems, alerts, or results.
- Blue used only for supplementary notes, feedback, or system state.

## Failure Signals

If any of the following appear, regenerate or locally edit:

- Top-left corner has a title like "Common Pitfalls / Workflow / System Architecture / Roadmap."
- The character looks like a mascot, emoji character, or cute cartoon.
- Image looks like a PPT, course slide, or formal flowchart.
- Too many elements, too many arrows, too many nodes.
- Text turned into long explanatory paragraphs.
- Background has paper texture, shadow, gradient, cream color, or noise.
- Real UI screenshot or tech-look interface.
- Annotations have serious typos or are illegible.
- Image is too stiff — no absurd metaphor.
- Composition is too similar to something in `assets/examples/`.

## Iteration Methods

- Too generic: Make the character the action subject; add one strange-but-coherent metaphor.
- Too complex: Cut nodes — keep only one action and 3–5 short labels.
- Too cute: Emphasize deadpan, blank serious expression, not cute, not mascot.
- Too PPT: Remove titles, borders, neat grids, and excess arrows; turn it into a hand-drawn scene.
- Too similar to an old example: Keep the core meaning; swap out the main object and Xiaohei's action.
- Text errors: Try local edit first; if errors are many, regenerate with fewer annotations.

## Delivery Judgment

A high-quality image should make the reader think "that's a bit strange" first, then understand the structure within one second.

If the first impression is "tutorial page" rather than "a weird product sketch on a blank piece of paper," it doesn't pass.

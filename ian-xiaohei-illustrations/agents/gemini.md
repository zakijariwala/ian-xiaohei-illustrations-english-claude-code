---
name: ian-xiaohei-illustrations
description: Generate Ian-style hand-drawn body illustrations for articles. Invoke when the user wants article illustrations, shot lists, image suggestions, or visual metaphors for articles, posts, blogs, Notion docs, workflow docs, methodology content, processes, structures, states, or concepts. Default style: Xiaohei IP, pure white hand-drawn, sparse red/orange/blue annotations, clean but wildly creative.
tools:
  - image_generation
---

# Ian Xiaohei Illustrations — Gemini CLI

## Core Purpose

Design and generate 16:9 horizontal body illustrations for articles using the Xiaohei (小黑) IP. Not commercial illustration, not PPT infographics — hand-drawn, absurd, clean explanatory images that turn key article judgments into memorable visuals.

## Reference Files

Load these as needed (don't load all at once):

- `references/style-dna.md` — Visual rules, colors, prohibitions
- `references/xiaohei-ip.md` — Xiaohei character definition and action library
- `references/composition-patterns.md` — Structure types and metaphor generation
- `references/prompt-template.md` — Image generation prompt template
- `references/qa-checklist.md` — Post-generation checklist

## Workflow

1. Read and digest the article content
2. If asked for planning only: output a shot list (4–8 images, one per cognitive anchor)
3. If asked to generate: call the image generation tool for each image separately
4. Check QA checklist after each generation
5. Save final images to `assets/<article-slug>-illustrations/`

Each image: 16:9, pure white background, black hand-drawn line art, Xiaohei as core action subject, sparse annotations, lots of blank space. One structure per image. Never copy old example compositions.

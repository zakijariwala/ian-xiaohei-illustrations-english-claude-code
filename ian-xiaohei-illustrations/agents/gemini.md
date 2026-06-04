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
- `references/characters/INDEX.md` — All 9 IP characters with IDs and cultures
- `references/characters/<id>.md` — The active character's descriptors and prompt-injection block
- `references/composition-patterns.md` — Structure types and metaphor generation
- `references/prompt-template.md` — Image generation prompt template
- `references/qa-checklist.md` — Post-generation checklist

## Workflow

1. **Pick a character.** Read `settings.json` for `default_character` (fallback `xiaohei`). If the user names a character, alias, or culture, that overrides for this session. Load its `references/characters/<id>.md`.
2. **No article provided?** Run `python3 scripts/scan_project.py` to discover article candidates in the working directory, then suggest which to illustrate.
3. Read and digest the chosen article content.
4. If asked for planning only: output a shot list (4–8 images, one per cognitive anchor).
5. If asked to generate: render each image separately. Use a native image tool if present; otherwise run the bundled binding `python3 scripts/generate_image.py --character <id> --prompt-file prompt.txt --out <path>` (auto-detects Nano Banana / DALL·E / Imagen / Stability from the API key env vars — see `scripts/README.md`).
6. Check QA checklist after each generation.
7. Save final images to `assets/<article-slug>-illustrations/`.

Each image: 16:9, pure white background, black hand-drawn line art, the active character as core action subject, sparse English annotations, lots of blank space. One structure per image. Never copy old example compositions.

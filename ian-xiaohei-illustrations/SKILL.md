---
name: ian-xiaohei-illustrations
description: Generate Ian-style hand-drawn body illustrations for articles. Use when the user wants to create article illustrations, shot lists, image suggestions, or visual metaphors for articles, posts, blogs, Notion docs, workflow docs, methodology content, processes, structures, states, or concepts. Default style: Xiaohei IP, pure white hand-drawn, sparse red/orange/blue annotations, clean but wildly creative.
---

# Ian Xiaohei Illustrations

## Core Purpose

Design and generate 16:9 horizontal body illustrations for articles. The goal is not commercial illustration, PPT infographics, or cute cartoons — it's taking the key judgments, flows, structures, states, or metaphors inside an article and turning them into clean, absurd, creative, readable-but-not-instructional hand-drawn explanatory images.

The default visual IP is "Xiaohei" (小黑): a solid black creature with white dot eyes, thin legs, and a blank expression, seriously performing something absurd but coherent. Xiaohei must participate in the core action of the scene — never just stand in the corner as decoration.

## Read These References First

Load only what the task requires — don't fill the context with everything at once:

- `references/style-dna.md`: Visual DNA, colors, typography, and prohibitions.
- `references/characters/INDEX.md`: All available IP characters with IDs and cultures.
- `references/characters/<id>.md`: The active character's descriptors and prompt injection block.
- `references/composition-patterns.md`: Structure types, original metaphor method, and anti-reuse rules.
- `references/prompt-template.md`: Single-image generation prompt template.
- `references/qa-checklist.md`: Post-generation checklist and iteration rules.
- `assets/examples/`: Use only for low-frequency visual calibration — not in the default generation path. Never copy these examples' compositions, objects, or labels.

## Workflow

### 0. Select a Character

Default character is **Xiaohei**. If the user specifies a different character, load its file from `references/characters/<id>.md` and use the `Prompt Injection` block in every image prompt instead of the default Xiaohei block.

Available characters (see `references/characters/INDEX.md` for full list):

| ID | Culture |
|----|---------|
| `xiaohei` | Chinese / East Asian (default) |
| `chibi-kage` | Japanese |
| `kaala` | South / Southeast Asian |
| `kali-tikka` | Indian (street / vernacular) |
| `le-bloc` | European |
| `the-smudge` | American |
| `dudu` | West African / Afrofuturist |
| `el-manchon` | Latin American |
| `al-zill` | Middle Eastern / Arabic |

The user can request a character by name, alias, or culture: "use the American character", "use Dudu", "use `le-bloc`", etc. All characters follow the same IP contract: deadpan, structurally essential, hand-drawn, absurd worker.

Via the generation script: `python3 scripts/generate_image.py --character the-smudge ...`

### 1. Digest the Article

First read the article, link, Notion page, Markdown file, or screenshot content the user provides. Extract:

- What is the core argument
- Which paragraphs carry cognitive turning points
- Which content benefits from visual explanation
- Which parts should stay text-only

Don't distribute illustrations evenly. Prioritize "cognitive anchors": core judgments, two breakpoints, input-output loops, decision forks, before-after contrasts, one-to-many reuse, handoff paths, common pitfalls, character state changes.

### 2. Produce a Shot List First

If the user only says "analyze how to illustrate this / think about where illustrations would help," give a shot list first. For each image write:

- Which paragraph it follows
- The image's theme
- Core meaning
- Structure type
- What Xiaohei is doing in the image
- Suggested elements
- Suggested annotation words

Default 4–8 images. Very short articles: 1–3. Long articles: don't go beyond 9 unless essential. Enough is enough — avoid turning the article into a picture book.

### 3. Single Image Generation

If the user explicitly says "generate / create / make the image / go ahead," don't stop to confirm. Generate each image separately — never combine multiple images into one.

**How to generate.** Build the prompt from `references/prompt-template.md`, then render it with whatever image model is available:

1. **Built-in image tool** — if the host agent exposes a native image-generation tool (e.g. Claude Code/Codex `image_gen`), call it directly with the prompt.
2. **Bundled bindings** — otherwise use the bundled script, which auto-detects an available provider (Nano Banana / Gemini, DALL·E / OpenAI, Imagen, Stability):

   ```bash
   python3 scripts/generate_image.py --prompt-file prompt.txt --out assets/<slug>-illustrations/01-topic.png
   # force a provider:
   python3 scripts/generate_image.py --provider nanobanana --prompt-file prompt.txt --out 01-topic.png
   # check which providers have a key set:
   python3 scripts/generate_image.py --list-providers
   ```

   The script reads the API key from the environment (`GEMINI_API_KEY`/`GOOGLE_API_KEY` for Nano Banana & Imagen, `OPENAI_API_KEY` for DALL·E, `STABILITY_API_KEY` for Stability). See `scripts/README.md` for setup.

If no built-in tool and no provider key are available, output the finished prompt and tell the user which env var to set — don't claim an image was produced.

Each image explains only one core structure. Prompts must include:

- 16:9 horizontal article illustration
- Pure white background
- Black hand-drawn line art
- Sparse red/orange/blue handwritten annotations (English by default)
- Lots of blank space
- Xiaohei as the core action subject
- No PPT, no commercial illustration, no cute cartoon, no complex architecture diagrams, no top-left title

Never recreate past examples. Examples only calibrate visual density and Xiaohei's level of involvement — never directly reuse compositions like "conveyor belt breakpoints / Xiaohei pulling levers / fish materials / stamp toolbox / common pitfall path." Every image must invent a fresh, strange-but-coherent metaphor from the current article.

### 4. Check and Iterate

After generating, check `references/qa-checklist.md`. If any of these issues appear, prioritize regenerating or locally editing:

- Xiaohei is only decoration
- Image is too crowded
- Looks like a flowchart or PPT
- Too much Chinese text or serious typos
- Top-left corner shows a title like "Common Pitfalls / Workflow / System Architecture"
- Art style is too cute, childish, or stiff
- Background is not clean white

### 5. Save and Deliver

If the user is working within a workspace, copy final images to:

```text
assets/<article-slug>-illustrations/
```

Name them in order:

```text
01-topic-name.png
02-topic-name.png
```

Keep original generated files — do not overwrite existing assets unless the user explicitly asks for replacement.

## Output Standards

Pre-generation strategy output should be short and precise. Post-generation delivery must include:

- How many images were generated
- Each image's purpose
- Save path
- Which images are most solid, which are optional

Don't explain style theory at length — let the images speak for themselves.

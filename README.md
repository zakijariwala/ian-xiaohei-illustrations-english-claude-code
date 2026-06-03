# Ian Xiaohei Illustrations

> Turn the judgments, flows, states, and metaphors inside an article into clean 16:9 hand-drawn body illustrations.
>
> 16:9 horizontal · Xiaohei IP · Pure white hand-drawn · Sparse red/orange/blue annotations · Multi-platform skill

---

## What This Is

Ian Xiaohei Illustrations is a multi-platform AI agent skill for generating hand-drawn body illustrations for articles, posts, blogs, Notion docs, and methodology content.

It is not a general illustration prompt, and not a PPT infographic template. Its core goal is to first understand the cognitive anchors in an article, then turn one judgment, flow, structure, state, or metaphor into a memorable 16:9 hand-drawn explanatory image.

The default visual IP is "Xiaohei" (小黑): a solid black creature with white dot eyes, thin legs, and a blank expression. Xiaohei is not a mascot, not a sticker, not a decoration — Xiaohei is seriously participating in how the system operates, doing something slightly absurd but coherent.

**In one line: make AI not just "add an image," but draw out one key cognitive action from the article.**

---

## Who It's For

Best fit:
- Writers who need body illustrations and article images for their content
- People producing knowledge content, methodology content, or AI workflow content
- Anyone who wants to turn abstract judgments into concrete visual metaphors
- People who want a style lighter, stranger, and more recognizable than PPT infographics
- Anyone using an AI agent CLI who wants a stable, reusable visual language

Not a fit:
- People who want commercial illustration, brand KV, or polished flat design
- People who want traditional PPT infographics, complex architecture diagrams, or formal flowcharts
- People who want children's cartoons, cute IP, or meme-style images
- People who want to pack long text passages or full course pages into one image
- People who need strictly editable vector source files

---

## What It Produces

Default output:
- 16:9 horizontal body illustrations
- A shot list of 4–8 images for an article
- Per-image: theme, core meaning, structure type, Xiaohei's action, suggested annotations
- Final PNG files saved to `assets/<article-slug>-illustrations/`

Not produced by default:
- PPTX / PDF / Keynote
- SVG / HTML / Canvas editable files
- Commercial poster or cover KV
- Dense text infographics

---

## Visual Style

- Pure white background — no paper texture, cream, shadows, gradients
- Black hand-drawn line art, thin lines, slight wobble
- Lots of blank space — main subject ~40%–60% of canvas
- Sparse red/orange/blue handwritten annotations
- One image = one core action, structure, state, or metaphor
- Xiaohei must perform the core action — not just decoration
- Absurd, creative, clean — not childish, not cute

---

## Supported Platforms

| Platform | Entry File | Install Path |
|----------|-----------|--------------|
| **Claude Code** | `SKILL.md` | `~/.claude/skills/ian-xiaohei-illustrations/` |
| **OpenAI Codex** | `agents/openai.yaml` | `~/.codex/skills/ian-xiaohei-illustrations/` |
| **Gemini CLI** | `agents/gemini.md` | `~/.gemini/skills/ian-xiaohei-illustrations/` |
| **Hermes** | `agents/hermes.yaml` | — |
| **Antigravity** | `agents/antigravity.yaml` | — |

---

## Installation

Clone the repo:

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations-english.git
cd ian-xiaohei-illustrations-english
```

### Auto-detect and install

```bash
chmod +x ian-xiaohei-illustrations/install.sh
./ian-xiaohei-illustrations/install.sh
```

The script detects your active AI CLI (`claude`, `codex`, or `gemini`) and installs to the right directory.

### Manual install

**Claude Code:**

```bash
mkdir -p ~/.claude/skills
cp -R ./ian-xiaohei-illustrations ~/.claude/skills/
```

**OpenAI Codex:**

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./ian-xiaohei-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Gemini CLI:**

```bash
mkdir -p ~/.gemini/skills
cp -R ./ian-xiaohei-illustrations ~/.gemini/skills/
```

---

## Usage

### Claude Code

```text
/ian-xiaohei-illustrations Generate 5 Xiaohei illustrations for this article.

<paste article>
```

### OpenAI Codex

```text
Use $ian-xiaohei-illustrations to design and generate 5 Xiaohei hand-drawn illustrations for this article.

<paste article>
```

### Gemini CLI

```text
@ian-xiaohei-illustrations Generate illustrations for this article.

<paste article>
```

---

## Common Tasks

### Planning only — no generation

```text
Use the ian-xiaohei-illustrations skill. Don't generate images yet.
Analyze this article and produce a shot list of ~5 illustrations.
For each: which paragraph it follows, theme, core meaning, structure type, what Xiaohei is doing, suggested annotation words.

<paste article>
```

### Generate body illustrations directly

```text
Use the ian-xiaohei-illustrations skill to generate 4 Xiaohei hand-drawn illustrations for this article.
Requirements: 16:9 horizontal, pure white background, black hand-drawn line art, sparse red/orange/blue annotations.

<paste article>
```

### Generate one image for a concept

```text
Use the ian-xiaohei-illustrations skill to generate one illustration for the idea:
"Trust isn't declared — it's laid brick by brick, one piece of evidence at a time."
The image should be absurd but clean, and Xiaohei must carry the core action.
```

### Remove a title or wrong text from an image

```text
Use the ian-xiaohei-illustrations skill to edit this image.
Remove the "Flowchart" title from the top-left corner. Keep everything else exactly as-is.
```

More examples: [examples/prompts.md](examples/prompts.md)

---

## Workflow

1. Read the article, Markdown, Notion content, screenshot, or user-provided theme
2. Extract core arguments, cognitive turning points, flows, and visually explainable paragraphs
3. Output shot list: one cognitive anchor per image
4. Choose a structure type: Workflow, System Slice, Before-After Contrast, Character State, Conceptual Metaphor, Method Layers, Map Route, or Mini Comic Panels
5. Invent a low-tech, absurd-but-coherent physical metaphor
6. Let Xiaohei carry the core action
7. Generate each image separately via the image generation tool
8. Run QA checklist: white background, blank space, Xiaohei's action, annotations, non-PPT feel, no old-example recreation
9. Save final PNGs and report purpose and path

---

## Directory Structure

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── assets/
│   └── ian-wechat-qr.jpg
├── examples/
│   ├── images/
│   │   ├── 01-two-breakpoints.png
│   │   ├── 02-sort-by-purpose.png
│   │   └── ...
│   └── prompts.md
└── ian-xiaohei-illustrations/        ← install this directory
    ├── SKILL.md                       ← Claude Code entry point
    ├── manifest.json                  ← Universal plugin manifest
    ├── install.sh                     ← Auto-installer
    ├── agents/
    │   ├── openai.yaml                ← OpenAI Codex
    │   ├── gemini.md                  ← Gemini CLI
    │   ├── hermes.yaml                ← Hermes agents
    │   └── antigravity.yaml           ← Antigravity agents
    ├── assets/
    │   └── examples/
    └── references/
        ├── style-dna.md
        ├── xiaohei-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        └── qa-checklist.md
```

Only the subdirectory needs to be installed:

```text
ian-xiaohei-illustrations/
```

The root README, LICENSE, NOTICE, and examples are GitHub sharing docs.

---

## Notes

- Fewer Chinese characters in images = more stable output.
- One image = one core structure. Don't turn the article into a manual.
- Xiaohei must carry the core action. If the metaphor holds without Xiaohei, Xiaohei is too decorative.
- Example images are only for calibrating line density, blank space, color restraint, and Xiaohei's energy — never copy compositions.
- AI image models may produce typos, hallucinated labels, style drift, or extra titles — check every output.
- If Chinese characters are badly wrong, reduce annotation count and regenerate.

---

## Related Projects

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — Chinese hand-drawn tech PPT-style page generation skill
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — Curated collection of Claude Code skills, agents, and plugins
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — Obsidian + Claude AI personal knowledge base guide

---

## About the Author

**Ian (伊恩)** — Product designer / Solo founder / AI Builder

Building a one-person company with an AI team.

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- Website: [www.ianneo.xyz](https://www.ianneo.xyz)

---

## License

MIT License. See [LICENSE](LICENSE).

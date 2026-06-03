# Ian Xiaohei Illustrations

> Turn the judgments, flows, states, and metaphors inside an article into clean, absurd 16:9 hand-drawn body illustrations.
>
> 16:9 horizontal · Xiaohei IP · Pure white hand-drawn · Sparse English annotations · Multi-platform skill

---

## What This Is

**Ian Xiaohei Illustrations** is a multi-platform AI agent skill for generating hand-drawn body illustrations for articles, posts, blogs, Notion docs, and methodology content.

Not a general illustration prompt, not a PPT infographic template. Its job is to first understand the cognitive anchors in an article, then turn one judgment, flow, structure, state, or metaphor into a memorable 16:9 hand-drawn image.

The default visual IP is **Xiaohei** (小黑): a solid black creature with white dot eyes, thin legs, and a blank expression. Xiaohei is not a mascot — Xiaohei is seriously performing something absurd but coherent, as the core actor in every image.

**In one line:** make AI not just "add an image," but draw out a key cognitive action from the article.

---

## Supported Platforms

| Platform | Entry Point | Status |
|----------|------------|--------|
| [Claude Code](#claude-code) | `SKILL.md` | ✅ Full skill with `/ian-xiaohei-illustrations` |
| [OpenAI Codex](#openai-codex) | `agents/openai.yaml` | ✅ `$ian-xiaohei-illustrations` |
| [Gemini CLI](#gemini-cli) | `agents/gemini.md` | ✅ `@ian-xiaohei-illustrations` |
| [Hermes](#hermes-agents) | `agents/hermes.yaml` | ✅ Trigger phrases |
| [Antigravity](#antigravity) | `agents/antigravity.yaml` | ✅ Skill config |

---

## Characters

Nine cultural IP characters are available. Default is **Xiaohei**. Swap via a natural-language request or the `--character` flag.

| ID | Character | Culture |
|----|-----------|---------|
| `xiaohei` | Xiaohei (小黑) | Chinese / East Asian |
| `chibi-kage` | Chibi Kage (小影) | Japanese |
| `kaala` | Kaala (काला) | South / Southeast Asian |
| `kali-tikka` | Kali Tikka | Indian (street / vernacular) |
| `le-bloc` | Le Bloc / Der Fleck | European |
| `the-smudge` | The Smudge | American |
| `dudu` | Dudu | West African / Afrofuturist |
| `el-manchon` | El Manchón | Latin American |
| `al-zill` | Al-Zill (الظل) | Middle Eastern / Arabic |

All characters share the same IP contract: **deadpan, structurally essential, hand-drawn, absurd worker**. Each brings a different cultural line tradition, body morphology, and personality flavor.

```bash
# List all characters
python3 ian-xiaohei-illustrations/scripts/generate_image.py --list-characters

# Generate with a specific character
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character the-smudge \
  --prompt-file prompt.txt \
  --out 01-topic.png
```

Full character descriptors: [ian-xiaohei-illustrations/references/characters/](ian-xiaohei-illustrations/references/characters/)

---

## Generating Images

**[Full guide → docs/GENERATE.md](docs/GENERATE.md)**

Three ways:

| Method | Cost | Setup |
|--------|------|-------|
| **Script + Nano Banana / Imagen** | Free tier | `GEMINI_API_KEY` from [aistudio.google.com](https://aistudio.google.com) |
| **Script + DALL·E** | Paid | `OPENAI_API_KEY` from [platform.openai.com](https://platform.openai.com/api-keys) |
| **Script + Stability** | Trial credits | `STABILITY_API_KEY` from [platform.stability.ai](https://platform.stability.ai) |
| **Claude Code native** | Claude Pro/Max subscription | Install Claude Code + skill |
| **Web UI (free, no API)** | Free | Paste prompt into Claude.ai, Google AI Studio, Bing, Firefly, or Ideogram |

Quickest start — Nano Banana free tier:
```bash
export GEMINI_API_KEY="your-key-from-aistudio.google.com"
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider nanobanana --character xiaohei \
  --prompt-file examples/prompts/01-xiaohei-content-press.txt \
  --out examples/output/01-xiaohei-content-press.png
```

---

## Quick Install

```bash
git clone https://github.com/zakijariwala/ian-xiaohei-illustrations-english-claude-code.git
cd ian-xiaohei-illustrations-english-claude-code

# Auto-detects your agent CLI (claude / codex / gemini)
chmod +x ian-xiaohei-illustrations/install.sh
./ian-xiaohei-illustrations/install.sh

# Or force a platform
./ian-xiaohei-illustrations/install.sh claude
./ian-xiaohei-illustrations/install.sh codex
./ian-xiaohei-illustrations/install.sh gemini
```

For per-agent step-by-step instructions → **[docs/SETUP.md](docs/SETUP.md)**

---

## Usage

### Claude Code

```text
/ian-xiaohei-illustrations Generate 5 Xiaohei illustrations for this article.

<paste article>
```

### OpenAI Codex

```text
Use $ian-xiaohei-illustrations to generate 5 Xiaohei hand-drawn illustrations for this article.

<paste article>
```

### Gemini CLI

```text
@ian-xiaohei-illustrations Generate illustrations for this article.

<paste article>
```

---

## Common Tasks

**Plan only (no generation):**
```text
Use ian-xiaohei-illustrations. Don't generate images yet.
Analyze this article and produce a shot list of ~5 illustrations.
For each: paragraph placement, theme, core meaning, structure type,
what Xiaohei is doing, suggested annotation words.

<paste article>
```

**Generate illustrations directly:**
```text
Use ian-xiaohei-illustrations to generate 4 Xiaohei hand-drawn illustrations for this article.
16:9, pure white, black hand-drawn line art, sparse English annotations.

<paste article>
```

**Generate one image for a single concept:**
```text
Use ian-xiaohei-illustrations to generate one illustration for:
"Trust isn't declared — it's laid brick by brick, one piece of evidence at a time."
Absurd but clean. Xiaohei must carry the core action.
```

**Remove a wrong title from an image:**
```text
Use ian-xiaohei-illustrations to edit this image.
Remove the "Flowchart" title from the top-left corner. Keep everything else exactly as-is.
```

More examples: [examples/prompts.md](examples/prompts.md)

---

## What It Produces

✅ Default output:
- 16:9 horizontal body illustrations
- Shot list of 4–8 images per article
- Per-image: theme, core meaning, structure type, Xiaohei's action, annotation words
- Final PNG files saved to `assets/<article-slug>-illustrations/`

❌ Not produced:
- PPTX / PDF / Keynote
- SVG / HTML / Canvas editable files
- Commercial poster or cover artwork
- Dense text infographics

---

## Visual Style

- **Background:** Pure white — no paper texture, cream, shadows, or gradients
- **Line art:** Black hand-drawn, thin lines, slight wobble
- **Space:** Lots of blank space — main subject ~40%–60% of canvas
- **Annotations:** Sparse, English by default, 1–4 words each
- **Colors:** Black (main) · Orange (flow/arrows) · Red (warnings/results) · Blue (secondary notes)
- **Xiaohei:** Must perform the core action — remove him and the metaphor should collapse
- **Aesthetic:** Absurd, creative, clean — not childish, not cute, not stiff

---

## Directory Structure

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── docs/
│   └── SETUP.md                       ← Per-agent step-by-step setup guides
├── assets/
│   └── ian-wechat-qr.jpg
├── examples/
│   ├── images/
│   └── prompts.md
└── ian-xiaohei-illustrations/         ← The skill — install this directory
    ├── SKILL.md                        ← Claude Code entry point
    ├── manifest.json                   ← Universal plugin manifest
    ├── install.sh                      ← Auto-installer
    ├── agents/
    │   ├── openai.yaml                 ← OpenAI Codex config
    │   ├── gemini.md                   ← Gemini CLI config
    │   ├── hermes.yaml                 ← Hermes agent config
    │   └── antigravity.yaml            ← Antigravity agent config
    ├── scripts/
    │   ├── generate_image.py           ← Image bindings (Nano Banana/DALL·E/Imagen/Stability)
    │   └── README.md                   ← Provider + character setup reference
    ├── assets/
    │   └── examples/                   ← Visual calibration only — never copy compositions
    └── references/
        ├── style-dna.md
        ├── xiaohei-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        ├── qa-checklist.md
        └── characters/
            ├── INDEX.md                ← All character IDs, cultures, aliases
            ├── xiaohei.md
            ├── chibi-kage.md
            ├── kaala.md
            ├── kali-tikka.md
            ├── le-bloc.md
            ├── the-smudge.md
            ├── dudu.md
            ├── el-manchon.md
            └── al-zill.md
```

---

## Notes

- Fewer words in annotations = more stable image output.
- One image = one core structure. Don't turn the article into a manual.
- If removing Xiaohei leaves the metaphor fully intact, Xiaohei is too decorative — regenerate.
- Example images calibrate line density, blank space, and Xiaohei's energy — never copy their compositions.
- AI image models may produce typos, hallucinated labels, or style drift — check every output.
- Annotations default to English. To use the original Chinese look, see the note in `references/prompt-template.md`.

---

## Related Projects

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — Hand-drawn tech PPT-style page generation skill
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — Curated Claude Code skills, agents, and plugins
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — Personal knowledge base with Obsidian + Claude AI

---

## About the Author

**Ian (伊恩)** — Product designer / solo founder / AI builder

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- Website: [www.ianneo.xyz](https://www.ianneo.xyz)

---

## License

MIT License. See [LICENSE](LICENSE).

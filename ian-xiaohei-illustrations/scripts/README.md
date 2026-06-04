# Scripts

Two bundled scripts: `generate_image.py` for rendering illustrations, and `scan_project.py` for discovering article content in a directory.

---

## scan_project.py — Project Scanner

Scans the current directory (or a given path) for article content — Markdown, text, RST — and outputs illustration suggestions: ranked files, headings, and cognitive anchor candidates.

Run this when the user hasn't provided an article and you want to discover what's in the project.

```bash
# Scan current directory (human-readable)
python3 scripts/scan_project.py

# Scan a specific directory
python3 scripts/scan_project.py /path/to/project

# Scan a single file
python3 scripts/scan_project.py --file post.md

# JSON output for agent parsing
python3 scripts/scan_project.py --json

# Limit how many files to analyse (default: 10)
python3 scripts/scan_project.py --max 5
```

The scanner skips boilerplate files (README, LICENSE, CHANGELOG, etc.), hidden directories, `node_modules`, `.git`, and `__pycache__`. Files are ranked by a score combining heading count, cognitive-anchor signal density (words like "why", "problem", "before", "after", "step", "lesson"), and word count.

Output includes:
- File path and word count
- Top 4 section headings
- First cognitive anchor sentence
- Suggested next steps (how to invoke the skill or the generation script)

---

# Image Generation Bindings

`generate_image.py` renders one illustration from a text prompt using whichever
image model has an API key set in the environment.

Pure Python 3 (stdlib only). The `stability` provider optionally uses `requests`.

For full setup instructions, provider keys, and per-agent guides:
→ **[docs/SETUP.md — Image Generation Setup](../../docs/SETUP.md#image-generation-setup)**

---

## Providers

| Provider | Alias(es) | Model | Env var |
|----------|-----------|-------|---------|
| Nano Banana | `nanobanana`, `gemini` | `gemini-2.5-flash-image-preview` | `GEMINI_API_KEY` or `GOOGLE_API_KEY` |
| DALL·E | `dalle`, `openai` | `gpt-image-1` (→ `dall-e-3`) | `OPENAI_API_KEY` |
| Imagen | `imagen` | `imagen-3.0-generate-002` | `GEMINI_API_KEY` or `GOOGLE_API_KEY` |
| Stability | `stability`, `sd` | Stable Image SD3 | `STABILITY_API_KEY` |

Auto-detect order (no `--provider` flag): **nanobanana → dalle → imagen → stability**

Model overrides: `NANOBANANA_MODEL`, `OPENAI_IMAGE_MODEL`, `IMAGEN_MODEL`

---

## Default Character (settings.json)

The skill ships with `settings.json` in the skill root. The `default_character` field
controls which IP is used when `--character` is not specified.

```json
// settings.json
{
  "default_character": "xiaohei",
  "_note": "Change via --set-default or edit this file directly"
}
```

**View the current default:**
```bash
python3 scripts/generate_image.py --show-default
```

**Change the default:**
```bash
python3 scripts/generate_image.py --set-default the-smudge
python3 scripts/generate_image.py --set-default al-zill
# Aliases work too
python3 scripts/generate_image.py --set-default smudge
```

Or edit `settings.json` directly — set `default_character` to any ID from
`references/characters/INDEX.md`.

The first time you run `install.sh`, it asks you to choose your default character
interactively and writes the selection to `settings.json` in the installed location.
On re-install / upgrade, the existing `settings.json` is preserved and the prompt
is skipped.

---

## Characters

Use `--character <id>` (or `-c`) to override the default for one image.

```bash
# List all available characters
python3 generate_image.py --list-characters

# Use a specific character
python3 generate_image.py --character the-smudge --prompt-file prompt.txt --out img.png
python3 generate_image.py -c al-zill --prompt-file prompt.txt --out img.png

# Aliases work too
python3 generate_image.py --character smudge ...
python3 generate_image.py --character bloc ...
python3 generate_image.py --character kage ...
```

Available IDs: `xiaohei`, `chibi-kage`, `kaala`, `kali-tikka`, `le-bloc`, `the-smudge`, `dudu`, `el-manchon`, `al-zill`

The character's `Prompt Injection` block (from `references/characters/<id>.md`) is spliced into the prompt automatically, replacing the default Xiaohei block if present.

Full details: [references/characters/INDEX.md](../references/characters/INDEX.md)

---

## Usage

```bash
# Check which providers have a key set
python3 generate_image.py --list-providers

# Auto-detect provider, prompt from a file
python3 generate_image.py --prompt-file prompt.txt --out 01-topic.png

# Force a provider, inline prompt
python3 generate_image.py --provider dalle --prompt "..." --out img.png

# Pipe prompt from stdin
cat prompt.txt | python3 generate_image.py --out img.png
```

## Quick Setup

```bash
export GEMINI_API_KEY="your-key"        # Nano Banana + Imagen
# or
export OPENAI_API_KEY="your-key"        # DALL·E
# or
export STABILITY_API_KEY="your-key"     # Stability (also: pip install requests)

python3 generate_image.py \
  --prompt-file prompt.txt \
  --out assets/my-article-illustrations/01-topic.png
```

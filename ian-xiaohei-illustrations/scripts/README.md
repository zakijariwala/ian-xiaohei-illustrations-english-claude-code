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

## Characters

Use `--character <id>` (or `-c`) to select an IP character. Default: `xiaohei`.

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

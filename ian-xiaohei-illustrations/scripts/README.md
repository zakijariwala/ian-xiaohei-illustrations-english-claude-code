# Image Generation Bindings

`generate_image.py` renders one illustration from a text prompt using whichever
image model has an API key set. It is pure Python 3 (stdlib only; the `stability`
provider optionally uses `requests`), so it runs from any agent platform or a
plain shell.

## Providers

| Provider | Alias | Model | API key env var |
|----------|-------|-------|-----------------|
| Nano Banana | `nanobanana`, `gemini` | `gemini-2.5-flash-image-preview` | `GEMINI_API_KEY` or `GOOGLE_API_KEY` |
| DALL·E | `dalle`, `openai` | `gpt-image-1` (→ `dall-e-3`) | `OPENAI_API_KEY` |
| Imagen | `imagen` | `imagen-3.0-generate-002` | `GEMINI_API_KEY` or `GOOGLE_API_KEY` |
| Stability | `stability`, `sd` | Stable Image SD3 | `STABILITY_API_KEY` |

Model IDs can be overridden via `NANOBANANA_MODEL`, `OPENAI_IMAGE_MODEL`,
`IMAGEN_MODEL`.

## Auto-detection

With no `--provider` flag, the first provider whose key is set is used, in order:
**nanobanana → dalle → imagen → stability**.

## Usage

```bash
# Auto-detect provider, prompt from a file
python3 generate_image.py --prompt-file prompt.txt --out 01-topic.png

# Force a provider, inline prompt
python3 generate_image.py --provider dalle --prompt "..." --out img.png

# Pipe the prompt in
cat prompt.txt | python3 generate_image.py --out img.png

# See which providers have a key set
python3 generate_image.py --list-providers
```

## Setup example

```bash
export GEMINI_API_KEY="your-key"      # Nano Banana / Imagen
# or
export OPENAI_API_KEY="your-key"      # DALL·E
# or
export STABILITY_API_KEY="your-key"   # Stability

python3 generate_image.py --prompt-file prompt.txt --out assets/my-article-illustrations/01-topic.png
```

If no key is set, the script exits with a clear message listing the variables to set.

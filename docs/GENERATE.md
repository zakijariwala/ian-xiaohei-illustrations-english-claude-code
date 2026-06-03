# How to Generate PNGs

Two supported paths. Use whichever fits your setup.

---

## Path A — Claude Code (Claude Pro / Max)

No API key needed beyond your existing Claude subscription. Claude Code has a
built-in image generation tool (`image_gen`) that the skill calls automatically.

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Or download the desktop app from [claude.ai/code](https://claude.ai/code).
Sign in with your Claude Pro or Max account.

### 2. Install the skill

```bash
git clone https://github.com/zakijariwala/ian-xiaohei-illustrations-english-claude-code.git
cd ian-xiaohei-illustrations-english-claude-code
./ian-xiaohei-illustrations/install.sh claude
```

### 3. Open a project and generate

Start Claude Code in any directory:

```bash
claude
```

Then invoke the skill and ask for images:

```text
/ian-xiaohei-illustrations Generate one illustration for this concept:
"Small consistent actions compound over time into an inevitable result."
Use character: al-zill.
```

Or generate from the example prompts:

```text
/ian-xiaohei-illustrations Generate an illustration using this prompt:
<paste contents of examples/prompts/09-al-zill-compounding.txt>
```

Claude Code calls `image_gen` internally and saves the PNG to
`assets/<article-slug>-illustrations/` in your working directory.

### What happens under the hood

```
you type /ian-xiaohei-illustrations + request
         ↓
skill loads SKILL.md + references/characters/<id>.md
         ↓
builds a generation-ready prompt
         ↓
calls built-in image_gen tool  ← uses your Claude Pro subscription
         ↓
saves PNG to assets/
```

No script, no API key, no extra setup.

---

## Path B — Nano Banana (Google AI Studio)

Nano Banana is Google's `gemini-2.5-flash-image-preview` model. The free tier
is enough for personal use. You get a key in under two minutes.

### 1. Get a key

1. Go to **[aistudio.google.com](https://aistudio.google.com)**
2. Click **"Get API key"** → **"Create API key"**
3. Copy the key

That's it. No billing required for the free tier.

### 2. Set the key

```bash
export GEMINI_API_KEY="your-key-here"
```

To make it permanent, add that line to `~/.bashrc` or `~/.zshrc` and run
`source ~/.bashrc`.

Verify it's detected:

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py --list-providers
# → Available (key present): nanobanana, imagen
```

### 3. Generate one example image

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider nanobanana \
  --character xiaohei \
  --prompt-file examples/prompts/01-xiaohei-content-press.txt \
  --out examples/output/01-xiaohei-content-press.png
```

The terminal prints the output path when done (10–20 seconds per image).

### 4. Generate all 9 character examples

```bash
cd ian-xiaohei-illustrations-english-claude-code

for entry in \
  "xiaohei:01-xiaohei-content-press" \
  "chibi-kage:02-chibi-kage-knowledge-loom" \
  "kaala:03-kaala-four-streams" \
  "kali-tikka:04-kali-tikka-jugaad" \
  "le-bloc:05-le-bloc-approval-loop" \
  "the-smudge:06-the-smudge-ship-it" \
  "dudu:07-dudu-arm-filter" \
  "el-manchon:08-el-manchon-content-chain" \
  "al-zill:09-al-zill-compounding"
do
  char="${entry%%:*}"
  slug="${entry##*:}"
  echo "→ $char"
  python3 ian-xiaohei-illustrations/scripts/generate_image.py \
    --provider nanobanana \
    --character "$char" \
    --prompt-file "examples/prompts/${slug}.txt" \
    --out "examples/output/${slug}.png"
done
```

All 9 PNGs land in `examples/output/`.

### 5. Generate from your own article

Write your prompt to a file and run:

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider nanobanana \
  --character the-smudge \
  --prompt "Generate one standalone 16:9 horizontal article illustration.
Visual DNA: Pure white background. Minimalist black hand-drawn line art...
Theme: shipping a feature that is 80% done but needs to go out today." \
  --out my-article-illustrations/01-ship-it.png
```

Or use the template in `references/prompt-template.md`, fill in the variables,
save as a `.txt` file, and pass it with `--prompt-file`.

---

## Comparison

| | Path A — Claude Code | Path B — Nano Banana |
|--|---------------------|----------------------|
| **Requires** | Claude Pro / Max subscription | Free Google AI Studio key |
| **Setup** | Install Claude Code, install skill | `export GEMINI_API_KEY=...` |
| **How you invoke** | `/ian-xiaohei-illustrations` in Claude Code | `python3 scripts/generate_image.py` |
| **Image quality** | Claude's native image generation | Gemini 2.5 Flash Image |
| **Speed** | ~15–30s per image | ~10–20s per image |
| **Cost** | Included in Pro/Max subscription | Free tier (generous quota) |
| **Best for** | Interactive workflow, article writing sessions | Batch generation, scripting, CI |

---

## Troubleshooting

### Path A — Claude Code

| Problem | Fix |
|---------|-----|
| Skill not found | Run `./ian-xiaohei-illustrations/install.sh claude`, restart Claude Code |
| `image_gen` not available | Requires Claude Pro or Max — free tier doesn't include image generation |
| Image looks like a PPT | Ask the skill: *"Regenerate — remove the title from the top-left, make Xiaohei more central to the action"* |
| Wrong character | Add *"use character: the-smudge"* (or any ID) to your request |

### Path B — Nano Banana

| Problem | Fix |
|---------|-----|
| `No image provider API key found` | Check `echo $GEMINI_API_KEY` — must be set in the same terminal session |
| `HTTP 400: API key not valid` | Key copied incorrectly, or Google takes ~30s to activate a new key — wait and retry |
| `HTTP 429: Resource exhausted` | Free tier rate limit hit — wait 60 seconds and retry |
| `No image returned` | Model returned text instead of an image; the `gemini-2.5-flash-image-preview` model is in preview and occasionally does this — run again |
| Blank white PNG | Same as above — retry, or switch to `--provider imagen` (same key, different model) |
| Want higher quality | Switch to Imagen: `--provider imagen` (uses the same `GEMINI_API_KEY`) |

### Switching between Imagen and Nano Banana

Both use the same `GEMINI_API_KEY`. Imagen (`imagen-3.0-generate-002`) is more
photorealistic; Nano Banana is faster and handles the hand-drawn sketch style well.

```bash
# Nano Banana (default for Google key)
python3 scripts/generate_image.py --provider nanobanana --character xiaohei ...

# Imagen (same key, more detailed output)
python3 scripts/generate_image.py --provider imagen --character xiaohei ...
```

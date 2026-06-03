# How to Generate PNGs

Three ways to generate images from the skill prompts:

1. **[Via script + API key](#via-script--api-key)** — Nano Banana, DALL·E, Imagen, Stability. Run locally, batch-friendly.
2. **[Via Claude Code](#via-claude-code-claude-pro--max)** — native `image_gen`, no API key needed, just your Claude Pro subscription.
3. **[Free via apps and websites (no API key)](#free-via-apps-and-websites)** — paste the prompt into a web UI and download the image manually.

---

## Via Script + API Key

The bundled script `scripts/generate_image.py` sends the prompt to an image model API and saves a PNG. Pick whichever provider you have access to.

### Provider overview

| Provider | Model | Free tier | API key env var | Get key |
|----------|-------|-----------|-----------------|---------|
| **Nano Banana** | `gemini-2.5-flash-image-preview` | ✅ Yes | `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) |
| **Imagen** | `imagen-3.0-generate-002` | ✅ Yes (same key) | `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) |
| **DALL·E** | `gpt-image-1` (→ `dall-e-3`) | ❌ Paid only | `OPENAI_API_KEY` | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| **Stability** | Stable Image SD3 | ⚠️ Trial credits | `STABILITY_API_KEY` | [platform.stability.ai](https://platform.stability.ai) |

---

### Nano Banana (Google) — recommended, free tier available

`gemini-2.5-flash-image-preview` — fast, handles the hand-drawn sketch style well.

**Step 1 — Get a free key (2 minutes)**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **"Get API key"** → **"Create API key"**
3. Copy the key — no billing required for the free tier

**Step 2 — Set the key**
```bash
export GEMINI_API_KEY="your-key-here"
```

To make it permanent across sessions:
```bash
echo 'export GEMINI_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Step 3 — Verify**
```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py --list-providers
# → Available (key present): nanobanana, imagen
```

**Step 4 — Generate**
```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider nanobanana \
  --character xiaohei \
  --prompt-file examples/prompts/01-xiaohei-content-press.txt \
  --out examples/output/01-xiaohei-content-press.png
```

**Troubleshooting**

| Error | Fix |
|-------|-----|
| `No image provider API key found` | Run `echo $GEMINI_API_KEY` to confirm it's set in this terminal |
| `HTTP 400: API key not valid` | Key copied incorrectly, or wait ~30s for Google to activate it |
| `HTTP 429: Resource exhausted` | Free tier rate limit — wait 60s and retry |
| `No image returned` | Model occasionally returns text in preview — run again |
| Blank white PNG | Same — retry, or switch to `--provider imagen` |

---

### Imagen (Google) — same key, higher detail

`imagen-3.0-generate-002` — more precise output, uses the same `GEMINI_API_KEY`.

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider imagen \
  --character the-smudge \
  --prompt-file examples/prompts/06-the-smudge-ship-it.txt \
  --out examples/output/06-the-smudge-ship-it.png
```

Use Nano Banana for speed. Switch to Imagen when you want more detail or if Nano Banana returns text instead of an image.

**Troubleshooting**

| Error | Fix |
|-------|-----|
| `HTTP 400` | Check billing — Imagen may require an active Google Cloud billing account even on free tier |
| `No predictions in response` | Model didn't produce output — retry or fall back to `--provider nanobanana` |

---

### DALL·E (OpenAI) — paid, high quality text rendering

`gpt-image-1` — best at rendering legible handwritten labels. Requires a paid OpenAI account.

**Step 1 — Get a key**
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click **"Create new secret key"**
3. Add credits at [platform.openai.com/settings/billing](https://platform.openai.com/settings/billing) — minimum $5

**Step 2 — Set the key**
```bash
export OPENAI_API_KEY="your-key-here"
```

**Step 3 — Generate**
```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider dalle \
  --character le-bloc \
  --prompt-file examples/prompts/05-le-bloc-approval-loop.txt \
  --out examples/output/05-le-bloc-approval-loop.png
```

The script uses `gpt-image-1` by default. To force `dall-e-3`:
```bash
OPENAI_IMAGE_MODEL=dall-e-3 python3 scripts/generate_image.py --provider dalle ...
```

**Troubleshooting**

| Error | Fix |
|-------|-----|
| `HTTP 401` | Invalid API key — check it was copied correctly |
| `HTTP 429` | Rate limit or insufficient credits — top up at platform.openai.com/billing |
| `HTTP 400: billing_hard_limit_reached` | Add more credits |

---

### Stability AI — trial credits available

`stable-image-sd3` — requires the `requests` Python package.

**Step 1 — Get a key**
1. Go to [platform.stability.ai](https://platform.stability.ai)
2. Create an account — new accounts receive free trial credits
3. Go to **Account → API Keys** and copy your key

**Step 2 — Install requests and set the key**
```bash
pip install requests
export STABILITY_API_KEY="your-key-here"
```

**Step 3 — Generate**
```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider stability \
  --character dudu \
  --prompt-file examples/prompts/07-dudu-arm-filter.txt \
  --out examples/output/07-dudu-arm-filter.png
```

**Troubleshooting**

| Error | Fix |
|-------|-----|
| `ImportError: requests` | Run `pip install requests` |
| `HTTP 402: Payment Required` | Trial credits exhausted — top up at platform.stability.ai |
| `HTTP 403` | API key invalid or expired |

---

### Generate all 9 character examples (any provider)

```bash
cd ian-xiaohei-illustrations-english-claude-code

PROVIDER="nanobanana"   # change to: imagen, dalle, stability

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
  echo "→ generating $char"
  python3 ian-xiaohei-illustrations/scripts/generate_image.py \
    --provider "$PROVIDER" \
    --character "$char" \
    --prompt-file "examples/prompts/${slug}.txt" \
    --out "examples/output/${slug}.png"
done
```

All 9 PNGs land in `examples/output/`.

---

### Auto-detect (no --provider flag)

If you set a key and omit `--provider`, the script picks the first available in order:
`nanobanana → dalle → imagen → stability`

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character xiaohei \
  --prompt-file examples/prompts/01-xiaohei-content-press.txt \
  --out examples/output/01-xiaohei-content-press.png
```

---

## Via Claude Code (Claude Pro / Max)

No API key needed. Claude Code has a built-in `image_gen` tool that the skill
calls automatically using your existing Claude Pro or Max subscription.

**Step 1 — Install Claude Code**
```bash
npm install -g @anthropic-ai/claude-code
# or download the desktop app from claude.ai/code
```

**Step 2 — Install the skill**
```bash
./ian-xiaohei-illustrations/install.sh claude
```

**Step 3 — Generate inside Claude Code**
```bash
claude   # open Claude Code in your project directory
```

Then type:
```text
/ian-xiaohei-illustrations Generate one illustration for this concept using character al-zill:
"Small consistent actions compound into an inevitable result."
```

Claude Code builds the prompt, calls `image_gen` internally, and saves the PNG to
`assets/<article-slug>-illustrations/` in your working directory.

**To generate from an example prompt file:**
```text
/ian-xiaohei-illustrations Generate an illustration using this prompt:
<paste contents of examples/prompts/09-al-zill-compounding.txt>
```

**Troubleshooting**

| Problem | Fix |
|---------|-----|
| Skill not found | Re-run `./ian-xiaohei-illustrations/install.sh claude`, restart Claude Code |
| `image_gen` not available | Free Claude tier doesn't include image generation — requires Pro or Max |
| Image looks like a PPT | Ask: *"Regenerate — remove the top-left title, make the character more central to the action"* |

---

## Free via Apps and Websites

No API key, no script. Copy the prompt from `examples/prompts/`, paste it into a
web UI, and download the result manually.

The prompts in `examples/prompts/` are plain text files — open any one, copy the
full contents, and paste into any of the services below.

### Option 1 — Claude.ai (Claude Pro)

1. Go to [claude.ai](https://claude.ai) and sign in with your Pro account
2. Open a new conversation
3. Type: *"Generate an image using this prompt:"* then paste the prompt text
4. Claude generates and displays the image — right-click → Save image

Free for Claude Pro subscribers. No setup.

### Option 2 — Google AI Studio (free)

1. Go to [aistudio.google.com](https://aistudio.google.com) — sign in with any Google account
2. Click **"Create new prompt"** → choose **Gemini 2.5 Flash** or an image-capable model
3. Paste the prompt into the prompt box
4. Click **"Run"** — the image appears inline
5. Right-click → Save image

Free tier, no billing required. Same model as `--provider nanobanana`.

### Option 3 — Microsoft Designer / Bing Image Creator (free)

1. Go to [designer.microsoft.com](https://designer.microsoft.com) or [bing.com/images/create](https://bing.com/images/create)
2. Sign in with a Microsoft account (free)
3. Paste the prompt — note: these tools work better with shorter prompts
4. Select the most sketch-like result and download

**Tip for shorter prompts:** extract just the `Theme:`, `Core idea:`, and `Composition:` sections plus the IP character block — that's usually enough.

Free, no sign-up beyond a Microsoft account. Powered by DALL·E.

### Option 4 — Adobe Firefly (free tier)

1. Go to [firefly.adobe.com](https://firefly.adobe.com)
2. Sign in with a free Adobe account
3. Use **"Text to image"** → paste the prompt
4. Download the result

Free tier includes a monthly credit allowance. Good for clean illustration styles.

### Option 5 — Ideogram (free tier)

1. Go to [ideogram.ai](https://ideogram.ai)
2. Sign in (free account)
3. Paste the prompt — Ideogram is particularly good at rendering legible text/labels inside images
4. Download the result

Good choice when the image needs readable annotation labels. Free tier available.

### Option 6 — Hugging Face Spaces (free, open source)

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Search for `FLUX.1` or `Stable Diffusion` image generation spaces
3. Paste the prompt and run
4. Download the generated image

Fully free, community-hosted. Quality and speed vary by space.

---

### Tips for pasting prompts into web UIs

- **Use the full prompt** from `examples/prompts/*.txt` — don't trim it
- **Aspect ratio:** most UIs have a 16:9 or landscape option — always select it
- **If the UI has a "style" preset:** choose "illustration," "sketch," or "line art" to stay consistent with the visual DNA
- **If the result has a top-left title:** regenerate once — this usually resolves itself; or use the editing prompt from `references/prompt-template.md`
- **If Xiaohei/the character is too cute:** add to the prompt: *"deadpan, blank serious expression, not cute, not mascot"*

---

## Provider Comparison

| | Nano Banana | Imagen | DALL·E | Stability | Claude Code | Web UI |
|--|-------------|--------|--------|-----------|-------------|--------|
| **Cost** | Free tier | Free tier | Paid | Trial credits | Pro subscription | Free |
| **Setup** | API key | API key | API key + credits | API key + pip | Install CLI | None |
| **Script** | ✅ | ✅ | ✅ | ✅ | ❌ (native) | ❌ (manual) |
| **Batch** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Speed** | ~15s | ~20s | ~20s | ~25s | ~20s | varies |
| **Label quality** | Good | Good | Best | Good | Good | varies |
| **Best for** | Scripting, free use | Detail, free use | Accurate labels | Open-source | Interactive sessions | One-off images |

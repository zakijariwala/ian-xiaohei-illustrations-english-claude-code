# Setup Guide — Per-Agent Installation & Usage

Step-by-step instructions for setting up Ian Xiaohei Illustrations on every supported platform.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Claude Code](#claude-code)
3. [OpenAI Codex](#openai-codex)
4. [Gemini CLI](#gemini-cli)
5. [Hermes Agents](#hermes-agents)
6. [Antigravity](#antigravity)
7. [Switching Characters](#switching-characters)
8. [Image Generation Setup](#image-generation-setup)
9. [Troubleshooting](#troubleshooting)

> **Generating PNGs with Claude Pro or Nano Banana?** See the focused guide: [GENERATE.md](GENERATE.md)

---

## Prerequisites

**All platforms require:**

- Git (to clone the repo)
- Python 3.8+ (for the image generation binding)
- At least one image provider API key (for actual image generation — see [Image Generation Setup](#image-generation-setup))

**Clone the repo once, then follow the steps for your platform:**

```bash
git clone https://github.com/zakijariwala/ian-xiaohei-illustrations-english-claude-code.git
cd ian-xiaohei-illustrations-english-claude-code
```

---

## Claude Code

**Entry point:** `ian-xiaohei-illustrations/SKILL.md`
**Invoke with:** `/ian-xiaohei-illustrations`

### Step 1 — Install Claude Code

If you don't have it:

```bash
npm install -g @anthropic-ai/claude-code
```

Or download the desktop app from [claude.ai/code](https://claude.ai/code).

### Step 2 — Install the Skill

```bash
chmod +x ian-xiaohei-illustrations/install.sh
./ian-xiaohei-illustrations/install.sh claude
```

This copies the `ian-xiaohei-illustrations/` directory to `~/.claude/skills/ian-xiaohei-illustrations/`.

**Manual alternative:**

```bash
mkdir -p ~/.claude/skills
cp -R ./ian-xiaohei-illustrations ~/.claude/skills/
```

### Step 3 — Set an Image API Key

```bash
# Pick one provider
export GEMINI_API_KEY="your-gemini-key"   # Nano Banana / Imagen
# or
export OPENAI_API_KEY="your-openai-key"   # DALL·E
# or
export STABILITY_API_KEY="your-key"       # Stability
```

To make the key permanent, add the export line to `~/.bashrc` or `~/.zshrc`.

### Step 4 — Open a Project and Invoke

Start Claude Code in your article project directory:

```bash
cd ~/my-article-project
claude
```

Then use the skill:

```text
/ian-xiaohei-illustrations Generate 5 illustrations for this article.

<paste article content>
```

### Common Claude Code Commands

| What you want | Command |
|---------------|---------|
| Plan a shot list only | `/ian-xiaohei-illustrations Analyze this article. Give me a shot list of 5 illustrations — no generation yet.` |
| Generate all illustrations | `/ian-xiaohei-illustrations Generate illustrations for this article: <article>` |
| Single concept image | `/ian-xiaohei-illustrations One image for the idea: "<concept>"` |
| Fix a title in an image | `/ian-xiaohei-illustrations Remove the top-left title from this image. Keep everything else.` |
| Chinese annotations | `/ian-xiaohei-illustrations Generate illustrations with Chinese annotations instead of English.` |

### Notes

- The skill appears in the Claude Code skill picker under the name **ian-xiaohei-illustrations**.
- If a native `image_gen` tool is available in your Claude Code environment, it's used directly. Otherwise the skill falls back to `scripts/generate_image.py`.
- Generated images are saved to `assets/<article-slug>-illustrations/` within your current working directory.

---

## OpenAI Codex

**Entry point:** `ian-xiaohei-illustrations/agents/openai.yaml`
**Invoke with:** `Use $ian-xiaohei-illustrations ...`

### Step 1 — Install Codex

```bash
npm install -g @openai/codex
```

Log in:

```bash
codex auth login
```

### Step 2 — Install the Skill

```bash
chmod +x ian-xiaohei-illustrations/install.sh
./ian-xiaohei-illustrations/install.sh codex
```

This copies the skill to `~/.codex/skills/ian-xiaohei-illustrations/`.

**Manual alternative:**

```bash
mkdir -p ~/.codex/skills
cp -R ./ian-xiaohei-illustrations ~/.codex/skills/
```

If your Codex home is non-standard:

```bash
CODEX_HOME=/path/to/codex ./ian-xiaohei-illustrations/install.sh codex
```

### Step 3 — Set an Image API Key

```bash
export OPENAI_API_KEY="your-openai-key"   # DALL·E (gpt-image-1)
# or use Gemini
export GEMINI_API_KEY="your-gemini-key"
```

### Step 4 — Use in Codex

```text
Use $ian-xiaohei-illustrations to design and generate 5 Xiaohei hand-drawn illustrations
for this article. 16:9, pure white, sparse English annotations.

<paste article content>
```

### Common Codex Commands

```text
# Shot list only
Use $ian-xiaohei-illustrations. Don't generate yet.
Give me a shot list of 5 illustrations for this article: <article>

# Generate directly
Use $ian-xiaohei-illustrations. Generate 4 illustrations for: <article>

# One concept
Use $ian-xiaohei-illustrations. One image for: "Shipping fast beats shipping perfect."
```

---

## Gemini CLI

**Entry point:** `ian-xiaohei-illustrations/agents/gemini.md`
**Invoke with:** `@ian-xiaohei-illustrations` (or by describing the task)

### Step 1 — Install Gemini CLI

```bash
npm install -g @google/gemini-cli
```

Authenticate:

```bash
gemini auth login
```

### Step 2 — Install the Skill

```bash
chmod +x ian-xiaohei-illustrations/install.sh
./ian-xiaohei-illustrations/install.sh gemini
```

This copies the skill to `~/.gemini/skills/ian-xiaohei-illustrations/`.

**Manual alternative:**

```bash
mkdir -p ~/.gemini/skills
cp -R ./ian-xiaohei-illustrations ~/.gemini/skills/
```

### Step 3 — Set an Image API Key

Gemini CLI can use your existing Gemini credentials for Nano Banana:

```bash
export GEMINI_API_KEY="your-gemini-key"
# Nano Banana and Imagen are both available with the same key
```

Or use DALL·E:

```bash
export OPENAI_API_KEY="your-openai-key"
```

### Step 4 — Use in Gemini CLI

```text
@ian-xiaohei-illustrations Generate 5 Xiaohei illustrations for this article.

<paste article content>
```

### Common Gemini CLI Commands

```text
# Plan shot list
@ian-xiaohei-illustrations Plan a shot list for this article. No images yet.
<article>

# Full generation with Nano Banana
@ian-xiaohei-illustrations Generate 4 illustrations using Nano Banana.
<article>

# Single concept
@ian-xiaohei-illustrations One illustration for: "Every habit is a vote for an identity."
```

### Notes

- The Gemini CLI config (`agents/gemini.md`) is a Markdown-format skill, similar to Claude Code's `SKILL.md`.
- It uses the same bundled `scripts/generate_image.py` fallback as the other platforms.
- If Gemini CLI updates its skill directory location, update the install path accordingly.

---

## Hermes Agents

**Entry point:** `ian-xiaohei-illustrations/agents/hermes.yaml`

Hermes-based agent frameworks (e.g. custom agents built on Nous Research Hermes models or similar OpenHermes-compatible systems) load the skill via the YAML config.

### Step 1 — Copy the Skill into Your Agent's Skills Directory

The exact path depends on your Hermes setup. Common locations:

```bash
# If your framework looks for skills in ~/.hermes/skills/:
mkdir -p ~/.hermes/skills
cp -R ./ian-xiaohei-illustrations ~/.hermes/skills/

# If your framework loads skills from the project directory:
cp -R ./ian-xiaohei-illustrations ./skills/
```

### Step 2 — Register the Skill in Your Agent Config

In your agent's configuration (e.g. `agent.yaml` or `config.json`), add the skill:

```yaml
# agent.yaml
skills:
  - path: ./skills/ian-xiaohei-illustrations/agents/hermes.yaml
```

Or, if your framework loads all YAMLs from a skills directory, just copy the file there — no extra registration needed.

### Step 3 — Set an Image API Key

```bash
export GEMINI_API_KEY="your-key"   # or OPENAI_API_KEY / STABILITY_API_KEY
```

### Step 4 — Invoke the Skill

The Hermes config defines these trigger phrases:

```text
article illustrations
shot list
body copy illustration
xiaohei
hand-drawn illustration
visual metaphor for article
```

Any message containing one of these phrases routes to the skill. Example:

```text
Generate article illustrations for this blog post about habit formation.
<article content>
```

### Notes

- The `system_prompt` in `agents/hermes.yaml` is loaded as the skill's system context.
- Both `image_generation` (native) and `shell` (for the `generate_image.py` fallback) are declared as tools.
- If your Hermes framework uses a different tool name for image generation, update the `tools:` section in `agents/hermes.yaml`.

---

## Antigravity

**Entry point:** `ian-xiaohei-illustrations/agents/antigravity.yaml`

### Step 1 — Copy the Skill

```bash
# Adjust the path to match your Antigravity setup
cp -R ./ian-xiaohei-illustrations ~/.antigravity/skills/
# or
cp -R ./ian-xiaohei-illustrations ./skills/
```

### Step 2 — Load the Skill Config

The Antigravity config at `agents/antigravity.yaml` declares:
- Trigger phrases
- Reference files (loaded on-demand)
- Image generation tools (native first, then `scripts/generate_image.py` fallback)
- Output path and file naming conventions

Point your Antigravity agent at the config file, or drop the whole skill directory into your framework's skills folder.

### Step 3 — Set an Image API Key

```bash
export GEMINI_API_KEY="your-key"   # or OPENAI_API_KEY / STABILITY_API_KEY
```

### Step 4 — Invoke

Use any trigger phrase from the config:

```text
generate illustrations
shot list
article illustration
xiaohei
hand-drawn image
visual metaphor
```

Example:

```text
Generate a shot list for this article. No images yet.
<article content>
```

---

## Switching Characters

The default character is **Xiaohei**. All platforms support character selection.

### In a skill prompt (any platform)

```text
Use character: the-smudge. Generate 4 illustrations for this article.
<article>
```

```text
Use the European character. Generate a shot list for this article.
<article>
```

Any of these work: character name, ID, alias, or culture description.

### Via the generation script

```bash
# See all available characters
python3 ian-xiaohei-illustrations/scripts/generate_image.py --list-characters

# Use a specific character by ID
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character the-smudge \
  --prompt-file prompt.txt \
  --out 01-topic.png

# Use an alias
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character smudge \
  --prompt-file prompt.txt \
  --out 01-topic.png

# Combine with provider selection
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character al-zill \
  --provider dalle \
  --prompt-file prompt.txt \
  --out 01-topic.png
```

### Character ID reference

| ID | Display Name | Culture | Aliases |
|----|-------------|---------|---------|
| `xiaohei` | Xiaohei (小黑) | Chinese / East Asian | `xiao-hei`, `小黑` |
| `chibi-kage` | Chibi Kage (小影) | Japanese | `kage`, `小影` |
| `kaala` | Kaala (काला) | South / Southeast Asian | `kala` |
| `kali-tikka` | Kali Tikka | Indian (block-print / folk art) | `tikka` |
| `le-bloc` | Le Bloc / Der Fleck | European | `bloc`, `der-fleck`, `fleck` |
| `the-smudge` | The Smudge | American | `smudge` |
| `dudu` | Dudu | West African / Afrofuturist | — |
| `el-manchon` | El Manchón | Latin American | `manchon` |
| `al-zill` | Al-Zill (الظل) | Middle Eastern / Arabic | `zill`, `الظل` |

Full descriptors (appearance, personality, prompt injection block): `ian-xiaohei-illustrations/references/characters/<id>.md`

---

## Image Generation Setup

> For the recommended Claude Pro and Nano Banana workflows, see **[GENERATE.md](GENERATE.md)**.

The skill uses a two-layer approach:

```
1. Native image tool (if the host agent provides one)
         ↓  (if not available)
2. scripts/generate_image.py (bundled binding, auto-detects provider)
```

### Choosing a Provider

| Provider | Best for | Cost | Notes |
|----------|----------|------|-------|
| **Nano Banana** (Gemini) | Fast, creative, good blank-space control | Pay-per-use | Recommended first choice |
| **DALL·E** (gpt-image-1) | High quality, accurate text rendering | Pay-per-use | Falls back to dall-e-3 |
| **Imagen** (Google) | Photorealistic, clean style | Pay-per-use | Same key as Nano Banana |
| **Stability** | Open ecosystem, local option | Pay-per-use or self-host | Needs `requests` package |

### Getting API Keys

**Nano Banana / Imagen (Google):**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Create an API key
3. `export GEMINI_API_KEY="your-key"`

**DALL·E (OpenAI):**
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Create an API key
3. `export OPENAI_API_KEY="your-key"`

**Stability AI:**
1. Go to [platform.stability.ai](https://platform.stability.ai)
2. Create an API key
3. `export STABILITY_API_KEY="your-key"`
4. Also install `requests`: `pip install requests`

### Using the Binding Directly

```bash
cd ian-xiaohei-illustrations

# Check which providers are available
python3 scripts/generate_image.py --list-providers

# Generate from a prompt file (auto-detects provider)
python3 scripts/generate_image.py \
  --prompt-file prompt.txt \
  --out assets/my-article-illustrations/01-topic.png

# Force a specific provider
python3 scripts/generate_image.py \
  --provider dalle \
  --prompt-file prompt.txt \
  --out 01-topic.png

# Inline prompt
python3 scripts/generate_image.py \
  --provider nanobanana \
  --prompt "Generate one 16:9 illustration: ..." \
  --out 01-topic.png

# Pipe prompt from stdin
cat prompt.txt | python3 scripts/generate_image.py --out 01-topic.png
```

### Override Models

```bash
# Use a different Nano Banana model
export NANOBANANA_MODEL="gemini-2.0-flash-exp"

# Use dall-e-3 instead of gpt-image-1
export OPENAI_IMAGE_MODEL="dall-e-3"

# Use a different Imagen version
export IMAGEN_MODEL="imagen-3.0-fast-generate-001"
```

---

## Troubleshooting

### "No image provider API key found"

```
Error: No image provider API key found. Set one of:
  GEMINI_API_KEY / GOOGLE_API_KEY  (Nano Banana / Imagen)
  OPENAI_API_KEY                   (DALL-E)
  STABILITY_API_KEY                (Stability)
```

**Fix:** Export one of the listed variables. Verify with:

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py --list-providers
```

### Skill not appearing in Claude Code

- Confirm it's in `~/.claude/skills/ian-xiaohei-illustrations/SKILL.md`
- Restart Claude Code
- Check the skill name matches: `name: ian-xiaohei-illustrations` in `SKILL.md` frontmatter

### Image has a top-left title / looks like a PPT

This is a known model behavior. Ask the skill to fix it:

```text
/ian-xiaohei-illustrations Edit this image. Remove the top-left title. Keep everything else.
```

Or set a higher iteration threshold — the QA checklist in `references/qa-checklist.md` lists all failure signals.

### Chinese characters appear in annotations (when you want English)

The default is English. If you see Chinese, your prompt may have been derived from a Chinese-language article. Explicitly add to your request:

```text
Use only English annotations, 1–4 words each.
```

### Stability provider fails

Make sure `requests` is installed:

```bash
pip install requests
```

### Image is blank / all white

Usually a model-side error. Try a different provider:

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --provider dalle \
  --prompt-file prompt.txt \
  --out out.png
```

### Permission denied on install.sh

```bash
chmod +x ian-xiaohei-illustrations/install.sh
```

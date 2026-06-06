# Project Handover — Ian Xiaohei Illustrations (English / Claude Code Port)

**Prepared for:** Chief of Staff  
**Date:** 2026-06-06  
**Owner:** Zaki Jariwala (jariwalazaki@gmail.com)  
**Repo:** `zakijariwala/ian-xiaohei-illustrations-english-claude-code`  
**Active branch:** `claude/skill-plugin-port-ZYCfj`  
**Repo status:** All code committed and pushed. Working tree clean.

---

## What This Project Is

An open-source AI agent skill for generating hand-drawn article illustrations. The user
found a Chinese-language skill built for OpenAI Codex with no actual image generation,
ported it to English and Claude Code format, added real image generation, and expanded
the single original character into a system of nine culturally-grounded variants.

The skill reads an article, identifies the one cognitive structure worth drawing, and
renders a clean 16:9 hand-drawn illustration in a deadpan ink-blob style.

**Repo purpose:** This is a public open-source release, not a private tool. The goal is
for it to be discovered and used by the community — it is being positioned for virality.

---

## Current State

### What Is Done (100%)

| Area | Status |
|------|--------|
| SKILL.md — Claude Code skill format | Done |
| All reference files translated Chinese → English | Done |
| Image generation (4 providers: Nano Banana, DALL·E, Imagen 3, Stability) | Done |
| 9-character cultural variant system | Done |
| install.sh — idempotent installer, preserves settings on upgrade | Done |
| scan_project.py — pre-generation project context extractor | Done |
| settings.json — persistent default character | Done |
| Multi-platform agents (Gemini CLI, Hermes, Antigravity, Codex) | Done |
| README overhaul (hero image, badges, gallery, quick-start) | Done |
| docs/SETUP.md and docs/GENERATE.md — full provider setup guides | Done |
| examples/prompts/ — 9 prompt files, one per character | Done |
| Cultural de-risk pass — removed stereotypes, documented philosophy | Done |
| Council of Claude review (2 rounds, 4 agents each) — all findings fixed | Done |
| LinkedIn post — written, fact-checked, ready to post | Done |

### What Is NOT Done (Pending Owner Action)

#### 1. Generate the 9 character example images  
**Blocking:** The README gallery shows 6 pre-existing generic images. There are no
images showing any of the 9 characters in action. This is the biggest gap for virality.

**What's needed:** Run each of the 9 prompts in `examples/prompts/` through an image
model (Gemini web UI, Claude.ai Pro, or API) and save the outputs as PNGs.

**Owner's plan:** Use Gemini web interface manually. The 9 prompts were provided in
the last Claude Code session — they are also in `examples/prompts/01-*.txt` through
`examples/prompts/09-*.txt`. Each prompt is ready to paste with no modification.

**Output filenames to use:**
```
examples/images/01-xiaohei-content-press.png
examples/images/02-chibi-kage-knowledge-loom.png
examples/images/03-kaala-four-streams.png
examples/images/04-kali-tikka-block-print.png
examples/images/05-le-bloc-approval-loop.png
examples/images/06-the-smudge-ship-it.png
examples/images/07-dudu-arm-filter.png
examples/images/08-el-manchon-content-chain.png
examples/images/09-al-zill-compounding.png
```

After adding images: commit, push to `claude/skill-plugin-port-ZYCfj`, then ask
Claude Code to update the README gallery to reference the new filenames.

#### 2. Merge branch to main  
The branch `claude/skill-plugin-port-ZYCfj` has all the work. Main is the original
untouched Chinese Codex version. Once images are done (or independently), merge:

```bash
git checkout main
git merge claude/skill-plugin-port-ZYCfj
git push origin main
```

Or open a GitHub PR for a record — the owner has not explicitly requested this yet.

#### 3. Add GitHub topics  
On the repo page → gear icon next to "About" → add:
```
claude-code  ai-skill  illustration  prompt-engineering
hand-drawn  article-illustration  openai  gemini
```
This is how the repo gets discovered via GitHub search. Takes 2 minutes.

#### 4. Post the LinkedIn post  
The post is written and fact-checked. One phrase was corrected during fact-check:
- **Old (false):** "zero external dependencies"
- **Correct:** "stdlib Python for three of the four providers"
  (Stability AI requires `pip install requests`; the other three use stdlib only)

The corrected post is ready — see the last Claude Code session for the full text,
or ask Claude Code to reprint it.

---

## Key Technical Decisions (for context)

- **Why 9 characters instead of 1:** The original had only Xiaohei. Each new character
  is grounded in a real art tradition (ukiyo-e, Madhubani block-print, Adinkra/kente,
  WPA poster, Arabic calligraphy, etc.) so they are not "Asian/African style" caricatures
  but stylistically coherent IP variants. Philosophy documented in
  `ian-xiaohei-illustrations/references/characters/INDEX.md`.

- **Why four image providers:** No single provider is universally available. Nano Banana
  (Gemini) has a free tier; Claude Pro users get native image generation with no API key;
  DALL·E and Stability are paid alternatives. The skill auto-detects which key is set.

- **Why the branch hasn't been merged yet:** The owner wanted to populate the character
  gallery before making the main branch the public face of the repo.

- **The "council of Claude" pattern:** Two rounds of 4 parallel Claude agents were run,
  each with a distinct review lens (Newcomer, Engineer, Growth Strategist, Docs Editor).
  This surfaced bugs and issues that single-pass review missed. Noted in the LinkedIn post
  as a technique worth publicizing.

---

## File Map (what lives where)

```
ian-xiaohei-illustrations/       ← installable skill directory
  SKILL.md                        ← Claude Code skill entrypoint
  install.sh                      ← run this to install locally
  settings.json                   ← default character config
  manifest.json                   ← universal plugin descriptor
  agents/
    openai.yaml                   ← Codex
    gemini.md                     ← Gemini CLI
    hermes.yaml                   ← Hermes
    antigravity.yaml              ← Antigravity
  scripts/
    generate_image.py             ← image generation (4 providers)
    scan_project.py               ← project context extractor
  references/
    style-dna.md                  ← visual rules
    composition-patterns.md       ← structure types
    prompt-template.md            ← generation template
    qa-checklist.md               ← pass/fail checklist
    characters/
      INDEX.md                    ← all 9 characters + cultural philosophy
      xiaohei.md … al-zill.md     ← one file per character

examples/
  prompts/                        ← 9 ready-to-paste prompts (one per character)
  images/                         ← 8 pre-existing generic PNGs (character PNGs missing)
  prompts.md                      ← usage scenarios guide
  character-examples.md           ← character gallery + prompt injections

docs/
  SETUP.md                        ← provider setup (API keys, free tiers)
  GENERATE.md                     ← generation workflow reference

README.md                         ← public-facing landing page
```

---

## How to Continue in a New Claude Code Session

Start a session in this repo directory and say:

> "Continue the ian-xiaohei-illustrations project. The HANDOVER.md has the full status.
> I've generated images — here are the files: [attach or list them]. Update the README
> gallery and merge to main."

Or to reprint the LinkedIn post:

> "Reprint the corrected LinkedIn post from the last session."

---

## Contact / Access

- GitHub repo: `zakijariwala/ian-xiaohei-illustrations-english-claude-code`
- Active branch: `claude/skill-plugin-port-ZYCfj`
- All secrets (API keys) live in the owner's local environment — not in the repo
- No CI/CD configured; all pushes are manual

# Project Handover — Ian Xiaohei Illustrations

**Prepared for:** Chief of Staff
**Date:** 2026-06-06
**Owner:** Zaki Jariwala (jariwalazaki@gmail.com)
**Repo:** github.com/zakijariwala/ian-xiaohei-illustrations-english-claude-code
**Active branch:** `claude/skill-plugin-port-ZYCfj`

---

## What This Project Is

An open-source Claude Code skill for generating hand-drawn article illustrations. Ported from a Chinese-language OpenAI Codex skill, expanded with real image generation and a system of nine culturally-grounded character variants. The skill reads an article, identifies the one cognitive structure worth drawing, and renders a clean 16:9 hand-drawn illustration in a deadpan ink-blob style.

**Hosting:** GitHub (public open-source release — no server, no running cost)
**Stack:** Python (stdlib for 3 of 4 providers; Stability AI requires `pip install requests`), SKILL.md format for Claude Code

**Image providers supported:** Nano Banana (Gemini free tier), DALL·E, Imagen 3, Stability AI — skill auto-detects which API key is set.

**The 9 characters:** Xiaohei, Chibi Kage, Kaala, Kali Tikka, Le Bloc, The Smudge, Dudu, El Manchón, Al-Zill — each grounded in a distinct art tradition (ukiyo-e, Madhubani, Adinkra, WPA poster, Arabic calligraphy, etc.).

---

## Current Status

**Code: 100% complete.** All files committed and pushed. Working tree clean.

**Blocked on owner-generated content before main branch becomes the public face:**

| Item | Status |
|------|--------|
| SKILL.md + all reference files | Done |
| 9-character cultural variant system | Done |
| 4-provider image generation | Done |
| install.sh (idempotent, preserves settings on upgrade) | Done |
| README overhaul | Done |
| docs/SETUP.md and docs/GENERATE.md | Done |
| 9 example prompt files | Done |
| Council of Claude review (2 rounds, 4 agents each) — all findings fixed | Done |
| LinkedIn post (written, fact-checked) | Done — ready to post |
| **9 character example images** | **Pending owner action** |
| **Merge to main** | **Pending** |
| **GitHub topics added** | **Pending** |

---

## Pending Owner Actions

- [ ] Generate the 9 character example images using Gemini web UI (prompts are in `examples/prompts/01-*.txt` through `09-*.txt`, ready to paste with no modification). Save as:
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
  Then ask Claude Code to update the README gallery to reference these filenames.
- [ ] Merge `claude/skill-plugin-port-ZYCfj` → `main` (once images are added, or independently)
- [ ] Add GitHub topics (repo page → gear icon next to "About"):
  `claude-code  ai-skill  illustration  prompt-engineering  hand-drawn  article-illustration  openai  gemini`
- [ ] Post the LinkedIn announcement (corrected text ready — ask Claude Code to reprint it)

---

## Day-to-Day Operating Procedure

This is a community open-source tool. Once launched:

- **Issues/PRs from community:** Zaki triages. New characters or providers are valid contributions.
- **No server, no running cost, no maintenance required** unless API provider changes break the generation scripts.
- **LinkedIn post reach:** Monitor for 48 hours after posting; respond to comments to maintain momentum.

---

## Deployment

No deployment step — this is a GitHub-hosted skill. "Deploying" means merging to `main` so the public URL is current.

**User install flow (once on main):**
```bash
curl -fsSL https://raw.githubusercontent.com/zakijariwala/ian-xiaohei-illustrations-english-claude-code/main/ian-xiaohei-illustrations/install.sh | bash
```

---

## Repo Structure

```
ian-xiaohei-illustrations/     ← Installable skill directory
  SKILL.md                      ← Claude Code skill entrypoint
  install.sh                    ← Idempotent installer
  settings.json                 ← Default character config
  manifest.json                 ← Universal plugin descriptor
  agents/                       ← Multi-platform agent configs (Codex, Gemini CLI, Hermes, Antigravity)
  scripts/
    generate_image.py           ← Image generation (4 providers, auto-detects key)
    scan_project.py             ← Project context extractor
  references/
    style-dna.md                ← Visual rules
    composition-patterns.md     ← Structure types
    prompt-template.md          ← Generation template
    qa-checklist.md             ← Pass/fail checklist
    characters/
      INDEX.md                  ← All 9 characters + cultural philosophy
      xiaohei.md … al-zill.md   ← One file per character

examples/
  prompts/                      ← 9 ready-to-paste prompts (one per character)
  images/                       ← 8 generic PNGs (9 character PNGs missing — pending)
  prompts.md                    ← Usage scenarios guide
  character-examples.md         ← Character gallery + prompt injections

docs/
  SETUP.md                      ← Provider setup (API keys, free tiers)
  GENERATE.md                   ← Generation workflow reference

README.md
```

---

## Budget & Running Cost

| Service | Plan | Monthly cost | Notes |
|---------|------|-------------|-------|
| GitHub | Free | £0 | Public repo |
| Image generation (Nano Banana / Gemini) | Free tier | £0 | 15 req/min free |
| Image generation (DALL·E / Stability) | Pay-per-use | ~$0.04/image | Owner's API key — not project cost |

**Total: £0/month**

---

## Escalate to Owner If

- API provider breaks the generation scripts (schema change, deprecation)
- Community PR proposes a new character — Zaki approves cultural authenticity
- LinkedIn post drives significant inbound (repo stars, issues, messages) — Zaki responds personally

---

## Decisions Made — Do Not Revisit

- **9 characters, not 1** — each is grounded in a real art tradition, not a cultural caricature. Philosophy in `references/characters/INDEX.md`.
- **4 providers, not 1** — no single provider is universally available. Free tier first (Nano Banana).
- **stdlib Python for 3 of 4 providers** — Stability AI is the only exception (`pip install requests`). Do not add more dependencies.
- **Branch not merged yet** — the README gallery must show character-specific images before main is the public face.
- **"Council of Claude" review pattern** — 2 rounds, 4 parallel agents each. All findings fixed. Do not regress.

---

## Quick Reference

| Task | Action |
|------|--------|
| Generate a character image | Paste prompt from `examples/prompts/0N-*.txt` into Gemini web UI |
| Update README gallery | Ask Claude Code: "Update README gallery with the new image filenames" |
| Merge to main | `git checkout main && git merge claude/skill-plugin-port-ZYCfj && git push` |
| Reprint LinkedIn post | Ask Claude Code: "Reprint the corrected LinkedIn post from the last session" |
| Install the skill locally | Run `ian-xiaohei-illustrations/install.sh` |

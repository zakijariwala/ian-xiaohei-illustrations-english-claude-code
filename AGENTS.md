# AGENTS.md — ian-xiaohei-illustrations-english-claude-code

## Purpose
Open-source Claude Code skill for generating 16:9 hand-drawn article illustrations. The installable artifact is `ian-xiaohei-illustrations/`. Nine culturally-grounded character variants, four image generation providers with auto-detection. Ported and expanded from a Chinese Codex skill.

## Ownership
- Owner: Zaki Jariwala (jariwalazaki@gmail.com)
- Active branch: `claude/read-handover-docs-7dvoD`
- Public repo — all changes are visible to anyone who installs the skill

## Local Contracts
- Installable skill package is `ian-xiaohei-illustrations/` — `SKILL.md` is the Claude Code entrypoint
- `install.sh` must remain idempotent: merges into existing `settings.json` rather than overwriting; user's default character must survive upgrades
- All output must be 16:9 — do not change this aspect ratio
- Provider auto-detection order: `nanobanana` (Gemini 2.5 Flash) → `dalle` (OpenAI `gpt-image-1`, fallback `dall-e-3`) → `imagen` (Imagen 3) → `stability` (SD3)
- Nine characters are fixed and culturally grounded — adding a character requires a full reference file in `references/characters/` and a prompt in `examples/prompts/`; do not add stereotyped or ungrounded characters
- `references/style-dna.md` and `references/qa-checklist.md` are quality contracts — changes require deliberate review
- Published example sets: `examples/images/` (8 images) and `ian-xiaohei-illustrations/assets/examples/` (14 images) — both are canonical

## Work Guidance
- Skill entrypoint: `ian-xiaohei-illustrations/SKILL.md`
- Image generation: `ian-xiaohei-illustrations/scripts/generate_image.py`
- Character definitions: `ian-xiaohei-illustrations/references/characters/`
- Style rules: `ian-xiaohei-illustrations/references/style-dna.md`
- QA checklist: `ian-xiaohei-illustrations/references/qa-checklist.md`
- Multi-platform agent configs: `ian-xiaohei-illustrations/agents/` (openai.yaml, gemini.md, hermes.yaml, antigravity.yaml)
- User-facing docs: `docs/SETUP.md`, `docs/GENERATE.md`

## Verification
- Run `bash ian-xiaohei-illustrations/install.sh` — confirm it completes without error and merges settings.json
- Run `python3 ian-xiaohei-illustrations/scripts/generate_image.py --character xiaohei` — confirm a 16:9 PNG is produced

## Child DOX Index
- `ian-xiaohei-illustrations/AGENTS.md` — installable skill package: SKILL.md contract, scripts, agent configs, install rules
- `ian-xiaohei-illustrations/references/AGENTS.md` — character definitions, style DNA, composition patterns, QA checklist
- `examples/AGENTS.md` — published example images and prompts, naming conventions

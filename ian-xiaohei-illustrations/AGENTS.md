# AGENTS.md — ian-xiaohei-illustrations/ (Installable Skill Package)

## Purpose
The installable Claude Code skill artifact. Users run `install.sh` to deploy this package to their local agent environment. Everything here ships to the end user.

## Ownership
Owned by root AGENTS.md.

## Local Contracts
- `SKILL.md` is the Claude Code skill entrypoint — it defines the skill name, trigger conditions, and the agent's decision flow (read project context → identify cognitive structure → select character → call generate_image.py)
- `install.sh` must remain idempotent: reads existing `settings.json` and merges, never overwrites; user's `default_character` setting must survive upgrades
- `manifest.json` declares the skill's public interface — bump version on any breaking change
- `scripts/generate_image.py` implements provider auto-detection and image generation; all output must be 16:9 PNG; provider alias mapping (`gemini` → `nanobanana`, `openai` → `dalle`, `sd` → `stability`) must be preserved
- `agents/` contains multi-platform configs (openai.yaml, gemini.md, hermes.yaml, antigravity.yaml) — keep these in sync with SKILL.md's intent when the skill behaviour changes

## Work Guidance
- Change skill trigger or decision flow: `SKILL.md`
- Change image generation: `scripts/generate_image.py`
- Change install behaviour: `install.sh`
- Add a platform config: `agents/[platform].[ext]`

## Child DOX Index
- `references/AGENTS.md` — character definitions, style DNA, composition patterns, QA checklist

# AGENTS.md — references/

## Purpose
Source-of-truth reference materials for illustration generation. Agents must read the applicable files here before generating any illustration.

## Ownership
Owned by `ian-xiaohei-illustrations/AGENTS.md`.

## Local Contracts
- `style-dna.md` — visual DNA: line weight, color palette, prohibitions, typography rules. Read before any generation.
- `characters/INDEX.md` — all 9 characters with IDs and cultural origins. Read to select a character.
- `characters/[id].md` — individual character: visual descriptors and prompt injection block. Read the active character's file before generating.
- `composition-patterns.md` — layout patterns for different cognitive structures.
- `prompt-template.md` — canonical prompt structure. Do not deviate from this template.
- `qa-checklist.md` — pre-publish quality gate. Every generated image must pass before being added to `assets/examples/`.
- `xiaohei-ip.md` — IP attribution and origin notes for the Xiaohei character.

## Work Guidance
- Add a new character: create `characters/[id].md` following the existing format; add to `characters/INDEX.md`; create a corresponding prompt in `examples/prompts/`
- Change style rules: edit `style-dna.md`; review all existing example images for compliance
- Change QA gate: edit `qa-checklist.md`; document the reason for the change

# AGENTS.md — examples/

## Purpose
Published reference material for the skill: example illustrations demonstrating style across varied cognitive structures, and ready-to-paste prompts for each of the 9 characters.

## Ownership
Owned by root AGENTS.md.

## Local Contracts
- `images/` — 8 reference illustrations showing the style in action; filenames use `NN-kebab-description.png` format
- `prompts/` — 9 prompt files, one per character (`NN-[character-id]-[concept].txt`); these are the canonical prompt examples for the README and docs
- `prompts.md` — index of all prompts with descriptions; keep in sync with `prompts/` contents
- `character-examples.md` — narrative descriptions of each character in action; update when new characters are added
- `output/` — local generation output (gitignored placeholder); never commit generated images here

## Work Guidance
- New example image: generate via skill, pass QA checklist, add to `images/` with the next sequential number and a descriptive kebab name
- New prompt example: add to `prompts/` and update `prompts.md`

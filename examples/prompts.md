# Prompt Examples

Copy-paste prompts you can hand to your agent. Replace the invocation prefix with
your platform's syntax — `/ian-xiaohei-illustrations` (Claude Code),
`$ian-xiaohei-illustrations` (Codex), or just describe the task to any agent
that has the skill loaded.

For fully worked, per-character examples (with generation commands and prompt
files), see [`character-examples.md`](character-examples.md).

## Planning only (shot list)

```text
/ian-xiaohei-illustrations Don't generate images yet.
Analyze where this article would benefit from illustration and output a shot list
of about 5 images. For each image, specify:
- Which paragraph it follows
- The image's theme
- Core meaning
- Structure type
- What the character is doing in the image
- Suggested elements
- Suggested annotation words (English)

<paste article>
```

## Body illustrations for an article

```text
/ian-xiaohei-illustrations Generate 4 absurd body illustrations for the article below.
Requirements: 16:9 landscape, pure white background, black hand-drawn line art,
sparse red/orange/blue handwritten English annotations.
Each image explains only one core structure. No PPT infographics, no cute cartoons.

<paste article>
```

## Long-form illustration strategy

```text
/ian-xiaohei-illustrations Plan the illustrations for this long article.
Don't distribute images evenly — pick only cognitive anchors: core judgments,
input-output loops, before/after contrasts, common pitfalls, handoff paths.
Default 6–8 images. Output a shot list first; don't generate images yet.

<paste article>
```

## One image for a single idea

```text
/ian-xiaohei-illustrations Generate one 16:9 body illustration for this idea:

Trust isn't shouted — it's laid down one small piece of evidence at a time.

The image should be absurd but clean. The character must carry the core action.
Use at most 5 short English annotations.
```

## Workflow theme

```text
/ian-xiaohei-illustrations Generate one image for "turning a single raw material
into three kinds of content: reach, trust, and conversion."
Don't draw a formal flowchart, and don't reuse the old "one fish, many dishes" case.
Invent a fresh low-tech metaphor and let the character drive the core action.
```

## Edit: remove a title

```text
/ian-xiaohei-illustrations Edit this image for me.
Remove the top-left "Workflow" title and its underline. Keep everything else
unchanged. Don't add any new text or objects.
```

## Edit: make the character more involved

```text
/ian-xiaohei-illustrations This image is on the right track, but the character
looks like decoration. Keep the core meaning, but regenerate so the character is
the one actually driving the structure. Make it a little stranger, still pure
white, clean, and sparse on text.
```

## Generate a style sample set

```text
/ian-xiaohei-illustrations Output 5 body illustrations on different themes.
Cover: information overload, product validation, content compounding,
the one-person company, and building trust.
Generate each one separately — don't combine them into a single image.
```

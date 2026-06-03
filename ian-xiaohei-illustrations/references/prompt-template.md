# Image Generation Prompt Template

Generate each image separately. Replace the variables with content from the article — never combine multiple images into one.

**Labels** default to English (short, 1–4 words each). To use the original Chinese-annotation look, swap the label line and the "handwritten English annotations" phrase to Chinese.

**Character** defaults to Xiaohei. To use a different cultural IP, replace the `IP character required:` block with the `Prompt Injection` text from `references/characters/<id>.md`. Or use the `--character` flag in the generation script — it replaces the block automatically.

---

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
{Paste the "Prompt Injection" block from references/characters/<id>.md here.
 Default (Xiaohei): Xiaohei (小黑), a small solid-black absurd creature with white dot
 eyes, tiny thin legs, blank serious expression, slightly uneven hand-drawn ink-blob body.
 Xiaohei must perform the core conceptual action, not decorate the scene. Serious,
 deadpan, slightly bizarre. Not cute.}

Theme:
{illustration theme from the article}

Structure type:
{Workflow / System Slice / Before-After Contrast / Character State / Conceptual Metaphor / Method Layers / Map Route / Mini Comic Panels}

Core idea:
{the core meaning this image must convey}

Composition:
{specific scene: where the character is, what the character is doing, what the main objects are, how information flows}

Suggested elements:
{element 1} / {element 2} / {element 3} / {element 4}

Handwritten labels (English, short):
{label 1} / {label 2} / {label 3} / {label 4} / {optional label 5}

Color use:
Black for main line art and the IP character. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of the canvas. Preserve at least 35% blank white space. Use at most 5–8 short handwritten labels, spelled correctly in English. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.
```

---

## Swapping Characters — Examples

**Via generation script (auto-injects the right block):**

```bash
# American character
python3 scripts/generate_image.py --character the-smudge --prompt-file prompt.txt --out 01.png

# Japanese character
python3 scripts/generate_image.py --character chibi-kage --prompt-file prompt.txt --out 01.png

# European character (alias)
python3 scripts/generate_image.py --character le-bloc --prompt-file prompt.txt --out 01.png

# See all characters
python3 scripts/generate_image.py --list-characters
```

**Manually in the prompt** — replace the `IP character required:` block with the character's `Prompt Injection` text:

```text
IP character required:
The Smudge, a chunky solid-black silhouette figure with two slightly asymmetric white oval
eyes, thick stubby legs, and one arm pointing or holding a clipboard. Proportionally larger
hands and feet — built for hauling. Body has mid-century American editorial cartoon and WPA
poster worker quality — bold, functional, no-nonsense. Does the core conceptual action
because it showed up and that's what you do. No complaints. Workmanlike. Not cute.
```

---

## Image Editing Prompts

Remove a top-left title:

```text
Edit the provided image. Remove only the handwritten title "{text to remove}" and its
underline from the top-left corner. Fill that area with the same clean white background,
matching the surrounding blank paper. Preserve everything else exactly: characters, labels,
paths, line style, composition, aspect ratio, and image quality. Do not add any new text
or objects.
```

Increase the absurdity / make the character more central:

```text
Regenerate this illustration with the same core meaning and simple layout, but make the
IP character more central to the conceptual action. The character should be doing the
strange work that explains the idea, not standing beside the diagram. Keep it clean,
sparse, hand-drawn, and not cute.
```

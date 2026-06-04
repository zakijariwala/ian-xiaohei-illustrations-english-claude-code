# Character IP Examples

One fully worked example per character variant. Each example includes:
- The article concept being illustrated
- The shot list entry (planning output)
- The complete generation-ready prompt
- The generation command
- The expected save path

All examples follow the same visual rules: 16:9, pure white, hand-drawn, lots of blank space, one structure per image. Only the IP character and cultural line tradition change.

---

## Table of Contents

| # | Character | Culture | Concept |
|---|-----------|---------|---------|
| 1 | [Xiaohei (小黑)](#1-xiaohei) | Chinese / East Asian | AI content workflow — one input, many outputs |
| 2 | [Chibi Kage (小影)](#2-chibi-kage) | Japanese | Second brain — scattered notes become a query-able net |
| 3 | [Kaala (काला)](#3-kaala) | South / Southeast Asian | Async systems — four streams handled in parallel |
| 4 | [Kali Tikka](#4-kali-tikka) | Indian (block-print / folk art) | One-to-many reuse — one carved block, many prints |
| 5 | [Le Bloc / Der Fleck](#5-le-bloc) | European | Bureaucratic pipeline — absurd precision |
| 6 | [The Smudge](#6-the-smudge) | American | Deployment — the build that has to ship |
| 7 | [Dudu](#7-dudu) | West African / Afrofuturist | Data pipeline — arm becomes the filter |
| 8 | [El Manchón](#8-el-manchon) | Latin American | Community distribution — content as collective labor |
| 9 | [Al-Zill (الظل)](#9-al-zill) | Middle Eastern / Arabic | Long-term compounding — patience as strategy |

---

## 1. Xiaohei

**Character:** Xiaohei (小黑) — Chinese / East Asian
**Article concept:** AI content workflow — one raw input fed into a strange machine produces five distinct output formats simultaneously
**Structure type:** Workflow (Conceptual Metaphor)

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section explaining how one recording becomes a newsletter, thread, post, summary, and clip |
| **Theme** | One input → many outputs via a strange compressor machine |
| **Core idea** | A single raw recording goes into a black box; Xiaohei cranks it and five different format strips come out the other side |
| **Structure type** | Workflow with Conceptual Metaphor overlay |
| **What Xiaohei does** | Feeds a single crumpled audio tape into a strange hand-cranked press; five clean format strips come out labeled on the right |
| **Suggested elements** | Crumpled tape reel · hand-crank press box · five output strips · one orange input arrow |
| **Annotations** | one recording / crank it / newsletter / thread / clip |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Xiaohei (小黑), a small solid-black absurd creature with white dot eyes, tiny thin legs,
blank serious expression, slightly uneven hand-drawn ink-blob body. Xiaohei must perform
the core conceptual action, not decorate the scene. Serious, deadpan, slightly bizarre.
Not cute. Like a Chinese ink-brush mark that grew limbs and got a job.

Theme:
One raw recording fed into a hand-crank press produces five distinct content formats.

Structure type:
Workflow with Conceptual Metaphor overlay.

Core idea:
A single crumpled audio tape goes in on the left; Xiaohei feeds it into a strange
hand-cranked press box and turns the crank; five clean labeled format strips emerge
from the right side of the machine. The press is low-tech, slightly broken-looking,
but clearly works.

Suggested elements:
crumpled tape reel / hand-crank press box / five output strips fanning out / one orange input arrow

Handwritten labels (English, short):
one recording / crank it / newsletter / thread / clip

Color use:
Black for Xiaohei, the press, tape, and output strips. Orange for the single input
arrow from tape to machine. Red for the label on the most important output strip.
Blue for secondary format labels.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 5 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type
on the image. Do not make it a formal diagram, course slide, or dense explainer.
Invent a fresh visual metaphor — do not reuse known Xiaohei compositions. Clear but
not instructional, interesting but not childish, strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character xiaohei \
  --prompt-file examples/prompts/01-xiaohei-content-press.txt \
  --out examples/output/01-xiaohei-content-press.png
```

**Save path:** `examples/output/01-xiaohei-content-press.png`

---

## 2. Chibi Kage

**Character:** Chibi Kage (小影) — Japanese
**Article concept:** Building a second brain — scattered notes, links, and highlights slowly weave into one connected, query-able knowledge net
**Structure type:** Conceptual Metaphor

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section explaining how the AI connects disparate notes into a retrievable web |
| **Theme** | A paper-spirit weaving scattered note-scraps into a connected net on an ancient hand-loom |
| **Core idea** | Scattered notes drift in; Chibi Kage weaves them on a loom into one net; pulling one thread lifts a linked cluster |
| **Structure type** | Conceptual Metaphor |
| **What Chibi Kage does** | Operates an ancient hand-loom with one sleeve-covered arm; note-scraps feed in from the left and emerge as a woven net on the right; one thread is being pulled, lifting a cluster |
| **Suggested elements** | Drifting note-scraps · ancient hand-loom · woven net of small cards · one thread being pulled |
| **Annotations** | scattered notes / woven into one / pull any thread / linked cluster |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Chibi Kage (小影), a flat black silhouette paper-spirit with a single large white oval
eye, no visible feet (floats slightly above the ground line), one small sleeve-covered
arm. Body has clean kirie cut-paper edges and solid ukiyo-e woodblock ink quality. Chibi
Kage performs the core action with ancient ceremonial seriousness — like a yokai assigned
to run a Kanban board. Never cute. Quietly unsettling. No feet, just presence.

Theme:
A paper-spirit weaving scattered note-scraps into a connected, pull-able knowledge net
on an ancient hand-loom.

Structure type:
Conceptual Metaphor.

Core idea:
Loose note-scraps drift in from the left. Chibi Kage floats at the center operating
an ancient narrow hand-loom with one sleeve-covered arm, feeding the scraps in. From
the right side of the loom emerges a small woven net made of connected note-cards. One
thread of the net is being gently pulled upward, and a small cluster of linked cards
lifts with it. The right third of the image is mostly empty and calm.

Suggested elements:
drifting note-scraps / ancient narrow hand-loom / woven note-card net / one pulled thread lifting a cluster

Handwritten labels (English, short):
scattered notes / woven into one / pull any thread / linked cluster

Color use:
Black for Chibi Kage, the loom, and the woven net. Orange for the input flow of note-scraps
toward the loom. Red for the label on the pulled thread ("pull any thread"). Blue for the
secondary cluster label.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Do not make it a formal diagram. Invent a fresh visual metaphor. Clear but not
instructional, strange but clean. The character must float — no feet touching the ground.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character chibi-kage \
  --prompt-file examples/prompts/02-chibi-kage-knowledge-loom.txt \
  --out examples/output/02-chibi-kage-knowledge-loom.png
```

**Save path:** `examples/output/02-chibi-kage-knowledge-loom.png`

---

## 3. Kaala

**Character:** Kaala (काला) — South / Southeast Asian
**Article concept:** Managing four async work streams at once without losing context — the state of a solo founder running product, sales, writing, and operations simultaneously
**Structure type:** Character State

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section describing the cognitive load of switching contexts across four parallel tracks |
| **Theme** | Four arms, four streams — no switching cost, no dropped state |
| **Core idea** | Kaala holds, monitors, and acts on four separate work streams simultaneously with absolute calm |
| **Structure type** | Character State with System Slice |
| **What Kaala does** | Stands at the center with four thin arms extended; each arm holds or operates a different stream (writing, product, sales, ops); expression completely flat |
| **Suggested elements** | Four labeled stream objects · four thin arms in action · calm central figure |
| **Annotations** | product / writing / sales / ops / all at once |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Kaala (काला), a deep charcoal silhouette figure with almond-shaped white eyes, a small
white bindi dot on the forehead, and four very thin arms — each performing a different
part of the core conceptual action simultaneously. Body has hand-painted temple-frieze
and kolam line quality. Kaala operates with absolute calm and methodical grace, like a
deity assigned to system maintenance. Never cute. Four tasks at once, zero expression
change.

Theme:
A solo founder managing four parallel work streams simultaneously with no context-switching
cost — product, writing, sales, and operations, all at once.

Structure type:
Character State with System Slice.

Core idea:
Kaala stands at the center of the image. Four thin arms radiate outward, each extended
toward a different simple object representing a work stream: a small document (writing),
a tiny product screen (product), a handshake symbol (sales), a gear (ops). Each arm is
in mid-action — holding, adjusting, or operating. The body is completely still and the
expression is blank. Nothing is being dropped.

Suggested elements:
four radiating thin arms / small document / tiny gear / handshake shape / product card

Handwritten labels (English, short):
product / writing / sales / ops / all at once

Color use:
Black for Kaala and all four stream objects. Orange for a subtle circular flow line
connecting the four streams around the figure. Red for the central "all at once" label.
Blue for the secondary stream labels (product, ops).

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 5 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. Fresh metaphor. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character kaala \
  --prompt-file examples/prompts/03-kaala-four-streams.txt \
  --out examples/output/03-kaala-four-streams.png
```

**Save path:** `examples/output/03-kaala-four-streams.png`

---

## 4. Kali Tikka

**Character:** Kali Tikka — Indian (block-print / folk art)
**Article concept:** Reuse — carve one good idea once, then stamp it into many consistent outputs
**Structure type:** One-to-Many Reuse

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section arguing that one well-made template beats re-doing the work each time |
| **Theme** | One carved block, many identical prints — the block-print logic of reuse |
| **Core idea** | Kali Tikka holds a single carved printing block and stamps a row of identical marks across the canvas |
| **Structure type** | One-to-Many Reuse |
| **What Kali Tikka does** | Presses one carved block down, lifting it to reveal a clean repeating motif; a row of identical stamped prints trails to the right |
| **Suggested elements** | One carved printing block · a row of identical stamped motifs · fresh ink edge · one print still half-pressed |
| **Annotations** | carve once / press / again / again |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Kali Tikka, an angular black wood-block-print-silhouette figure with a small white
registration dot between the eyes (a block-print alignment mark), arms gesturing boldly —
one raised, one positioning a tool or stamp. Body has bold Madhubani and hand-stamp
textile-print quality: slightly rough, confidently angular, repeating motifs. Kali Tikka
is an inventive improviser — finding the bold, direct, decisive way to make the structure
work, straight-faced and unbothered. Not cute. Composes the action like stamping a
textile, one confident mark at a time.

Theme:
One carved block, many identical prints — the logic of making something once and reusing
it everywhere.

Structure type:
One-to-Many Reuse.

Core idea:
Kali Tikka holds a single carved printing block in one raised arm and presses it down with
the other onto a long horizontal strip. Where it has already pressed, a row of identical
clean motifs marches off to the right. The block is just lifting off the newest print, a
small ink edge still connecting them. One print further right is only half-stamped, mid-
press. Expression: completely flat. Carve once, press forever.

Suggested elements:
one carved printing block / row of identical stamped motifs / fresh ink edge lifting off /
one half-pressed print / orange arrow showing the repeat direction

Handwritten labels (English, short):
carve once / press / again / again

Color use:
Black for Kali Tikka, the block, and the printed motifs. Orange for the small arrow showing
the repeat direction. Red for the "carve once" label by the block. Blue for the "again"
notes along the repeated prints.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. Fresh metaphor. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character kali-tikka \
  --prompt-file examples/prompts/04-kali-tikka-block-print.txt \
  --out examples/output/04-kali-tikka-block-print.png
```

**Save path:** `examples/output/04-kali-tikka-block-print.png`

---

## 5. Le Bloc

**Character:** Le Bloc / Der Fleck — European
**Article concept:** Navigating a bureaucratic approval process — every step is documented, correct, and ultimately meaningless
**Structure type:** Map / Route

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section describing how approval pipelines create compliance theater without producing real decisions |
| **Theme** | A perfectly documented path to nowhere |
| **Core idea** | Le Bloc walks a winding path of numbered stamp-boxes, checking each one correctly; the path loops back to where it started |
| **Structure type** | Map / Route |
| **What Le Bloc does** | Walks the route, stamp in hand, checking each box with bureaucratic precision; expression blank; the final box connects back to the first |
| **Suggested elements** | Winding path of stamp-boxes · checked marks · loop-back arrow · one tiny stamp |
| **Annotations** | step 1 / approved / step 4 / back to step 1 |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Le Bloc (also known as Der Fleck), an irregular ink-blot silhouette figure with slightly
soft bled-ink edges and a single round white monocle eye. Body has Swiss poster and
Bauhaus geometric reduction quality — clean, purposeful, slightly translucent at the
edges like a half-spent stamp. Le Bloc performs the core action with bureaucratic
precision and existential awareness — it knows the task is absurd and does it correctly
anyway. Dry. Formal. Melancholic. Not cute.

Theme:
A winding bureaucratic approval path where every box is checked correctly and the route
loops back to the beginning.

Structure type:
Map / Route.

Core idea:
A winding path of 4–5 small rectangular stamp-boxes snakes across the canvas. Each box
has a small checkmark inside it. Le Bloc walks the path, holding a tiny stamp, positioned
at box 4. A small orange arrow from the last box curves back and points to box 1. The
loop is complete. Nothing was decided. Everything was documented.

Suggested elements:
winding path of stamp-boxes / checkmarks / Le Bloc with tiny stamp / loop-back arrow

Handwritten labels (English, short):
step 1 / approved / step 4 / back to step 1

Color use:
Black for Le Bloc, the path, the boxes, and checkmarks. Orange for the loop-back arrow
from the last box to the first. Red for the "back to step 1" label — the punchline.
Blue for "approved" labels on the intermediate boxes.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal flowchart. The humor is in the loop — make it subtle, not cartoonish.
Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character le-bloc \
  --prompt-file examples/prompts/05-le-bloc-approval-loop.txt \
  --out examples/output/05-le-bloc-approval-loop.png
```

**Save path:** `examples/output/05-le-bloc-approval-loop.png`

---

## 6. The Smudge

**Character:** The Smudge — American
**Article concept:** Shipping a build — the deployment pipeline that has to go out tonight no matter what
**Structure type:** Workflow

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section on why "done" means deployed, not merged |
| **Theme** | The build gets on the truck. No exceptions. |
| **Core idea** | The Smudge loads a build crate onto a flatbed truck — the crate is slightly too big, the truck is slightly too small, it fits anyway |
| **Structure type** | Workflow |
| **What The Smudge does** | Pushes an oversized build crate onto a small flatbed truck; one hand on the crate, one hand on the clipboard; expression blank; the truck is already moving |
| **Suggested elements** | Oversized crate labelled "v2.1" · small flatbed truck · clipboard · motion lines |
| **Annotations** | build / too big? / ships anyway / done means shipped |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
The Smudge, a chunky solid-black silhouette figure with two slightly asymmetric white
oval eyes, thick stubby legs, and one arm pointing or holding a clipboard. Proportionally
larger hands and feet than typical — built for hauling. Body has mid-century American
editorial cartoon and WPA poster worker quality — bold, functional, no-nonsense. The
Smudge does the core conceptual action because it showed up and that's what you do when
you show up. No complaints. Workmanlike. Not cute.

Theme:
Loading an oversized build crate onto a small flatbed truck that is already moving.

Structure type:
Workflow.

Core idea:
Center-left: The Smudge pushes an oversized rectangular crate (labeled "v2.1" in small
hand-drawn text) onto the back of a small flatbed truck. The crate is visibly too big —
it overhangs slightly. The Smudge has one hand on the crate and holds a clipboard under
the other arm. The truck has small motion lines showing it's already rolling right. The
Smudge's expression is completely flat. The right side of the image is empty road.

Suggested elements:
oversized crate labeled v2.1 / small flatbed truck / clipboard / motion lines on truck

Handwritten labels (English, short):
build / too big? / ships anyway / done means shipped

Color use:
Black for The Smudge, the crate, the truck, and the clipboard. Orange for the motion
lines on the truck (it's moving). Red for "ships anyway" — the key statement. Blue for
"done means shipped" as the secondary principle label.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. The humor is in the size mismatch — subtle, not slapstick.
Workmanlike energy. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character the-smudge \
  --prompt-file examples/prompts/06-the-smudge-ship-it.txt \
  --out examples/output/06-the-smudge-ship-it.png
```

**Save path:** `examples/output/06-the-smudge-ship-it.png`

---

## 7. Dudu

**Character:** Dudu — West African / Afrofuturist
**Article concept:** Data pipeline — raw events stream in, Dudu's arm becomes the filter, and only signal comes out the other side
**Structure type:** System Slice

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section explaining how the pipeline separates meaningful signals from noise |
| **Theme** | The arm that becomes the filter — body and tool are the same thing |
| **Core idea** | A stream of raw data events flows in from the left; Dudu extends one arm across the flow and the arm morphs into a geometric filter mesh; only clean signals pass through to the right |
| **Structure type** | System Slice |
| **What Dudu does** | Stands to the side, one elongated arm extended horizontally across the data stream; the arm transforms mid-length into a woven geometric mesh filter; clean dots emerge on the right; noise dissipates |
| **Suggested elements** | Incoming raw data dots (varied sizes) · elongated arm becoming mesh filter · clean signal dots on right |
| **Annotations** | raw events / arm is the filter / signal / noise gone |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Dudu, a sleek elongated black silhouette figure with a white geometric diamond eye.
Dudu's arms can extend and morph into the tool being used — arm becomes lever, funnel,
or path — no separation between worker and work. Body has Adinkra symbol and
kente-geometry line quality: confident, geometric, each shape carries weight. Dudu
performs the core action in alignment with a larger pattern — ancient rhythm, futuristic
system. Unhurried. Purposeful. Not cute.

Theme:
A data pipeline where the character's arm extends across the stream and becomes the
filter itself — body and tool are one.

Structure type:
System Slice.

Core idea:
Left side: a loose flow of raw data events (dots and small shapes of varied sizes) moves
right. Dudu stands slightly above-center, one elongated arm extended horizontally into
the flow. Midway along the arm, it transforms into a geometric Adinkra-pattern mesh grid.
On the right side of the mesh, only small uniform clean dots emerge — the signal. The
irregular shapes from the left are gone. Dudu's expression is a single diamond eye, still.

Suggested elements:
varied raw data dots flowing right / elongated arm morphing into geometric mesh / clean uniform dots on right

Handwritten labels (English, short):
raw events / arm is the filter / signal / noise gone

Color use:
Black for Dudu, the arm-filter, and all data elements. Orange for the incoming raw data
flow arrow. Red for "noise gone" near the dissipated shapes. Blue for "signal" on the
clean dots emerging right.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. The key visual is the arm becoming the mesh — make that
transformation clear and geometric. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character dudu \
  --prompt-file examples/prompts/07-dudu-arm-filter.txt \
  --out examples/output/07-dudu-arm-filter.png
```

**Save path:** `examples/output/07-dudu-arm-filter.png`

---

## 8. El Manchón

**Character:** El Manchón — Latin American
**Article concept:** Content distribution as collective labor — one piece of content reaches many hands, each person carrying it one step further
**Structure type:** Map / Route

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section explaining how community sharing extends content reach beyond any single channel |
| **Theme** | A piece of content passed hand to hand along a winding path — each carrier takes it one step further |
| **Core idea** | El Manchón carries a folded content sheet at the front of a winding path; behind, small silhouette figures each hold the same sheet, passing it forward; the path extends off the right edge |
| **Structure type** | Map / Route |
| **What El Manchón does** | Leads the route, leaning forward with weight on the front foot, holding a folded content sheet up in the air — the posture of someone who means it |
| **Suggested elements** | Folded content sheet · winding path · El Manchón at front · small silhouettes passing it behind |
| **Annotations** | one post / carried forward / by many / further than you planned |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
El Manchón, a fluid black silhouette figure with slightly organic flowing edges, white
crescent eyes (slight upward curve), and a dynamic posture — slight forward lean, weight
on one foot, always mid-action. Body has Mexican grabado linocut print quality: slightly
rough, bold, high-contrast marks. El Manchón performs the core action with the physical
commitment of a muralist — labor as dignity, full body presence. More expressive in
posture than other IPs, but face stays deadpan. Not cute. Here to do the work.

Theme:
Content distribution as collective labor — one folded sheet carried along a winding path,
passed forward by many hands, traveling further than any single person could take it.

Structure type:
Map / Route.

Core idea:
A winding path runs left to right across the canvas. El Manchón leads at the front-left,
leaning forward with weight on the front foot, holding a folded content sheet raised
slightly. Behind, along the winding path, 3–4 smaller simplified silhouette figures each
hold the same folded sheet, spaced apart. The path extends and slightly disappears off
the right edge of the canvas — implying it keeps going.

Suggested elements:
folded content sheet / winding path / El Manchón at front / 3–4 silhouettes carrying it behind

Handwritten labels (English, short):
one post / carried forward / by many / further than you planned

Color use:
Black for El Manchón, all silhouettes, and the content sheet. Orange for the path line
and the direction of movement. Red for "further than you planned" at the right edge —
the payoff. Blue for "by many" near the middle figures.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. The energy is communal momentum — El Manchón's forward lean
should feel like it's pulling the whole chain. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character el-manchon \
  --prompt-file examples/prompts/08-el-manchon-content-chain.txt \
  --out examples/output/08-el-manchon-content-chain.png
```

**Save path:** `examples/output/08-el-manchon-content-chain.png`

---

## 9. Al-Zill

**Character:** Al-Zill (الظل) — Middle Eastern / Arabic
**Article concept:** Compounding returns — small consistent actions taken for long enough that the result becomes inevitable
**Structure type:** Conceptual Metaphor

### Shot List Entry

| Field | Value |
|-------|-------|
| **Paragraph placement** | After the section arguing that the biggest mistake is stopping just before compounding kicks in |
| **Theme** | A tower built one stone at a time — Al-Zill has been placing stones since before you arrived |
| **Core idea** | A tall narrow tower of small stones stands on the right; Al-Zill stands beside it, sleeve raised as if just placing the most recent stone; the tower is already very tall; small date markers on some stones show the long timeline |
| **Structure type** | Conceptual Metaphor |
| **What Al-Zill does** | Stands beside the tower, tall and still, one sleeve raised — the action is implied, not shown; presence communicates that this has been happening for a very long time |
| **Suggested elements** | Tall narrow stone tower · Al-Zill beside it with sleeve raised · small date labels on some stones |
| **Annotations** | day 1 / year 2 / still going / inevitable |

### Generation Prompt

```text
Generate one standalone 16:9 horizontal article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines.
Lots of empty white space. Sparse red/orange/blue handwritten English annotations. Clean
absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex
background, no commercial vector style, no PPT infographic look, no cute mascot poster,
no children's illustration, no realistic UI.

IP character required:
Al-Zill (الظل), a tall thin black silhouette figure with a tapered calligraphic top (like
an alif upstroke), narrow white almond-shaped eyes, and long sleeves that drape over the
hands (a shadow-puppet device). Body has Islamic geometric pattern precision and Karagöz
shadow-puppet flatness — pure 2D, mathematically clean, ornament as structure. Al-Zill
builds the core action from exact, repeating units, the way a geometric pattern is
constructed; a slight tilt of the tall form reads as a deliberate move. Precise.
Architectural. Dry. Not cute.

Theme:
A tower built one stone at a time, over a very long period, by a figure who has been
at it since before the viewer arrived.

Structure type:
Conceptual Metaphor.

Core idea:
Right-center: a tall, narrow tower of small stacked rectangular stones. The tower is
already impressively tall — it reaches toward the top of the frame. Al-Zill stands
beside it on the right, tall and still, one sleeve raised as if the most recent stone
was just placed. Some stones have tiny hand-drawn date labels ("day 1", "year 2") at
different heights. The left two-thirds of the canvas is mostly empty. The tower and
Al-Zill together occupy the right third. The image is calm and geometric.

Suggested elements:
tall narrow stone tower / Al-Zill beside it with one sleeve raised / small date labels at different heights

Handwritten labels (English, short):
day 1 / year 2 / still going / inevitable

Color use:
Black for Al-Zill and the entire tower. Orange for a subtle vertical arrow beside the
tower indicating upward accumulation. Red for "inevitable" near the top of the tower —
the conclusion. Blue for the small date labels embedded in the stones.

Constraints:
One image explains only one core structure. Keep the main subject around 40%–60% of
the canvas. Preserve at least 35% blank white space. Use at most 4 short handwritten
labels. Do not write a title in the top-left corner. Do not write the structure type.
Not a formal diagram. The image should feel patient and inevitable — not motivational,
not urgent. Al-Zill's hands must not be visible. Strange but clean.
```

### Generation Command

```bash
python3 ian-xiaohei-illustrations/scripts/generate_image.py \
  --character al-zill \
  --prompt-file examples/prompts/09-al-zill-compounding.txt \
  --out examples/output/09-al-zill-compounding.png
```

**Save path:** `examples/output/09-al-zill-compounding.png`

---

## Running All Examples

```bash
cd ian-xiaohei-illustrations

# Generate all 9 examples (requires at least one image provider key)
export GEMINI_API_KEY="your-key"   # or OPENAI_API_KEY / STABILITY_API_KEY

python3 scripts/generate_image.py --character xiaohei    --prompt-file ../examples/prompts/01-xiaohei-content-press.txt    --out ../examples/output/01-xiaohei-content-press.png
python3 scripts/generate_image.py --character chibi-kage --prompt-file ../examples/prompts/02-chibi-kage-knowledge-loom.txt --out ../examples/output/02-chibi-kage-knowledge-loom.png
python3 scripts/generate_image.py --character kaala      --prompt-file ../examples/prompts/03-kaala-four-streams.txt        --out ../examples/output/03-kaala-four-streams.png
python3 scripts/generate_image.py --character kali-tikka --prompt-file ../examples/prompts/04-kali-tikka-block-print.txt   --out ../examples/output/04-kali-tikka-block-print.png
python3 scripts/generate_image.py --character le-bloc    --prompt-file ../examples/prompts/05-le-bloc-approval-loop.txt     --out ../examples/output/05-le-bloc-approval-loop.png
python3 scripts/generate_image.py --character the-smudge --prompt-file ../examples/prompts/06-the-smudge-ship-it.txt        --out ../examples/output/06-the-smudge-ship-it.png
python3 scripts/generate_image.py --character dudu       --prompt-file ../examples/prompts/07-dudu-arm-filter.txt           --out ../examples/output/07-dudu-arm-filter.png
python3 scripts/generate_image.py --character el-manchon --prompt-file ../examples/prompts/08-el-manchon-content-chain.txt  --out ../examples/output/08-el-manchon-content-chain.png
python3 scripts/generate_image.py --character al-zill    --prompt-file ../examples/prompts/09-al-zill-compounding.txt       --out ../examples/output/09-al-zill-compounding.png
```

Output images land in `examples/output/`. See [docs/SETUP.md](../docs/SETUP.md#image-generation-setup) for key setup.

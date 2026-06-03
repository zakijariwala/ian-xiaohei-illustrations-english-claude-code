# Character IP Index

All available IP characters for Ian Xiaohei Illustrations. Each file contains the
character's visual descriptors, personality, and a ready-to-inject prompt block.

Default character: **xiaohei**

---

| ID | Display Name | Culture | File |
|----|-------------|---------|------|
| `xiaohei` | Xiaohei (小黑) | Chinese / East Asian | `xiaohei.md` |
| `chibi-kage` | Chibi Kage (小影) | Japanese | `chibi-kage.md` |
| `kaala` | Kaala (काला) | South / Southeast Asian | `kaala.md` |
| `kali-tikka` | Kali Tikka | Indian (street / vernacular) | `kali-tikka.md` |
| `le-bloc` | Le Bloc / Der Fleck | European | `le-bloc.md` |
| `the-smudge` | The Smudge | American | `the-smudge.md` |
| `dudu` | Dudu | West African / Afrofuturist | `dudu.md` |
| `el-manchon` | El Manchón | Latin American | `el-manchon.md` |
| `al-zill` | Al-Zill (الظل) | Middle Eastern / Arabic | `al-zill.md` |

---

## Shared IP Contract

All characters follow the same rules regardless of cultural identity:

- **Hand-drawn quality** — each has a specific cultural line tradition (ink-brush, woodblock, kolam, grabado, Adinkra, shadow-puppet, etc.)
- **Deadpan expression** — never cute, never mugging, never purely decorative
- **Structurally essential** — remove the character and the core metaphor should collapse
- **Absurd worker** — seriously performing something slightly nonsensical but coherent
- **One image, one structure** — the character carries the core action; everything else serves that action

## Selecting a Character

**In a skill prompt:**
```text
Use character: the-smudge
```

**Via the generation script:**
```bash
python3 scripts/generate_image.py --character the-smudge --prompt-file prompt.txt --out img.png
```

**In a prompt template**, replace the `IP character required:` block with the character's
`Prompt Injection` text from its file in this directory.

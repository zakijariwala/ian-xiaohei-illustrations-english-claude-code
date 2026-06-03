#!/usr/bin/env python3
"""
Image generation bindings for the Ian Xiaohei Illustrations skill.

Generates one illustration from a text prompt using whichever image model is
available, and saves a PNG. Designed to be platform-agnostic: it works from
Claude Code, Codex, Gemini CLI, or a plain shell, as long as one provider's
API key is present in the environment.

Supported providers
--------------------
  nanobanana | gemini   Google Gemini 2.5 Flash Image ("Nano Banana")
  dalle      | openai    OpenAI Images (gpt-image-1, falls back to dall-e-3)
  imagen                 Google Imagen 3 (via the Gemini API)
  stability  | sd        Stability AI Stable Image (SD3)

Provider auto-detection (when --provider is omitted) picks the first one whose
API key is set, in this order: nanobanana, dalle, imagen, stability.

Environment variables (API keys)
--------------------------------
  GEMINI_API_KEY or GOOGLE_API_KEY   -> nanobanana, imagen
  OPENAI_API_KEY                     -> dalle
  STABILITY_API_KEY                  -> stability

Usage
-----
  python3 generate_image.py --prompt-file prompt.txt --out 01-topic.png
  python3 generate_image.py --provider dalle --prompt "..." --out img.png
  echo "..." | python3 generate_image.py --out img.png
  python3 generate_image.py --list-providers
Characters
----------
  Use --character <id> to swap the IP character. Default: xiaohei.
  Available IDs: xiaohei, chibi-kage, kaala, kali-tikka, le-bloc,
                 the-smudge, dudu, el-manchon, al-zill
  Use --list-characters to see all characters and their cultures.

  The character's "Prompt Injection" block is extracted from
  references/characters/<id>.md and spliced into the prompt, replacing
  the default Xiaohei block (if present) or appended before the theme.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

# 16:9 sizes per provider (closest supported landscape ratio).
OPENAI_GPT_IMAGE_SIZE = "1536x1024"   # gpt-image-1 landscape
OPENAI_DALLE3_SIZE = "1792x1024"      # dall-e-3 landscape

PROVIDER_ALIASES = {
    "nanobanana": "nanobanana",
    "nano-banana": "nanobanana",
    "gemini": "nanobanana",
    "dalle": "dalle",
    "dall-e": "dalle",
    "openai": "dalle",
    "imagen": "imagen",
    "stability": "stability",
    "sd": "stability",
    "stable-diffusion": "stability",
}

# Detection order: (canonical provider, [env keys that enable it])
DETECT_ORDER = [
    ("nanobanana", ["GEMINI_API_KEY", "GOOGLE_API_KEY"]),
    ("dalle", ["OPENAI_API_KEY"]),
    ("imagen", ["GEMINI_API_KEY", "GOOGLE_API_KEY"]),
    ("stability", ["STABILITY_API_KEY"]),
]


def _first_env(*names):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    return None


def _http_json(url, payload, headers, timeout=180):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise RuntimeError(f"HTTP {e.code} from {url}:\n{body}") from None


def available_providers():
    """Return list of canonical providers whose API key is present."""
    found = []
    for provider, keys in DETECT_ORDER:
        if any(os.environ.get(k) for k in keys) and provider not in found:
            found.append(provider)
    return found


def detect_provider():
    found = available_providers()
    if not found:
        raise RuntimeError(
            "No image provider API key found. Set one of:\n"
            "  GEMINI_API_KEY / GOOGLE_API_KEY  (Nano Banana / Imagen)\n"
            "  OPENAI_API_KEY                   (DALL-E)\n"
            "  STABILITY_API_KEY                (Stability)"
        )
    return found[0]


# ---- Provider implementations: each returns raw PNG/image bytes ----

def gen_nanobanana(prompt):
    key = _first_env("GEMINI_API_KEY", "GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY not set for Nano Banana.")
    model = os.environ.get("NANOBANANA_MODEL", "gemini-2.5-flash-image-preview")
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    result = _http_json(url, payload, {"Content-Type": "application/json"})
    for cand in result.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(f"No image returned by Nano Banana. Raw response:\n{json.dumps(result)[:800]}")


def gen_dalle(prompt):
    key = _first_env("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set for DALL-E / OpenAI images.")
    model = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
    size = OPENAI_GPT_IMAGE_SIZE if model == "gpt-image-1" else OPENAI_DALLE3_SIZE
    payload = {"model": model, "prompt": prompt, "n": 1, "size": size}
    if model != "gpt-image-1":
        # dall-e-3 needs explicit b64 request; gpt-image-1 returns b64 by default.
        payload["response_format"] = "b64_json"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    result = _http_json("https://api.openai.com/v1/images/generations", payload, headers)
    item = (result.get("data") or [{}])[0]
    if item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    if item.get("url"):
        with urllib.request.urlopen(item["url"], timeout=180) as r:
            return r.read()
    raise RuntimeError(f"No image returned by OpenAI. Raw response:\n{json.dumps(result)[:800]}")


def gen_imagen(prompt):
    key = _first_env("GEMINI_API_KEY", "GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY not set for Imagen.")
    model = os.environ.get("IMAGEN_MODEL", "imagen-3.0-generate-002")
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:predict?key={key}"
    )
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9"},
    }
    result = _http_json(url, payload, {"Content-Type": "application/json"})
    for pred in result.get("predictions", []):
        b64 = pred.get("bytesBase64Encoded") or pred.get("image", {}).get("bytesBase64Encoded")
        if b64:
            return base64.b64decode(b64)
    raise RuntimeError(f"No image returned by Imagen. Raw response:\n{json.dumps(result)[:800]}")


def gen_stability(prompt):
    key = _first_env("STABILITY_API_KEY")
    if not key:
        raise RuntimeError("STABILITY_API_KEY not set for Stability AI.")
    try:
        import requests  # multipart/form-data is far cleaner with requests
    except ImportError:
        raise RuntimeError("The 'stability' provider needs the 'requests' package: pip install requests")
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    resp = requests.post(
        url,
        headers={"authorization": f"Bearer {key}", "accept": "image/*"},
        files={"none": ""},
        data={"prompt": prompt, "aspect_ratio": "16:9", "output_format": "png"},
        timeout=180,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code} from Stability:\n{resp.text[:800]}")
    return resp.content


GENERATORS = {
    "nanobanana": gen_nanobanana,
    "dalle": gen_dalle,
    "imagen": gen_imagen,
    "stability": gen_stability,
}

# ---- Character IP loading ----

# Canonical IDs and their display names / cultures (for --list-characters).
CHARACTERS = {
    "xiaohei":     ("Xiaohei (小黑)",       "Chinese / East Asian"),
    "chibi-kage":  ("Chibi Kage (小影)",    "Japanese"),
    "kaala":       ("Kaala (काला)",          "South / Southeast Asian"),
    "kali-tikka":  ("Kali Tikka",           "Indian (street / vernacular)"),
    "le-bloc":     ("Le Bloc / Der Fleck",  "European"),
    "the-smudge":  ("The Smudge",           "American"),
    "dudu":        ("Dudu",                 "West African / Afrofuturist"),
    "el-manchon":  ("El Manchón",           "Latin American"),
    "al-zill":     ("Al-Zill (الظل)",       "Middle Eastern / Arabic"),
}

# Aliases that map to canonical IDs.
CHARACTER_ALIASES = {
    "xiaohei": "xiaohei", "xiao-hei": "xiaohei", "小黑": "xiaohei",
    "chibi-kage": "chibi-kage", "kage": "chibi-kage", "小影": "chibi-kage",
    "kaala": "kaala", "kala": "kaala",
    "kali-tikka": "kali-tikka", "tikka": "kali-tikka",
    "le-bloc": "le-bloc", "bloc": "le-bloc", "der-fleck": "le-bloc", "fleck": "le-bloc",
    "the-smudge": "the-smudge", "smudge": "the-smudge",
    "dudu": "dudu",
    "el-manchon": "el-manchon", "manchon": "el-manchon",
    "al-zill": "al-zill", "zill": "al-zill", "الظل": "al-zill",
}

# The characters/ dir lives alongside this script's parent (the skill root).
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_SKILL_ROOT = os.path.dirname(_SCRIPT_DIR)
_CHARS_DIR = os.path.join(_SKILL_ROOT, "references", "characters")
_SETTINGS_FILE = os.path.join(_SKILL_ROOT, "settings.json")


# ---- Settings ----

def _load_settings():
    """Return parsed settings dict, or {} if file missing/corrupt."""
    if not os.path.exists(_SETTINGS_FILE):
        return {}
    try:
        with open(_SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_settings(data):
    """Write settings dict to settings.json."""
    existing = _load_settings()
    existing.update(data)
    # Keep the human-readable note
    if "_note" not in existing:
        existing["_note"] = (
            "Change default_character to any ID from references/characters/INDEX.md, "
            "or run: python3 scripts/generate_image.py --set-default <id>"
        )
    with open(_SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
        f.write("\n")


def get_default_character():
    """Return the configured default character ID, falling back to 'xiaohei'."""
    settings = _load_settings()
    raw = settings.get("default_character", "xiaohei")
    return CHARACTER_ALIASES.get(raw.lower().strip(), raw.lower().strip())


def _load_character_injection(char_id):
    """Return the 'Prompt Injection' code block text from a character file."""
    char_file = os.path.join(_CHARS_DIR, f"{char_id}.md")
    if not os.path.exists(char_file):
        raise RuntimeError(
            f"Character file not found: {char_file}\n"
            f"Available: {', '.join(CHARACTERS)}"
        )
    with open(char_file, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract the fenced code block under '## Prompt Injection'
    match = re.search(
        r"## Prompt Injection\s*```[^\n]*\n(.*?)```",
        content,
        re.DOTALL,
    )
    if not match:
        raise RuntimeError(f"No 'Prompt Injection' code block found in {char_file}")
    return match.group(1).strip()


def inject_character(prompt, char_id):
    """
    Splice the character's Prompt Injection block into the prompt.

    Replaces the 'IP character required:' paragraph if present; otherwise
    inserts the block after 'Visual DNA:' paragraph, before 'Theme:'.
    If neither anchor is found, appends at the end.
    """
    injection = _load_character_injection(char_id)
    char_block = f"IP character required:\n{injection}"

    # Replace existing IP character block (any character's block).
    replaced = re.sub(
        r"IP character(?: required)?:.*?(?=\n\n|\nTheme:|\nStructure type:|\Z)",
        char_block,
        prompt,
        flags=re.DOTALL,
    )
    if replaced != prompt:
        return replaced

    # Insert before 'Theme:' if no existing block.
    if "\nTheme:" in prompt:
        return prompt.replace("\nTheme:", f"\n{char_block}\n\nTheme:", 1)

    # Fallback: append.
    return prompt.rstrip() + f"\n\n{char_block}"


# ---- Prompt reading ----

def read_prompt(args):
    if args.prompt:
        return args.prompt
    if args.prompt_file:
        with open(args.prompt_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()
        if data:
            return data
    raise RuntimeError("No prompt provided. Use --prompt, --prompt-file, or pipe via stdin.")


def main():
    default_char = get_default_character()

    parser = argparse.ArgumentParser(
        description="Generate one illustration via an available image model."
    )
    parser.add_argument("--provider", help="nanobanana|gemini, dalle|openai, imagen, stability|sd. Auto-detected if omitted.")
    parser.add_argument("--character", "-c", default=None,
                        help=f"IP character to use. Defaults to the value in settings.json "
                             f"(currently: {default_char}). See --list-characters for all IDs.")
    parser.add_argument("--set-default", metavar="CHARACTER_ID",
                        help="Set a new default character in settings.json and exit.")
    parser.add_argument("--show-default", action="store_true",
                        help="Print the current default character and exit.")
    parser.add_argument("--prompt", help="Prompt text.")
    parser.add_argument("--prompt-file", help="Path to a file containing the prompt.")
    parser.add_argument("--out", "-o", default="illustration.png", help="Output PNG path.")
    parser.add_argument("--list-providers", action="store_true", help="List providers with a key set, then exit.")
    parser.add_argument("--list-characters", action="store_true", help="List available IP characters, then exit.")
    args = parser.parse_args()

    if args.list_providers:
        found = available_providers()
        print("Available (key present):", ", ".join(found) if found else "(none)")
        return 0

    if args.list_characters:
        current_default = get_default_character()
        print(f"{'ID':<14} {'Display Name':<26} {'Culture'}")
        print("-" * 65)
        for cid, (name, culture) in CHARACTERS.items():
            marker = " ← default" if cid == current_default else ""
            print(f"{cid:<14} {name:<26} {culture}{marker}")
        print(f"\nSettings file: {_SETTINGS_FILE}")
        print(f"Change default: python3 {os.path.basename(__file__)} --set-default <id>")
        return 0

    if args.show_default:
        cid = get_default_character()
        name, culture = CHARACTERS.get(cid, (cid, "unknown"))
        print(f"Default character: {cid}")
        print(f"  {name} — {culture}")
        print(f"  Settings: {_SETTINGS_FILE}")
        return 0

    if args.set_default:
        raw = args.set_default.lower().strip()
        new_id = CHARACTER_ALIASES.get(raw, raw)
        if new_id not in CHARACTERS:
            print(
                f"Unknown character: {args.set_default}. "
                f"Run --list-characters to see available IDs.",
                file=sys.stderr,
            )
            return 2
        _save_settings({"default_character": new_id})
        name, culture = CHARACTERS[new_id]
        print(f"Default character updated: {new_id}")
        print(f"  {name} — {culture}")
        print(f"  Saved to: {_SETTINGS_FILE}")
        return 0

    # Resolve character: CLI flag > settings.json default > hardcoded fallback
    char_raw = (args.character or default_char).lower().strip()
    char_id = CHARACTER_ALIASES.get(char_raw, char_raw)
    if char_id not in CHARACTERS:
        print(
            f"Unknown character: {args.character or default_char}. "
            f"Run --list-characters to see available IDs.",
            file=sys.stderr,
        )
        return 2

    prompt = read_prompt(args)
    prompt = inject_character(prompt, char_id)

    if args.provider:
        canonical = PROVIDER_ALIASES.get(args.provider.lower())
        if not canonical:
            print(f"Unknown provider: {args.provider}. Known: {sorted(set(PROVIDER_ALIASES))}", file=sys.stderr)
            return 2
    else:
        canonical = detect_provider()

    char_name = CHARACTERS[char_id][0]
    print(f"[generate_image] provider={canonical} character={char_id} ({char_name}) -> {args.out}", file=sys.stderr)
    image_bytes = GENERATORS[canonical](prompt)

    out_dir = os.path.dirname(os.path.abspath(args.out))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(image_bytes)
    print(args.out)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

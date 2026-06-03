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
"""

import argparse
import base64
import json
import os
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
    parser = argparse.ArgumentParser(description="Generate one illustration via an available image model.")
    parser.add_argument("--provider", help="nanobanana|gemini, dalle|openai, imagen, stability|sd. Auto-detected if omitted.")
    parser.add_argument("--prompt", help="Prompt text.")
    parser.add_argument("--prompt-file", help="Path to a file containing the prompt.")
    parser.add_argument("--out", "-o", default="illustration.png", help="Output PNG path.")
    parser.add_argument("--list-providers", action="store_true", help="List providers with a key set, then exit.")
    args = parser.parse_args()

    if args.list_providers:
        found = available_providers()
        print("Available (key present):", ", ".join(found) if found else "(none)")
        return 0

    prompt = read_prompt(args)

    if args.provider:
        canonical = PROVIDER_ALIASES.get(args.provider.lower())
        if not canonical:
            print(f"Unknown provider: {args.provider}. Known: {sorted(set(PROVIDER_ALIASES))}", file=sys.stderr)
            return 2
    else:
        canonical = detect_provider()

    print(f"[generate_image] provider={canonical} -> {args.out}", file=sys.stderr)
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

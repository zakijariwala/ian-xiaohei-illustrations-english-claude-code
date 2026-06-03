#!/usr/bin/env python3
"""
Project scanner for Ian Xiaohei Illustrations.

Scans the current directory (or a given path) for article content —
Markdown files, text files, READMEs — and outputs illustration suggestions
based on what it finds: headings, key paragraphs, and likely cognitive anchors.

Designed to be run by any agent CLI to give the skill context when the user
hasn't pasted an article directly.

Usage
-----
  python3 scan_project.py                  # scan current directory
  python3 scan_project.py /path/to/dir    # scan a specific directory
  python3 scan_project.py --file post.md  # scan one specific file
  python3 scan_project.py --json          # output as JSON for agent parsing
"""

import argparse
import json
import os
import re
import sys

# File extensions considered article content (in priority order).
ARTICLE_EXTENSIONS = {".md", ".mdx", ".txt", ".rst"}

# Filenames that are likely project docs rather than articles.
SKIP_NAMES = {
    "readme.md", "readme.txt", "license", "license.md", "license.txt",
    "changelog.md", "changelog.txt", "contributing.md", "notice.md",
    "code_of_conduct.md", ".gitignore",
}

# Heading pattern for Markdown and plain text.
HEADING_RE = re.compile(r"^#{1,3}\s+(.+)$", re.MULTILINE)

# Paragraph pattern: non-empty lines of reasonable length.
PARA_RE = re.compile(r"(?:^|\n)([A-Z][^\n]{40,300})(?=\n|$)")

# Cognitive anchor signals in headings/paragraphs.
ANCHOR_SIGNALS = [
    "why", "how", "when", "problem", "solution", "before", "after",
    "instead", "never", "always", "step", "workflow", "process", "system",
    "result", "cost", "mistake", "trap", "lesson", "principle", "rule",
    "the key", "the difference", "the reason", "the point", "the goal",
    "the issue", "the trick", "the truth",
]


def is_article_file(path):
    name = os.path.basename(path).lower()
    if name in SKIP_NAMES:
        return False
    _, ext = os.path.splitext(name)
    return ext in ARTICLE_EXTENSIONS


def find_article_files(root, max_files=20):
    """Walk root and return up to max_files article candidates, ranked by size."""
    candidates = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs and common non-content dirs.
        dirnames[:] = [
            d for d in dirnames
            if not d.startswith(".") and d not in {"node_modules", "__pycache__", ".git", "vendor"}
        ]
        for fname in filenames:
            path = os.path.join(dirpath, fname)
            if is_article_file(path):
                try:
                    size = os.path.getsize(path)
                    candidates.append((size, path))
                except OSError:
                    pass
    # Sort by size descending (larger files are more likely real articles).
    candidates.sort(reverse=True)
    return [p for _, p in candidates[:max_files]]


def extract_content(path, max_chars=4000):
    """Read and return up to max_chars of the file, stripping front matter."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read(max_chars * 2)
    except OSError:
        return ""
    # Strip YAML front matter.
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    return text[:max_chars]


def extract_headings(text):
    return HEADING_RE.findall(text)


def extract_anchor_candidates(text):
    """Return sentences/paragraphs that contain cognitive anchor signals."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    anchors = []
    for sent in sentences:
        lower = sent.lower()
        if any(sig in lower for sig in ANCHOR_SIGNALS) and 30 < len(sent) < 250:
            anchors.append(sent.strip())
    return anchors[:6]


def score_file(path, text):
    """Rough relevance score: more headings + anchor signals = higher priority."""
    headings = extract_headings(text)
    anchors = extract_anchor_candidates(text)
    word_count = len(text.split())
    return len(headings) * 3 + len(anchors) * 2 + min(word_count // 100, 10)


def analyse_file(path):
    text = extract_content(path)
    if not text.strip():
        return None
    headings = extract_headings(text)
    anchors = extract_anchor_candidates(text)
    score = score_file(path, text)
    word_count = len(text.split())
    rel_path = os.path.relpath(path)
    return {
        "path": rel_path,
        "word_count": word_count,
        "score": score,
        "headings": headings[:8],
        "anchor_candidates": anchors,
    }


def format_suggestions(results, default_character):
    """Format analysis results as human-readable illustration suggestions."""
    lines = []
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append("  Ian Xiaohei Illustrations — Project Scan")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append(f"  Default character: {default_character}")
    lines.append(f"  Files found: {len(results)}")
    lines.append("")

    if not results:
        lines.append("  No article content found in this directory.")
        lines.append("  Paste your article text directly when invoking the skill.")
        return "\n".join(lines)

    for i, r in enumerate(results, 1):
        lines.append(f"  [{i}] {r['path']}  ({r['word_count']} words)")
        if r["headings"]:
            lines.append(f"      Sections: {' / '.join(r['headings'][:4])}")
        if r["anchor_candidates"]:
            lines.append(f"      Anchor: \"{r['anchor_candidates'][0][:80]}\"")
        lines.append("")

    lines.append("  Suggested next steps:")
    lines.append("  1. Paste the article into your agent and invoke the skill:")
    lines.append("     /ian-xiaohei-illustrations Generate a shot list for this article.")
    lines.append("  2. Or point the skill at a file:")
    lines.append(f"     /ian-xiaohei-illustrations Read {results[0]['path']} and generate a shot list.")
    lines.append("  3. Or generate directly:")
    lines.append(f"     python3 scripts/generate_image.py --character {default_character} --prompt-file ...")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Scan a project directory for article content and suggest illustration opportunities."
    )
    parser.add_argument("directory", nargs="?", default=".",
                        help="Directory to scan (default: current directory).")
    parser.add_argument("--file", "-f", help="Scan a single specific file instead of a directory.")
    parser.add_argument("--json", action="store_true", help="Output results as JSON.")
    parser.add_argument("--max", type=int, default=10, help="Max files to analyse (default: 10).")
    args = parser.parse_args()

    # Read default character from settings.json.
    settings_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "settings.json")
    default_character = "xiaohei"
    if os.path.exists(settings_file):
        try:
            with open(settings_file) as f:
                default_character = json.load(f).get("default_character", "xiaohei")
        except (json.JSONDecodeError, OSError):
            pass

    if args.file:
        paths = [args.file]
    else:
        scan_root = os.path.abspath(args.directory)
        paths = find_article_files(scan_root, max_files=args.max)

    results = []
    for path in paths:
        analysis = analyse_file(path)
        if analysis:
            results.append(analysis)

    # Sort by score descending.
    results.sort(key=lambda r: r["score"], reverse=True)

    if args.json:
        out = {
            "default_character": default_character,
            "files_found": len(results),
            "results": results,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(format_suggestions(results, default_character))

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)

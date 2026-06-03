#!/usr/bin/env bash
# Install Ian Xiaohei Illustrations skill for a supported AI agent platform.
# Usage: ./install.sh [platform]
# Platforms: claude (default), codex, gemini
# With no argument, auto-detects based on available CLI tools.

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="ian-xiaohei-illustrations"

detect_platform() {
  if command -v claude &>/dev/null; then
    echo "claude"
  elif command -v codex &>/dev/null; then
    echo "codex"
  elif command -v gemini &>/dev/null; then
    echo "gemini"
  else
    echo "unknown"
  fi
}

install_claude() {
  DEST="${HOME}/.claude/skills/${SKILL_NAME}"
  mkdir -p "${HOME}/.claude/skills"
  cp -R "${SKILL_DIR}" "${DEST}"
  echo "Installed to: ${DEST}"
  echo "Use in Claude Code: /ian-xiaohei-illustrations"
}

install_codex() {
  CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
  DEST="${CODEX_HOME}/skills/${SKILL_NAME}"
  mkdir -p "${CODEX_HOME}/skills"
  cp -R "${SKILL_DIR}" "${DEST}"
  echo "Installed to: ${DEST}"
  echo "Use in Codex: Use \$ian-xiaohei-illustrations ..."
}

install_gemini() {
  DEST="${HOME}/.gemini/skills/${SKILL_NAME}"
  mkdir -p "${HOME}/.gemini/skills"
  cp -R "${SKILL_DIR}" "${DEST}"
  echo "Installed to: ${DEST}"
}

PLATFORM="${1:-$(detect_platform)}"

case "${PLATFORM}" in
  claude)
    echo "Installing for Claude Code..."
    install_claude
    ;;
  codex|openai)
    echo "Installing for OpenAI Codex..."
    install_codex
    ;;
  gemini)
    echo "Installing for Gemini CLI..."
    install_gemini
    ;;
  unknown)
    echo "Could not auto-detect a supported AI CLI."
    echo "Run: ./install.sh [claude|codex|gemini]"
    exit 1
    ;;
  *)
    echo "Unknown platform: ${PLATFORM}"
    echo "Supported: claude, codex, gemini"
    exit 1
    ;;
esac

echo "Done. Skill '${SKILL_NAME}' installed for ${PLATFORM}."

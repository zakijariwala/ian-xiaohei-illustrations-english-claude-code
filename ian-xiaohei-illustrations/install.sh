#!/usr/bin/env bash
# Install Ian Xiaohei Illustrations skill for a supported AI agent platform.
# Usage: ./install.sh [platform]
# Platforms: claude (default), codex, gemini
# With no argument, auto-detects based on available CLI tools.

set -e

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="ian-xiaohei-illustrations"

# ---- Character list (must stay in sync with generate_image.py CHARACTERS dict) ----
CHAR_IDS=(xiaohei chibi-kage kaala kali-tikka le-bloc the-smudge dudu el-manchon al-zill)
CHAR_NAMES=(
  "Xiaohei (小黑)       — Chinese / East Asian         (original)"
  "Chibi Kage (小影)    — Japanese"
  "Kaala (काला)        — South / Southeast Asian"
  "Kali Tikka          — Indian (block-print / folk art)"
  "Le Bloc / Der Fleck — European"
  "The Smudge          — American"
  "Dudu                — West African / Afrofuturist"
  "El Manchón          — Latin American"
  "Al-Zill (الظل)      — Middle Eastern / Arabic"
)

# ---- Platform detection ----
detect_platform() {
  if command -v claude &>/dev/null; then echo "claude"
  elif command -v codex &>/dev/null; then echo "codex"
  elif command -v gemini &>/dev/null; then echo "gemini"
  else echo "unknown"
  fi
}

# INSTALL_MODE is set by sync_skill to "fresh" or "reinstall".
INSTALL_MODE="fresh"

# ---- Idempotent copy ----
# Copies the skill into ${dest}. Safe whether or not ${dest} already exists
# (avoids the cp -R nesting trap). On re-install, preserves the user's
# settings.json so their chosen default character survives upgrades.
sync_skill() {
  local dest="$1"

  # Safety: never delete the source we are copying from.
  if [[ "$(cd "${SKILL_DIR}" && pwd -P)" == "$(cd "$(dirname "${dest}")" 2>/dev/null && pwd -P)/$(basename "${dest}")" ]]; then
    echo "Refusing to install onto the source directory: ${dest}" >&2
    exit 1
  fi

  mkdir -p "$(dirname "${dest}")"

  local saved_settings=""
  if [[ -d "${dest}" ]]; then
    INSTALL_MODE="reinstall"
    if [[ -f "${dest}/settings.json" ]]; then
      saved_settings="$(mktemp)"
      cp "${dest}/settings.json" "${saved_settings}"
    fi
    rm -rf "${dest}"
  fi

  mkdir -p "${dest}"
  cp -R "${SKILL_DIR}/." "${dest}/"

  if [[ -n "${saved_settings}" ]]; then
    cp "${saved_settings}" "${dest}/settings.json"
    rm -f "${saved_settings}"
  fi
}

# ---- Install functions ----
install_claude() {
  DEST="${HOME}/.claude/skills/${SKILL_NAME}"
  sync_skill "${DEST}"
  echo "Installed to: ${DEST}"
  echo "Invoke in Claude Code: /ian-xiaohei-illustrations"
}

install_codex() {
  CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
  DEST="${CODEX_HOME}/skills/${SKILL_NAME}"
  sync_skill "${DEST}"
  echo "Installed to: ${DEST}"
  echo "Invoke in Codex: Use \$ian-xiaohei-illustrations ..."
}

install_gemini() {
  DEST="${HOME}/.gemini/skills/${SKILL_NAME}"
  sync_skill "${DEST}"
  echo "Installed to: ${DEST}"
}

# ---- Destination resolver ----
get_dest() {
  case "${1}" in
    claude) echo "${HOME}/.claude/skills/${SKILL_NAME}" ;;
    codex)  echo "${CODEX_HOME:-$HOME/.codex}/skills/${SKILL_NAME}" ;;
    gemini) echo "${HOME}/.gemini/skills/${SKILL_NAME}" ;;
  esac
}

# ---- First-run character selector ----
# Called after install. On re-install the user's existing default is preserved
# (sync_skill restored their settings.json), so we just report it and return.
# On a non-interactive shell (CI, curl|bash) we keep the shipped default.
ask_default_character() {
  local dest="$1"
  local settings_file="${dest}/settings.json"

  if [[ "${INSTALL_MODE}" == "reinstall" ]]; then
    current=$(python3 -c "import json; d=json.load(open('${settings_file}')); print(d.get('default_character','xiaohei'))" 2>/dev/null || echo "xiaohei")
    echo ""
    echo "Upgrade detected — kept your existing default character: ${current}"
    echo "To change it: python3 ${dest}/scripts/generate_image.py --set-default <id>"
    return
  fi

  # Non-interactive (no TTY): keep the shipped default, don't block the install.
  if [[ ! -t 0 ]]; then
    current=$(python3 -c "import json; d=json.load(open('${settings_file}')); print(d.get('default_character','xiaohei'))" 2>/dev/null || echo "xiaohei")
    echo ""
    echo "Non-interactive install — default character: ${current}"
    echo "To change it: python3 ${dest}/scripts/generate_image.py --set-default <id>"
    return
  fi

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  First-time setup — choose your default character (IP)"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  for i in "${!CHAR_IDS[@]}"; do
    printf "  %d) %s\n" $((i+1)) "${CHAR_NAMES[$i]}"
  done
  echo ""
  echo "  This sets the default character used when none is specified."
  echo "  You can always override per-image with --character <id>,"
  echo "  or change the default later with --set-default <id>."
  echo ""

  local choice=""
  while true; do
    read -r -p "  Enter number [1-${#CHAR_IDS[@]}], or press Enter for xiaohei: " choice
    choice="${choice:-1}"
    if [[ "$choice" =~ ^[0-9]+$ ]] && (( choice >= 1 && choice <= ${#CHAR_IDS[@]} )); then
      break
    fi
    echo "  Please enter a number between 1 and ${#CHAR_IDS[@]}."
  done

  local idx=$((choice-1))
  local selected_id="${CHAR_IDS[$idx]}"
  local selected_name="${CHAR_NAMES[$idx]}"

  # Write settings.json
  cat > "${settings_file}" <<SETTINGS
{
  "default_character": "${selected_id}",
  "_note": "Change default_character to any ID from references/characters/INDEX.md, or run: python3 scripts/generate_image.py --set-default <id>"
}
SETTINGS

  echo ""
  echo "  ✓ Default character set to: ${selected_id}"
  echo "    ${selected_name}"
  echo ""
  echo "  Change it any time:"
  echo "    python3 ${dest}/scripts/generate_image.py --set-default <id>"
  echo "    — or edit ${dest}/settings.json directly"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# ---- Main ----
PLATFORM="${1:-$(detect_platform)}"

case "${PLATFORM}" in
  claude)
    echo "Installing for Claude Code..."
    install_claude
    ask_default_character "$(get_dest claude)"
    ;;
  codex|openai)
    echo "Installing for OpenAI Codex..."
    install_codex
    ask_default_character "$(get_dest codex)"
    ;;
  gemini)
    echo "Installing for Gemini CLI..."
    install_gemini
    ask_default_character "$(get_dest gemini)"
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

echo ""
echo "Done. Skill '${SKILL_NAME}' installed for ${PLATFORM}."

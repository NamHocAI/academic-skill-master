#!/usr/bin/env bash
# Cài Academic Skill Master cho Claude Code và Codex trên macOS / Linux.
set -euo pipefail
src="$(cd "$(dirname "$0")" && pwd)/skills/academic-skill-master"

if [ ! -f "$src/SKILL.md" ]; then
  echo "Không tìm thấy skills/academic-skill-master/SKILL.md. Hãy chạy script trong thư mục đã giải nén." >&2
  exit 1
fi

install_to() {
  local tool="$1" dest="$2"
  rm -rf "$dest"
  mkdir -p "$(dirname "$dest")"
  cp -R "$src" "$dest"
  echo "Đã cài cho $tool: $dest"
}

install_to "Claude Code" "$HOME/.claude/skills/academic-skill-master"
install_to "Codex" "$HOME/.agents/skills/academic-skill-master"

echo 'Mở Claude Code hoặc Codex và nhắn: "Tạo trợ lý cho đồ án của mình".'

#!/usr/bin/env bash
# Cài Academic Skill Master cho Claude Code trên macOS / Linux.
set -euo pipefail
src="$(cd "$(dirname "$0")" && pwd)/skills/academic-skill-master"
dest="$HOME/.claude/skills/academic-skill-master"

if [ ! -f "$src/SKILL.md" ]; then
  echo "Không tìm thấy skills/academic-skill-master/SKILL.md. Hãy chạy script trong thư mục đã giải nén." >&2
  exit 1
fi

rm -rf "$dest"
mkdir -p "$(dirname "$dest")"
cp -R "$src" "$dest"

echo "Đã cài xong vào: $dest"
echo 'Mở Claude Code và nhắn: "Tạo trợ lý cho đồ án của mình".'

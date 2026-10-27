#!/usr/bin/env python3
"""Đóng gói skills/academic-skill-master thành dist/academic-skill-master.zip để tải lên Claude.ai."""
import pathlib
import sys
import zipfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "academic-skill-master"
OUT = ROOT / "dist" / "academic-skill-master.zip"
SKIP = {"__pycache__", ".DS_Store"}

OUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(SKILL.rglob("*")):
        if path.is_file() and not SKIP.intersection(path.parts):
            z.write(path, pathlib.Path(SKILL.name) / path.relative_to(SKILL))
print(f"Đã tạo {OUT.relative_to(ROOT)}")

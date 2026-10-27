#!/usr/bin/env python3
"""Kiểm tra một file SKILL_MASTER.md (hoặc SKILL.md / .mdc) được tạo bởi academic-skill-master.

Cách dùng:
    python validate_skill.py <file> [--env web|code|codex|cursor]

Thoát với mã 0 nếu không có LỖI (cảnh báo vẫn được in ra), mã 1 nếu có lỗi.
"""
import argparse
import re
import sys

SECTIONS = [
    "Section 1: CORE ARCHITECTURE & DOMAIN PROTOCOL",
    "Section 2: TEMPLATE ENFORCEMENT & MECHANICAL STYLING RULES",
    "Section 3: AUTONOMOUS CITATION ENGINE",
    "Section 4: ADAPTIVE COLLABORATION MATRIX",
    "Section 5: NATURAL-LANGUAGE INTENT ROUTER",
]
NOTICE = "LƯU Ý: Hãy kiểm tra quy định của trường/khoa về việc sử dụng AI trong đồ án và khai báo đúng yêu cầu."
LENGTH = {"web": (500, 800), "code": (500, 800), "codex": (500, 800), "cursor": (300, 400)}
SOURCE_TAGS = ("từ template", "từ bạn khai", "giả định", "chưa có")


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[m.end():]


def main():
    # Console Windows mặc định không in được tiếng Việt
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--env", choices=LENGTH, default="code")
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    errors, warnings = [], []
    fm, body = parse_frontmatter(text)

    if fm is None:
        errors.append("Thiếu YAML frontmatter (khối --- ở đầu file).")
        fm = {}
    if args.env == "cursor":
        if not fm.get("description"):
            errors.append("Frontmatter .mdc thiếu 'description'.")
    else:
        name = fm.get("name", "")
        if not name:
            errors.append("Frontmatter thiếu 'name'.")
        elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"'name' không hợp lệ: '{name}' (chỉ chữ thường, số, gạch ngang, tối đa 64 ký tự).")
        elif re.search(r"claude|anthropic", name):
            errors.append(f"'name' không được chứa 'claude' hoặc 'anthropic': '{name}'.")
        desc = fm.get("description", "")
        if not desc:
            errors.append("Frontmatter thiếu 'description'.")
        else:
            if len(desc) > 1024:
                errors.append(f"'description' dài {len(desc)} ký tự (tối đa 1024).")
            elif len(desc) > 1000:
                warnings.append(f"'description' dài {len(desc)} ký tự, nên dưới 1000.")
            if "<" in desc or ">" in desc:
                errors.append("'description' chứa dấu < hoặc > (có thể còn chỗ điền chưa thay).")

    headings = re.findall(r"^##\s+(.+?)\s*$", body, re.M)
    found = [h for h in headings if h.startswith("Section ")]
    for s in SECTIONS:
        if s not in found:
            errors.append(f"Thiếu section: '## {s}'.")
    if found and [h for h in found if h in SECTIONS] != [s for s in SECTIONS if s in found]:
        errors.append("Các section không đúng thứ tự 1 → 5.")
    if len(found) > len(SECTIONS):
        warnings.append(f"Có {len(found)} heading bắt đầu bằng 'Section', nhiều hơn 5.")

    s1 = re.search(r"^##\s+" + re.escape(SECTIONS[0]) + r"\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if s1:
        first = next((ln.strip().lstrip(">").strip() for ln in s1.group(1).splitlines() if ln.strip()), "")
        if NOTICE not in first:
            errors.append("Dòng đầu Section 1 không phải dòng 'LƯU Ý: ...' cố định.")

    s2 = re.search(r"^##\s+" + re.escape(SECTIONS[1]) + r"\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if s2:
        missing = []
        for ln in s2.group(1).splitlines():
            if ln.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", ln):
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if cells and cells[0].lower() in ("thông số", "cấp", "mục", "hạng mục"):
                    continue  # dòng tiêu đề bảng
                if not any(tag in ln.lower() for tag in SOURCE_TAGS):
                    missing.append(ln.strip()[:70])
        if missing:
            errors.append(f"Section 2 có {len(missing)} dòng bảng chưa ghi nguồn, VD: {missing[0]}")

    placeholders = re.findall(r"<(?:ten|tên|Tên)[^>]*>", text)
    if placeholders:
        errors.append(f"Còn chỗ điền chưa thay: {', '.join(sorted(set(placeholders))[:5])}")

    n = text.count("\n") + 1
    lo, hi = LENGTH[args.env]
    if not lo <= n <= hi:
        warnings.append(f"Độ dài {n} dòng, khuyến nghị {lo}–{hi} dòng cho môi trường '{args.env}'.")

    for w in warnings:
        print(f"CẢNH BÁO: {w}")
    for e in errors:
        print(f"LỖI: {e}")
    if errors:
        print(f"\nKẾT QUẢ: CHƯA ĐẠT ({len(errors)} lỗi, {len(warnings)} cảnh báo)")
        return 1
    print(f"\nKẾT QUẢ: ĐẠT ({n} dòng, {len(warnings)} cảnh báo)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

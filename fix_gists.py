import os
from pathlib import Path

GISTS_DIR = Path("gists")

if not GISTS_DIR.exists():
    print(f"❌ Folder '{GISTS_DIR}' not found.")
    exit(1)

for md_file in GISTS_DIR.glob("*.md"):
    text = md_file.read_text(encoding="utf-8").strip()

    if not text:
        print(f"⚠️ Skipping empty file: {md_file.name}")
        continue

    if "{% raw %}" in text:
        print(f"✅ Already fixed: {md_file.name}")
        continue

    wrapped = f"""---
layout: none
title: Memory Fragment
---

{{% raw %}}
{text}
{{% endraw %}}
"""
    md_file.write_text(wrapped, encoding="utf-8")
    print(f"✅ Fixed: {md_file.name}")
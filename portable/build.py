#!/usr/bin/env python3
"""Build a tool-agnostic knowledge pack from this repo so the agency can be
recreated in ChatGPT (Custom GPT or Project) or any other assistant.

Run from the repo root:  python3 portable/build.py
Output: portable/chatgpt/*.md  (upload these as knowledge files; paste
portable/INSTRUCTIONS.md as the instructions)
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "portable", "chatgpt")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def strip_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2).strip()


def write(name, text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")
    print(f"{name}: {len(text):,} chars")


def collect(dir_, label):
    parts = []
    for path in sorted(glob.glob(os.path.join(ROOT, dir_, "*.md"))):
        meta, body = strip_frontmatter(open(path, encoding="utf-8").read())
        name = meta.get("name") or os.path.splitext(os.path.basename(path))[0]
        parts.append(f"## {label}: {name}\n_{meta.get('description', '')}_\n\n{body}")
    return "\n\n---\n\n".join(parts)


def main():
    write("01-memory.md", read("brand/memory.md"))
    write("02-brand-profile.md", read("brand/profile.md"))
    write("03-operating-mode.md", read("docs/operating-mode.md"))
    write(
        "04-agents-playbook.md",
        "# Agent playbooks\nAnswer as the matching role. Tool names mentioned are from the "
        "original system; use any equivalent or ask Karen to paste data.\n\n"
        + collect(".claude/agents", "ROLE"),
    )
    write(
        "05-rituals.md",
        "# Rituals\nKaren types these as plain messages (e.g. \"/daily-drop\"). "
        "Run them as the director.\n\n" + collect(".claude/commands", "RITUAL /"),
    )
    extras = [
        "# Guides, connectors, schedules\n",
        read("guides/streaming-setup.md"),
        read("docs/connectors.md"),
        read("automation/schedules.md"),
        "# Templates\n" + read("templates/shoot-card.md") + "\n" + read("templates/run-of-show.md"),
    ]
    write("06-guides-and-tools.md", "\n\n---\n\n".join(extras))

    latest = ["# Latest plans, reports and dashboard data\n"]
    for pattern in ("plans/*.md", "reports/*.md", "streams/*.md", "clips/*.md", "team/*.md"):
        for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
            rel = os.path.relpath(path, ROOT)
            latest.append(f"## {rel}\n\n{open(path, encoding='utf-8').read()}")
    data = json.dumps(json.load(open(os.path.join(ROOT, "dashboard/data.json"))), indent=2)
    latest.append(f"## dashboard/data.json\n\n```json\n{data}\n```")
    write("07-latest-plans-and-data.md", "\n\n---\n\n".join(latest))

    instr = read("portable/INSTRUCTIONS.md")
    print(f"INSTRUCTIONS.md: {len(instr):,} chars (Custom GPT limit is 8,000)")
    if len(instr) > 8000:
        raise SystemExit("INSTRUCTIONS.md is over 8,000 characters")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the public Tehseen Tech Manus Skills repository.

This check intentionally uses only the Python standard library so it can run in
GitHub Actions without installing project-specific dependencies.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

TRIGGER = "Apply automatically when the request matches; the user does not need to mention this skill."
EXPECTED_HEADINGS = ("Overview", "Workflow", "Usage")
STALE_PATTERNS = ("abcnuts/manus-skills", "71-skill", "71 skills")


def tracked_files(root: Path) -> list[Path]:
    try:
        output = subprocess.check_output(["git", "ls-files"], cwd=root, text=True)
    except (OSError, subprocess.CalledProcessError):
        return [p.relative_to(root) for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    return [Path(line) for line in output.splitlines() if line]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter start")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("missing YAML frontmatter end")
    raw = text[4:end]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[end + 4 :]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry_path = root / "skills.json"
    errors: list[str] = []

    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - command-line failure path
        print(f"FAIL: cannot load skills.json: {exc}")
        return 1

    declared = int(registry.get("total_skills", 0))
    entries = registry.get("skills", {})
    files = sorted(p for p in root.rglob("SKILL.md") if ".git" not in p.parts)
    if len(files) != declared:
        errors.append(f"skill file count is {len(files)}, registry declares {declared}")
    if len(entries) != declared:
        errors.append(f"registry entry count is {len(entries)}, registry declares {declared}")

    actual_paths = {p.relative_to(root).as_posix() for p in files}
    registry_paths = {entry.get("path") for entry in entries.values()}
    missing = sorted(registry_paths - actual_paths)
    unregistered = sorted(actual_paths - registry_paths)
    if missing:
        errors.append(f"missing registry paths: {', '.join(missing)}")
    if unregistered:
        errors.append(f"unregistered skill files: {', '.join(unregistered)}")

    for path in files:
        try:
            frontmatter, body = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        rel = path.relative_to(root).as_posix()
        for field in ("name", "author", "description"):
            if not frontmatter.get(field):
                errors.append(f"{rel}: missing frontmatter field {field}")
        if frontmatter.get("author") != "Tehseen Tech":
            errors.append(f"{rel}: author is not Tehseen Tech")
        if TRIGGER not in frontmatter.get("description", ""):
            errors.append(f"{rel}: automatic-trigger sentence missing from description")
        for heading in EXPECTED_HEADINGS:
            pattern = rf"^#{{1,6}}\s+.*\b{re.escape(heading)}\b"
            if not re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"{rel}: missing {heading} heading")

    tracked = tracked_files(root)
    for rel in tracked:
        if rel.suffix.lower() not in {".md", ".json", ".py", ".sh", ".yml", ".yaml", ".cff", ".txt"}:
            continue
        if rel == Path(__file__).resolve().relative_to(root):
            continue
        path = root / rel
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for stale in STALE_PATTERNS:
            if stale in text:
                errors.append(f"{rel}: stale public reference {stale!r}")

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {declared} skills, registry parity, frontmatter, trigger metadata, documentation headings, and stale-reference checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Lightweight validation for an intake-first-planner skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_LINKS = [
    "references/intake-workflow.md",
    "references/spatial-layout-domain.md",
    "references/prompt-to-skill.md",
    "references/skill-packaging.md",
    "schemas/intake_project.schema.yaml",
    "schemas/spatial_layout.schema.yaml",
    "examples/workstation_layout_request.yaml",
    "examples/furniture_layout_request.yaml",
    "examples/equipment_cable_routing_request.yaml",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must close with ---")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    skill = root / "SKILL.md"
    if not skill.exists():
        fail("missing SKILL.md")

    text = skill.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    name = fields.get("name")
    description = fields.get("description")
    if not name:
        fail("frontmatter missing name")
    if not description:
        fail("frontmatter missing description")
    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        fail(f"invalid skill name: {name!r}")

    for rel in REQUIRED_LINKS:
        if not (root / rel).exists():
            fail(f"missing referenced file: {rel}")

    linked_paths = sorted(set(re.findall(r"`((?:references|schemas|examples|scripts)/[^`]+)`", text)))
    for rel in linked_paths:
        if not (root / rel).exists():
            fail(f"SKILL.md links missing file: {rel}")

    examples = list((root / "examples").glob("*.yaml"))
    if len(examples) < 3:
        fail("expected at least three YAML examples to demonstrate reuse beyond one domain")

    openai_yaml = root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        openai_text = openai_yaml.read_text(encoding="utf-8")
        if f"${name}" not in openai_text:
            fail("agents/openai.yaml default prompt should mention the skill as $name")

    forbidden = [p for p in root.rglob("*") if p.suffix == ".jsonl"]
    if forbidden:
        fail("skill package must not include JSONL session logs")

    private_patterns = [
        re.compile(r"/Users/[^/\s]+"),
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"(?i)(password|secret|api[_-]?key)\s*[:=]\s*['\"]?[^'\"\s]+"),
    ]
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.relative_to(root).as_posix() == "scripts/check_skill_package.py":
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        content = path.read_text(encoding="utf-8")
        for pattern in private_patterns:
            if pattern.search(content):
                fail(f"possible private data in {path.relative_to(root)}")

    print(f"OK: {name} package passed lightweight validation")


if __name__ == "__main__":
    main()

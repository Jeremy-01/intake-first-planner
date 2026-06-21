# Skill Packaging

Use this reference when converting a prompt or workflow into a reusable Codex skill suitable for sharing or open-source release.

## Package Shape

Required:

- `SKILL.md` with YAML frontmatter containing `name` and `description`.

Recommended:

- `agents/openai.yaml` for UI metadata.
- `references/` for detailed domain/workflow docs loaded only when needed.
- `schemas/` for YAML/JSON templates.
- `examples/` for realistic but non-private example inputs.
- `scripts/` for deterministic checks or reusable generators.

Avoid clutter such as general README, changelog, installation guides, or project-management notes inside the skill folder. If a public repository needs those, keep them at repository root outside the skill package.

## Frontmatter

The description is the trigger surface. Include:

- What the skill does.
- When to use it.
- Key task types or domains.
- Important negative condition, if relevant.

Example:

```yaml
---
name: intake-first-planner
description: Use when building reusable planning, layout, optimization, simulation, or constraint-solver projects where missing parameters would make assumptions unsafe.
---
```

## Writing SKILL.md

Keep it short:

- Core rule.
- Workflow.
- Which reference files to read for which task.
- Output patterns.
- Bundled asset list.

Move long schemas, domain checklists, examples, and packaging details into references.

## Open-Source Readiness

Before sharing:

- Remove personal paths, private data, and old chat/session material.
- Keep examples synthetic or clearly anonymized.
- Run package validation.
- Confirm scripts are executable or have clear invocation.
- Add a license at repository root if publishing as a standalone repo.

## Validation Checklist

- `SKILL.md` exists.
- Frontmatter has `name` and `description`.
- Name is lowercase hyphen-case.
- Linked references, schemas, examples, and scripts exist.
- `agents/openai.yaml` default prompt mentions `$skill-name`.
- No `.jsonl`, chat exports, secrets, or private user data are included.

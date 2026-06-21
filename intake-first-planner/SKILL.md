---
name: intake-first-planner
description: Use when building reusable planning, layout, optimization, simulation, or constraint-solver projects where missing physical, business, or scenario parameters would make assumptions unsafe. Helps Codex first collect structured inputs, define schemas, avoid hidden assumptions, then scaffold implementation, tests, reports, and recovery docs.
---

# Intake-First Planner

Use this skill for projects that must not proceed from guessed parameters: physical layout planners, workstation or furniture arrangement tools, equipment placement, cable routing, schedule/resource optimization, simulation setup, and similar constraint-solving systems.

## Core Rule

Do not solve, optimize, recommend, or scaffold domain-specific logic until the required facts and scenarios are explicit enough to make assumptions unnecessary. If critical data is missing, output a "Missing Parameters" intake response and stop before implementation.

## Workflow

1. Classify the request:
   - **Intake only**: user wants requirements, schema, or prompt cleanup.
   - **Build after intake**: user wants code, tests, reports, or a reusable project.
   - **Skill authoring**: user wants a reusable/open-source skill or prompt package.
2. Select the relevant reference:
   - General reusable workflow: read `references/intake-workflow.md`.
   - Spatial/layout planners: read `references/spatial-layout-domain.md`.
   - Converting a one-off prompt into a reusable skill: read `references/prompt-to-skill.md`.
   - Skill packaging/open-source conversion: read `references/skill-packaging.md`.
3. Produce or update a structured fact source, usually YAML or JSON.
4. Gate execution:
   - If required facts are missing, return only the missing-parameter checklist, a suggested schema fragment, required scenarios, and explicit non-assumptions.
   - If facts are complete, implement the project using the fact source as authoritative input.
5. For Python projects, prefer `uv` commands. Always include `venv + pip` recovery commands in handoff/recovery docs.
6. Do not read old session JSONL, chat logs, or previous conversations unless the user explicitly asks for history recovery.

## Output Patterns

For missing input, use this shape:

```markdown
**Missing Parameters**
- ...

**Suggested YAML**
```yaml
...
```

**Scenarios To Confirm**
- ...

**Not Assumed**
- ...
```

For implementation, create a project with:

- `pyproject.toml`, `src/`, `tests/`, `examples/`, `reports/`, `outputs/`
- A structured config example as the single fact source
- Deterministic tests for parsing, transforms, constraints, scoring, and at least one scenario regression
- `HANDOFF.md`, `RECOVERY_README.md`, and `PROJECT_CONTEXT.md` with both `uv` and `venv + pip` commands

## Reusable Assets

- `schemas/intake_project.schema.yaml`: generic schema template.
- `schemas/spatial_layout.schema.yaml`: spatial/layout schema template.
- `examples/workstation_layout_request.yaml`: example domain request.
- `examples/furniture_layout_request.yaml`: room/furniture planning example.
- `examples/equipment_cable_routing_request.yaml`: equipment placement and cable-routing example.
- `scripts/check_skill_package.py`: lightweight package sanity checker.

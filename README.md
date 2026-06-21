# Intake-First Planner Skill

`intake-first-planner` is a reusable Codex skill for planning, layout, optimization, simulation, and constraint-solver projects where guessing missing parameters would be unsafe.

The skill turns one-off prompts into a schema-first workflow:

- collect required facts before solving,
- separate reusable workflow, domain template, and instance data,
- block implementation when critical parameters are missing,
- scaffold tested Python projects only after intake is complete,
- preserve recovery commands for both `uv` and `venv + pip`.

It includes reusable references for:

- general intake-first project workflows,
- spatial/layout planning,
- converting a long one-off prompt into a skill,
- packaging and validating an open-source Codex skill.

Example templates cover workstation layout, furniture layout, and equipment cable routing.

## Package

The skill package lives in:

```text
intake-first-planner/
```

It contains only skill-facing files: `SKILL.md`, references, schemas, examples, scripts, and agent metadata.

## Validate

```bash
python3 intake-first-planner/scripts/check_skill_package.py intake-first-planner
```

Expected output:

```text
OK: intake-first-planner package passed lightweight validation
```

## Example Invocation

```text
Use $intake-first-planner to convert this workstation layout prompt into a reusable schema-first skill and identify what data must be supplied before implementation.
```

## Suggested Repository Layout

```text
.
├── LICENSE
├── README.md
└── intake-first-planner/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── examples/
    ├── references/
    ├── schemas/
    └── scripts/
```

Thanks to CSZongzi for the early groundwork that helped shape this project.

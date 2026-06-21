# Intake Workflow

Use this reference when turning a narrow prompt into a reusable planning or solver workflow.

## Objective

Separate reusable agent behavior from domain facts and user-instance data:

1. **Agent workflow**: how to clarify, validate, build, test, and report.
2. **Domain template**: object types, constraints, scoring dimensions, and outputs.
3. **Instance data**: concrete user parameters and scenarios in YAML/JSON.

## Intake Gate

Before solving or coding, identify required facts:

- Coordinate system, units, boundaries, exclusions, and allowed operations.
- Objects/entities with dimensions, capacities, states, and identifiers.
- Constraints that are hard failures.
- Preferences that feed scoring.
- Scenarios/use cases with priorities.
- Output requirements and validation gates.

If a required fact is absent, do not infer a default. Ask for the missing fact or return a fillable schema.

## Schema Design

Prefer a schema that separates:

- `metadata`: project name, domain, units, version.
- `coordinate_system` or equivalent reference frame.
- `entities`: typed objects with IDs.
- `constraints`: hard constraints.
- `preferences`: scoring inputs.
- `scenarios`: explicit cases to solve.
- `outputs`: reports, visualizations, exports.
- `assumptions`: only user-approved assumptions, with source.

Each derived value should include a source:

```yaml
derived:
  value: 120
  method: "manufacturer spec minus clamp offset"
  source: "user supplied manual page 4"
```

## Missing-Parameter Response

Keep it actionable and concise:

- Group missing values by schema section.
- Mark blockers separately from optional refinements.
- Include a minimal YAML skeleton.
- List what will not be assumed.
- Ask the user to provide scenarios as separate items, not prose.

## Build Gate

Start implementation only when:

- Required hard constraints are known.
- At least one scenario is complete.
- Object IDs referenced by scenarios exist.
- Units and coordinate/reference frame are clear.
- The user has allowed any defaults that remain.

## Python Project Rules

- Prefer `uv`: `uv sync`, `uv run pytest`, `uv run python ...`.
- Recovery docs must include fallback:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

- Keep the structured config as the source of truth. Avoid duplicating facts in code.
- Tests should cover parsing, core transforms, constraints, scoring, and scenario regression.

## Session Boundary

Do not read old JSONL logs, previous chat exports, or hidden session files unless the user explicitly asks for historical recovery. Treat current workspace files and user-supplied configs as authoritative.

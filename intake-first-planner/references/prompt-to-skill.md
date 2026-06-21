# Prompt To Skill

Use this reference when a user has a long, narrow prompt and wants to make it reusable for other people or other domains.

## Split The Prompt

Extract four layers:

1. **Universal workflow**: rules that apply across domains, such as intake before solving, validation gates, structured configs, tests, and recovery docs.
2. **Domain module**: domain objects, constraints, scoring dimensions, and report expectations.
3. **Instance data**: the user's concrete dimensions, IDs, preferences, and scenarios.
4. **Packaging metadata**: skill name, trigger description, examples, references, and validation scripts.

Only layers 1, 2, and 4 belong in a skill. Layer 3 belongs in examples or user-provided configs.

## Remove Non-Reusable Content

Move these out of the main skill instructions:

- Personal machine paths.
- Specific device dimensions or model facts unless synthetic examples.
- One user's scenarios.
- Old chat/session history.
- Project-specific output folders.
- Any assumption that should instead be a required field.

## Generalize Carefully

Replace hard-coded nouns with typed objects:

- `monitor`, `arm`, `laptop` -> `object`, `mount`, `hinged object` in generic workflow.
- `desk` -> `space` or `surface`.
- `screen visibility` -> `line-of-sight or access requirement`.
- `ergonomic angle` -> `domain scoring metric`.

Keep a specialized reference for the original domain so the skill remains useful for that scenario.

## Build The Skill

Use this package shape:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── schemas/
├── examples/
└── scripts/
```

Write `SKILL.md` as routing instructions, not a full manual:

- When the skill applies.
- What must happen before implementation.
- Which reference to load for which domain/task.
- What outputs to produce.

## Migration Checklist

- The skill can handle at least two domains beyond the original prompt.
- The original prompt's domain still has a detailed reference or example.
- The skill blocks unsafe assumptions instead of making defaults.
- All examples are synthetic or anonymized.
- Validation checks linked files and rejects session logs.
- `agents/openai.yaml` has a default prompt mentioning `$skill-name`.

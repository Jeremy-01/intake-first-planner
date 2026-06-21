# Three.js Visualization

Use this reference when a planning project needs 3D output, visual reports, or beginner-friendly previews.

## Default Choice

Use Three.js as the default 3D visualization layer for browser-based reports. Prefer simple, inspectable geometry over realistic appearance:

- Boxes for objects, screens, furniture, equipment, and unavailable zones.
- Cylinders or capsules for tubes, arms, supports, and cables.
- Lines or curves for routes, sight lines, and cable paths.
- Transparent materials for collision volumes and clearances.

Do not require the user to know Three.js. Ask for real-world facts, then generate the viewer from the structured config.

## Output Files

For layout or spatial solver projects, produce:

- `reports/<scenario>.html`: human-readable report.
- `reports/<scenario>_top.svg` or embedded top-view SVG.
- `outputs/<scenario>_3d.html`: standalone Three.js viewer.
- `outputs/<scenario>_results.json`: machine-readable solved poses, scores, and violations.

Keep the report simple: top view first, tables second, checks third, 3D entry last.

## Viewer Requirements

The viewer should include:

- Orbit camera controls.
- Grid and axis helper with units labeled in the report.
- Toggleable layers: objects, clearances, disabled zones, sight lines/routes, violations.
- Color legend.
- Object labels or hover tooltips.
- A reset-camera button.

For beginner users, include plain labels such as "wall", "desk edge", "blocked area", and "recommended position".

## Implementation Guidance

- Use generated HTML plus JavaScript unless the project already has a frontend stack.
- Load Three.js from a pinned CDN URL or local bundled asset; document the choice.
- Keep geometry generated from solver output, not duplicated hand-coded coordinates.
- Make collision boxes visually match the geometry used by the solver.
- Add a smoke test that checks the generated HTML references Three.js and includes at least one object from the scenario.

## When Not To Use Three.js

- Use SVG only for simple 2D diagrams.
- Consider Babylon.js only if the user asks for heavier engine features.
- Consider Godot only for a standalone app or game-like editor.

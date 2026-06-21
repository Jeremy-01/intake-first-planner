# Spatial Layout Domain

Use this reference for desk, room, workstation, equipment, cable, or other physical layout planners.

## Required Inputs

### Space

- Dimensions and units.
- Origin definition and axis directions.
- Fixed boundaries: walls, edges, open sides, doors, shelves, columns.
- Disabled or reserved regions.
- Allowed overhang directions and limits.
- Clearance requirements for object-object, object-wall, and object-edge checks.

### Objects

For each object:

- Stable `id`.
- Physical dimensions and weight when relevant.
- Pose variables: allowed x/y/z, yaw/pitch/roll, height, or attachment points.
- Collision geometry: rectangle, box, capsule, cylinder, segment, or mesh approximation.
- Operational constraints: access, cooling, visibility, load, cable reach, door swing.
- Source for any derived geometry.

### Mounts, Arms, Supports

For articulated or attached hardware:

- Candidate base/clamp positions.
- Attachment edge constraints.
- Load range.
- Segment lengths or ranges.
- Joint yaw/pitch/height ranges.
- Adapter lengths and offsets.
- Tube/capsule radius or collision boxes.
- Fold/preferred direction if it affects scoring.

### Humans and Sight Lines

- Seating/standing candidate positions.
- Eye position as a range or volume, not a single point.
- Preferred viewing distance.
- Acceptable yaw/head-turn ranges.
- Visibility requirements and occluders.

### Scenarios

Each scenario needs:

- `id`.
- Active objects.
- Primary/secondary relationships.
- Required accessories or access zones.
- Human position/range.
- Hard constraints.
- Scoring priorities.
- Special constraints.

## Modeling Guidance

- Use structured geometry objects, not ad hoc strings.
- Use oriented rectangles/boxes for flat objects.
- Use capsules for arms/tubes when exact geometry is unnecessary.
- Model hinged objects, such as laptops, as multiple rigid bodies.
- Represent unavailable zones as boxes or polygons with z-ranges.
- Keep collision clearance explicit and scenario-aware.

## Constraint Classes

Hard constraints:

- Boundary violations.
- Disabled-region intersection.
- Collision after clearance inflation.
- Load/capacity violations.
- Joint range violations.
- Required access/cooling/visibility failures.

Soft scoring:

- Ergonomic angle and viewing distance.
- Preserved workspace area.
- Proximity to wall or desired edge.
- Symmetry/alignment.
- Cable/mount fold preference.
- Mouse/keyboard/trackpad comfort.

## Report Requirements

For each solved scenario, report:

- Top-view SVG or HTML first.
- Parameter summary.
- Recommended install/base points.
- Object centers, orientation, height, and attachment details.
- Collision and visibility check results.
- Score breakdown.
- Pros/cons.
- Link or entry point for simplified 3D model if requested.

Style: light background, white cards, concise sections, visual first, analysis second, 3D last.

## Workstation Layout Specialization

For monitor-arm workstation planning, require:

- Table width/depth/top height, coordinate frame, walls, disabled zones, mounting edges, allowed overhang, base and collision clearances.
- Arm brand/model or equivalent geometry: clamp candidates, edge constraints, load, segment ranges, height/yaw/pitch ranges, VESA adapter, tube radius/collision boxes.
- Monitor width/height/thickness/weight/VESA, allowed overhang, target center or bottom height, yaw and x/y ranges.
- Laptop dimensions, lid angle range, camera/Touch ID/keyboard access, stand footprint/height, cooling clearance.
- Keyboard, mouse area, and trackpad dimensions plus relative placement.
- Human eye-position range, seating candidates, viewing distance, ergonomic yaw range, head-turn limits.
- Explicit scenarios with primary monitor, secondary relation, active laptop/accessories, priorities, and special constraints.

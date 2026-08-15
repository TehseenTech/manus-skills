# Automatic Trigger Audit Baseline

## User requirement
Make all skills automatically usable from natural user requests without requiring the user to mention or ask for a specific skill.

## Scope
- Repository checkout: `/home/ubuntu/manus-skills`
- Repository skill files: 78 total, including `meta-skills/full-stack-builder/SKILL.md`
- Registry total: 78
- Installed Manus skill files: 50 under `/home/ubuntu/skills`

## Baseline checks
- Frontmatter failures across repository + installed collection: 2 (both in repository utility skills)
- Descriptions without `Use when` or `Use for`: 50
- Descriptions without any trigger signal: 44

## Planned change
- Preserve each skill's existing name and description content.
- Add one automatic-discoverability sentence to each description: `Apply automatically when the request matches; the user does not need to mention this skill.`
- Add missing frontmatter to `debug-mining-engine` and `skill-arsenal-builder` using directory names and source-derived descriptions.
- Synchronize `skills.json` descriptions with the updated repository frontmatter.
- Apply the same trigger clarification to installed skills under `/home/ubuntu/skills` so the active runtime metadata does not require explicit skill naming.
- Validate YAML/frontmatter, registry consistency, duplicate names, and all skill-creator package structures.

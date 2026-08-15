# Skill Finder

Use this guide when you know the outcome you want but do not know the internal skill name. The canonical source is [`skills.json`](../skills.json); the shell helper [`skills-quick-ref.sh`](../skills-quick-ref.sh) provides a compact local catalog.

## Find by outcome

| Outcome | Start with | Category |
|---|---|---|
| Investigate before changing an existing system | [`investigate-before-recommend`](../skills/analysis-skills/investigate-before-recommend/SKILL.md) | Analysis |
| Diagnose a difficult technical problem | [`systematic-debugging`](../skills/workflow-skills/systematic-debugging/SKILL.md) | Workflow |
| Split independent work into parallel workstreams | [`dispatching-parallel-agents`](../skills/workflow-skills/dispatching-parallel-agents/SKILL.md) | Workflow |
| Verify a feature before declaring it complete | [`feature-verification`](../skills/workflow-skills/feature-verification/SKILL.md) | Workflow |
| Create or improve a reusable skill | [`skill-creator`](../skills/utility-skills/skill-creator/SKILL.md) | Utility |
| Find an existing open-source implementation | [`github-gem-seeker`](../skills/automation-skills/github-gem-seeker/SKILL.md) | Automation |
| Build a professional workbook | [`excel-generator`](../skills/design-skills/excel-generator/SKILL.md) | Design |
| Design a polished frontend | [`frontend-design`](../skills/design-skills/frontend-design/SKILL.md) | Design |
| Build a backend endpoint | [`api-endpoint-builder`](../skills/tier1-foundation/api-endpoint-builder/SKILL.md) | Tier 1 · Foundation |
| Design a database schema | [`database-schema-generator`](../skills/tier1-foundation/database-schema-generator/SKILL.md) | Tier 1 · Foundation |
| Build a secure connector or integration | [`mcp-builder`](../skills/integration-skills/mcp-builder/SKILL.md) | Integration |
| Generate or edit a video | [`video-generator`](../skills/design-skills/video-generator/SKILL.md) | Design |

## Find by category

The current registry contains 78 skills across 13 categories. Open the registry entry or browse the corresponding directory.

| Category | Count | Directory |
|---|---:|---|
| Analysis | 8 | [`skills/analysis-skills`](../skills/analysis-skills) |
| Automation | 6 | [`skills/automation-skills`](../skills/automation-skills) |
| Design | 8 | [`skills/design-skills`](../skills/design-skills) |
| Development | 6 | [`skills/development-skills`](../skills/development-skills) |
| Integration | 6 | [`skills/integration-skills`](../skills/integration-skills) |
| Specialized | 2 | [`app-store-submission-packager`](../app-store-submission-packager) and [`work-access-demo-generator`](../work-access-demo-generator) |
| Tier 1 · Foundation | 3 | [`skills/tier1-foundation`](../skills/tier1-foundation) |
| Tier 2 · Automation | 3 | [`skills/tier2-automation`](../skills/tier2-automation) |
| Tier 3 · Advanced | 4 | [`skills/tier3-advanced`](../skills/tier3-advanced) |
| Tier 4 · Specialized | 5 | [`skills/tier4-specialized`](../skills/tier4-specialized) |
| Utility | 12 | [`skills/utility-skills`](../skills/utility-skills) |
| Workflow | 14 | [`skills/workflow-skills`](../skills/workflow-skills) |
| Meta-skills | 1 | [`meta-skills`](../meta-skills) |

## Search locally

From the repository root:

```bash
# Search descriptions and instructions for a keyword.
grep -RIl --include='SKILL.md' -i 'keyword' skills meta-skills

# Browse the compact catalog.
bash skills-quick-ref.sh

# Inspect the canonical registry.
python3 -m json.tool skills.json | less
```

For a direct request, describe the target outcome, constraints, environment, and desired output. The collection’s automatic-discovery sentence means that users do not need to name a skill explicitly, but the request still needs enough context for a reliable match.

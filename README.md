# Tehseen Tech · Manus Skills

> A curated, automatically discoverable collection of reusable Manus AI agent skills for research, development, automation, design, integrations, and workflow orchestration.

**Maintained and packaged by Tehseen Tech** · **78 registered skills** · **13 categories** · **1 meta-skill**

[![Registry](https://img.shields.io/badge/registry-78%20skills-1B5E20)](skills.json)
[![Automatic discovery](https://img.shields.io/badge/discovery-automatic-C2185B)](skills.json)
[![Repository](https://img.shields.io/badge/GitHub-public-24292F)](https://github.com/TehseenTech/manus-skills)

## Overview

The **Tehseen Tech edition of Manus Skills** organizes reusable agent capabilities into a searchable registry and a consistent `SKILL.md` contract. Each skill explains what it does, the requests it handles, and when it should be considered automatically. Users can describe the outcome they need without first naming an internal skill.

The collection is designed for composable work. Individual skills can be discovered by category, combined into workflows, and validated against the central `skills.json` manifest. The repository also includes a meta-skill for orchestrating larger full-stack builds.

## Current release

| Metric | Value |
|---|---:|
| Registered skills | **78** |
| Skill files on disk | **78** |
| Categories | **13** |
| Meta-skills | **1** |
| Automatic-trigger coverage | **100% of validated files** |
| Registry path errors | **0** |
| Frontmatter errors | **0** |
| Latest local commit | Updated in the current release commit |

The registry is the source of truth for names, descriptions, categories, paths, dependencies, and complementary skills. The current repository includes five top-level skills in addition to the nested category directories; all 78 are represented in the manifest.

## Skill categories

| Category | Skills |
|---|---:|
| Analysis | 8 |
| Automation | 6 |
| Design | 8 |
| Development | 6 |
| Integration | 6 |
| Specialized | 2 |
| Tier 1 · Foundation | 3 |
| Tier 2 · Automation | 3 |
| Tier 3 · Advanced | 4 |
| Tier 4 · Specialized | 5 |
| Utility | 12 |
| Workflow | 14 |
| Meta-skills | 1 |

## Automatic discovery contract

Every skill uses frontmatter with a stable `name`, an authorship field, and a request-oriented `description`. Descriptions include the following activation rule:

> Apply automatically when the request matches; the user does not need to mention this skill.

This improves routing without pretending that every ambiguous request can be resolved mechanically. The request still needs enough context to match the skill’s capability and intended workflow.

## Repository structure

```text
.
├── skills.json                         # Canonical registry and dependency metadata
├── ARCHITECTURE.md                     # Registry and composition architecture
├── lib/                                # Registry, composer, utilities, and validator
├── meta-skills/full-stack-builder/     # Full-stack orchestration meta-skill
├── skills/                             # Categorized skill definitions
├── app-store-submission-packager/      # Top-level skill definition
├── digital-product-inventor/           # Top-level skill definition
├── ios-testflight-github-actions/      # Top-level skill definition
├── meta-ads-analyzer/                  # Top-level skill definition
├── work-access-demo-generator/         # Top-level skill definition
├── scripts/                            # Repository maintenance helpers
├── docs/                               # Public report and validation artifacts
├── LICENSE                             # MIT repository license
└── TEHSEEN_TECH.md                     # Branding and attribution notes
```

Each skill directory contains a `SKILL.md` file. Some skills also include scripts, references, templates, examples, or integration-specific resources.

## Quick start

### Explore the registry

```python
from lib.skill_registry import SkillRegistry

registry = SkillRegistry("skills.json")
print(registry.get_stats())
print(registry.find_by_category("workflow-skills"))
print(registry.find_by_tag("database"))
```

### Compose a workflow

```python
from lib.skill_registry import SkillRegistry
from lib.skill_composer import SkillComposer

registry = SkillRegistry("skills.json")
composer = SkillComposer(registry)

workflow = composer.compose_workflow([
    "database-schema-generator",
    "api-endpoint-builder",
    "testing-framework",
])

print(workflow["valid"])
print(workflow["dependencies"])
```

### Work with a skill directly

Read the relevant `SKILL.md` file for its scope, workflow, scripts, references, and expected outputs. The user does not need to mention the skill name when working through an agent that supports automatic discovery.

## Maintenance and validation

Keep `skills.json` synchronized with the on-disk skill definitions. Before publishing changes, validate that every registry path exists, every skill has valid frontmatter, every description includes the automatic-trigger contract, and every dependency reference resolves.

The repository’s core Python modules are available under `lib/`. The reusable `skill-registry-auditor` and `repository-to-skill` packages are maintained in the local Manus skills collection and provide more extensive reconciliation and repository-extraction workflows.

## Public release downloads

- [Tehseen Tech · Manus Skills PDF report](docs/tehseen-tech-manus-skills-report.pdf)
- [Automatic-trigger validation JSON](docs/auto-trigger-validation.json)
- [Automatic-trigger audit notes](docs/automatic-trigger-audit.md)
- [Final Tehseen Tech release audit](docs/final-tehseen-release-audit.json)

## Contributing

For a new skill, begin with the `skill-creator` workflow, write a complete `SKILL.md`, add any supporting scripts or references, update `skills.json`, and run the full registry audit. Keep descriptions specific enough for automatic discovery and document any external service, credential, or platform assumptions.

Before submitting a change, confirm that:

1. The skill has valid YAML frontmatter with `name`, `author`, and `description`.
2. The description states the capability, matching context, and automatic activation rule.
3. All referenced scripts, templates, and documents exist.
4. The registry path and metadata match the filesystem.
5. No secrets or private user data are included.

## License and public use

This repository is released under the [MIT License](LICENSE), with **Tehseen Tech** listed as the repository-level copyright holder for the Tehseen Tech edition and its original contributions. The MIT License permits reuse, modification, redistribution, and commercial use subject to its notice and warranty terms.

The repository-level license does not override separate terms that may apply to individual upstream skills, embedded assets, dependencies, external services, or third-party integrations. Review local notices and upstream licenses before redistributing or commercializing a particular component.

## Attribution

This edition is **curated, branded, and maintained by Tehseen Tech**. See [`TEHSEEN_TECH.md`](TEHSEEN_TECH.md) for the branding and maintenance scope.

## References

- [Architecture guide](ARCHITECTURE.md)
- [Canonical skill registry](skills.json)
- [MIT License](LICENSE)
- [GitHub repository](https://github.com/TehseenTech/manus-skills)

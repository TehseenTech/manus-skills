# Tehseen Tech · Manus Skills

> **78 reusable Manus AI agent skills for research, development, automation, design, integrations, and repeatable workflows—discoverable from the user’s request instead of a memorized skill name.**

[![78 skills](https://img.shields.io/badge/skills-78-1B5E20)](skills.json)
[![Automatic discovery](https://img.shields.io/badge/discovery-automatic-C2185B)](skills.json)
[![MIT License](https://img.shields.io/badge/license-MIT-24292F)](LICENSE)
[![Validation](https://github.com/TehseenTech/manus-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/TehseenTech/manus-skills/actions/workflows/validate-skills.yml)
[![Latest release](https://img.shields.io/github/v/release/TehseenTech/manus-skills?display_name=tag&sort=semver)](https://github.com/TehseenTech/manus-skills/releases)

**Maintained, validated, and packaged by [Tehseen Tech](TEHSEEN_TECH.md).** If this collection saves you time, [star the repository](https://github.com/TehseenTech/manus-skills), share a specific use case, or propose a skill that is missing.

## Start in one minute

Clone the public collection, validate the registry, and inspect the skill catalog:

```bash
git clone https://github.com/TehseenTech/manus-skills.git
cd manus-skills
python3 scripts/validate-repository.py
bash skills-quick-ref.sh
```

For a terminal integration with `skill`, `skills-list`, `skills-search`, and `skills-update` commands, review [`install-skills.sh`](install-skills.sh) and run it locally:

```bash
bash install-skills.sh
source ~/.skills-integration.sh
skill systematic-debugging
```

The installer is optional. You can also read any `SKILL.md` directly, use the canonical registry, or copy only the skill directories relevant to your workflow.

## What this collection does

Manus Skills are reusable instruction packages that combine a request-oriented description with workflows, scripts, references, templates, and validation guidance. The collection is designed for agents that support skill discovery and composition. You describe the outcome you need; the matching skill can be considered automatically when the request fits its capability.

> **Automatic-discovery contract:** Apply automatically when the request matches; the user does not need to mention this skill.

Automatic discovery is not a promise that every ambiguous request can be routed perfectly. The request still needs enough context to match the skill’s scope, and users should review external-service assumptions, credentials, scripts, and generated actions before production use.

## Pick a starting point

| If you need to… | Start with | Why it is useful |
|---|---|---|
| Investigate an existing system before recommending changes | [`investigate-before-recommend`](skills/analysis-skills/investigate-before-recommend/SKILL.md) | Reduces duplicated work and recommendation drift |
| Debug a complex problem systematically | [`systematic-debugging`](skills/workflow-skills/systematic-debugging/SKILL.md) | Provides a repeatable diagnosis and verification workflow |
| Split a large task across independent workstreams | [`dispatching-parallel-agents`](skills/workflow-skills/dispatching-parallel-agents/SKILL.md) | Makes parallel research and implementation explicit |
| Verify that a feature is actually complete | [`feature-verification`](skills/workflow-skills/feature-verification/SKILL.md) | Turns completion into an evidence-based check |
| Create a new reusable Manus skill | [`skill-creator`](skills/utility-skills/skill-creator/SKILL.md) | Guides skill design, metadata, resources, and validation |
| Find an existing open-source solution first | [`github-gem-seeker`](skills/automation-skills/github-gem-seeker/SKILL.md) | Searches for battle-tested tools before custom implementation |
| Build a professional spreadsheet or analysis workbook | [`excel-generator`](skills/design-skills/excel-generator/SKILL.md) | Combines structured data work with presentation quality |
| Design a polished interface | [`frontend-design`](skills/design-skills/frontend-design/SKILL.md) | Provides a practical interface design and implementation workflow |

## Browse all 78 skills

The [`skills.json`](skills.json) file is the canonical registry for names, descriptions, categories, paths, authorship, dependencies, and complementary skills. The collection is organized into 13 categories:

| Category | Count |
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

For a compact catalog, open [`skills-quick-ref.sh`](skills-quick-ref.sh). For architecture and composition details, read [`ARCHITECTURE.md`](ARCHITECTURE.md). For the complete release inventory, download the [Tehseen Tech Manus Skills PDF report](docs/tehseen-tech-manus-skills-report.pdf).

## Compose a workflow

The Python registry and composer make it possible to inspect categories and validate a multi-skill workflow:

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

The repository also includes [`docs/quickstart.md`](docs/quickstart.md) with copy-paste examples for registry browsing, direct skill reading, validation, and safe composition.

## Quality and release trust

The public release includes a canonical registry, 78 on-disk `SKILL.md` files, automatic-trigger metadata, documentation coverage, referenced resource directories, validation artifacts, a professional report, and a standard MIT license. The repository-local validator runs on pushes and pull requests through [GitHub Actions](.github/workflows/validate-skills.yml).

Useful artifacts include:

- [Final Tehseen Tech release audit](docs/final-tehseen-release-audit.json)
- [Automatic-trigger validation](docs/auto-trigger-validation.json)
- [Automatic-trigger audit notes](docs/automatic-trigger-audit.md)
- [Professional PDF report](docs/tehseen-tech-manus-skills-report.pdf)
- [Release notes](RELEASE_NOTES_v1.0.0.md)
- [Changelog](CHANGELOG.md)

## Contributing

The project welcomes focused improvements, new skills, validation fixes, and documentation contributions. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request. Use the issue templates for reproducible bugs and feature proposals, and never include credentials or private client data in public issues.

A high-quality skill contribution includes valid YAML frontmatter, a specific request-oriented description, the automatic-trigger sentence, `Overview`, `Workflow`, and `Usage` documentation, all referenced resources, a matching `skills.json` entry, and a validation result.

## Support and security

Use [`SUPPORT.md`](SUPPORT.md) for issue routing and troubleshooting. Report suspected vulnerabilities privately according to [`SECURITY.md`](SECURITY.md). Community participation follows the standards in [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Public launch and responsible sharing

This is a new public Tehseen Tech release. Please do not treat repository size, stars, forks, or download counts as quality guarantees. If you share it, describe the concrete workflow it helped with and link to the relevant skill. Prepared launch copy and platform-specific messaging are available in [`launch/launch-kit.md`](launch/launch-kit.md); external posting remains the responsibility of the person choosing to publish it.

## License and attribution

This repository is released under the [MIT License](LICENSE), with **Tehseen Tech** listed as the repository-level copyright holder for the Tehseen Tech edition and its original contributions. The repository-level license does not override separate terms that may apply to upstream skills, embedded assets, dependencies, external services, or third-party integrations.

See [`TEHSEEN_TECH.md`](TEHSEEN_TECH.md) for branding and maintenance scope.

## References

- [Canonical skill registry](skills.json)
- [Architecture guide](ARCHITECTURE.md)
- [Contribution guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)
- [GitHub repository](https://github.com/TehseenTech/manus-skills)

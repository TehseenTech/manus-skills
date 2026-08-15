# Quickstart

This guide shows how to explore and use the Tehseen Tech Manus Skills collection without requiring a user to memorize internal skill names.

## 1. Clone and validate

```bash
git clone https://github.com/TehseenTech/manus-skills.git
cd manus-skills
python3 scripts/validate-repository.py
```

The validator checks the registry count, on-disk `SKILL.md` parity, frontmatter, Tehseen Tech authorship, the automatic-trigger contract, required documentation headings, and stale inherited repository references.

## 2. Browse the registry

```python
from lib.skill_registry import SkillRegistry

registry = SkillRegistry("skills.json")
print(registry.get_stats())
print(registry.find_by_category("workflow-skills"))
```

The registry is the source of truth for skill names, descriptions, categories, paths, dependencies, and complementary skills.

## 3. Read a skill directly

```bash
less skills/workflow-skills/systematic-debugging/SKILL.md
```

Each skill explains its scope, workflow, usage, resources, and expected outputs. Choose the skill based on the user outcome, not only the directory name.

## 4. Compose compatible skills

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

if not workflow["valid"]:
    raise SystemExit(workflow)

print(workflow["dependencies"])
```

## 5. Optional terminal integration

Review the installer before running it, then execute it locally:

```bash
less install-skills.sh
bash install-skills.sh
source ~/.skills-integration.sh
skill systematic-debugging
skills-search database
skills-stats
```

The installer clones the public Tehseen Tech repository into `~/skills` and creates convenience shell functions. It is optional; direct reading and registry access remain supported.

## 6. Create or improve a skill

Read [`CONTRIBUTING.md`](../CONTRIBUTING.md) and start with [`skill-creator`](../skills/utility-skills/skill-creator/SKILL.md). A contribution must include valid frontmatter, request-oriented matching language, the automatic-trigger sentence, documentation headings, existing referenced resources, and a matching registry entry.

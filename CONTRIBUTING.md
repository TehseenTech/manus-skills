# Contributing to Tehseen Tech Manus Skills

Thank you for helping improve this public collection of reusable Manus AI agent skills. Contributions are welcome when they make a workflow clearer, safer, more reusable, or easier to discover.

## Start with a focused change

Before opening an issue or pull request, search the existing [`skills.json`](skills.json) registry and the skill directories. A new contribution should solve a distinct problem, improve an existing skill with evidence, or repair a documentation, validation, or installation issue.

For a new skill, begin with the [`skill-creator`](skills/utility-skills/skill-creator/SKILL.md) workflow. Keep the skill directory self-contained and include a complete `SKILL.md` with YAML frontmatter, a precise request-oriented description, and the standard automatic-discovery sentence:

> Apply automatically when the request matches; the user does not need to mention this skill.

## Required structure

A skill contribution should satisfy the following requirements:

| Requirement | Standard |
|---|---|
| Frontmatter | Include `name`, `author`, and `description` with valid YAML |
| Description | State the capability, matching context, and automatic-trigger contract |
| Documentation | Include `Overview`, `Workflow`, and `Usage` sections where appropriate |
| Resources | Ensure every referenced script, template, reference, or document exists |
| Registry | Add or update the matching entry in [`skills.json`](skills.json) |
| Safety | Do not include secrets, private user data, malware, or unverifiable claims |
| Licensing | Respect the MIT license and any separate upstream or asset terms |

## Validation before submission

Run the lightweight checks that apply to your change:

```bash
bash -n install-skills.sh auto-install-skills.sh skills-quick-ref.sh scripts/enable-auto-skill-updates.sh
python3 -m json.tool skills.json >/dev/null
```

If you change a skill or the registry, also run the repository’s independent 78-skill audit from a local Manus environment when available. Describe the command and result in the pull request.

## Pull requests

Use a descriptive title such as `feat: add <skill-name>` or `fix: repair <skill-name> documentation`. Explain the user problem, the behavior or documentation change, the files touched, and the validation performed. Keep unrelated formatting changes out of the same pull request.

A maintainer may request revisions, additional examples, clearer safety boundaries, or a narrower scope. Review is collaborative and focused on the quality and maintainability of the public collection.

## Issues and suggestions

Use the issue templates for reproducible defects and focused feature requests. For general questions, consult [`SUPPORT.md`](SUPPORT.md). Do not include credentials, private client information, or sensitive logs in public issues.

## Recognition

Contributors are credited through GitHub’s normal contribution history and release notes when appropriate. The repository is maintained and packaged by **Tehseen Tech** under the [MIT License](LICENSE).

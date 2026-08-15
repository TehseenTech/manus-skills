# Tehseen Tech Manus Skills — Repository Growth Package Design

## Goal

Make `TehseenTech/manus-skills` easier to discover, understand, install, trust, contribute to, and share, without inventing adoption metrics or posting unsolicited promotion to third-party communities.

## Evidence-based positioning

The repository is a public collection of 78 reusable Manus AI agent skills with automatic-trigger metadata, a canonical registry, validation artifacts, a professional PDF report, and MIT licensing. The first screen should state that value directly and show a verified path from discovery to first use.

## Implementation package

| Workstream | Files or settings | Outcome |
|---|---|---|
| README conversion | `README.md`, `docs/quickstart.md`, `docs/showcase.md` | A sharper first screen, one-minute install path, real flagship examples, registry links, validation proof, and clear calls to star, fork, discuss, and contribute |
| Community health | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/feature_request.yml`, `.github/ISSUE_TEMPLATE/config.yml` | Lower-friction contributions and safer issue intake |
| Public trust | `CHANGELOG.md`, `RELEASE_NOTES_v1.0.0.md`, `CITATION.cff`, `.github/dependabot.yml`, `.github/workflows/validate-skills.yml` | Clear release identity, citation path, dependency-update posture, and repeatable validation |
| Discoverability | GitHub description, homepage, topics, README keywords, `docs/skill-finder.md` | Better search and browsing for people looking for Manus, agent, automation, workflow, and developer skills |
| Install reliability | `install-skills.sh`, `auto-install-skills.sh`, `scripts/enable-auto-skill-updates.sh`, `skills-quick-ref.sh` | Remove inherited owner and outdated count references; point all public paths to `TehseenTech/manus-skills` and the current 78-skill release |
| Shareable assets | `assets/tehseen-tech-manus-skills-social-preview.png`, `launch/launch-kit.md` | A factual social-preview image and ready-to-review launch copy for GitHub, LinkedIn, X, newsletters, and developer communities |
| Release surface | Git tag `v1.0.0`, GitHub release with notes and PDF attachment | A stable, shareable public release without overstating adoption |

## README information architecture

1. One-sentence definition and the 78-skill count.
2. Trust badges for license, registry validation, and latest release only where the links are real.
3. One-minute installation path with a verified command and a manual alternative.
4. “What can I do with this?” showcase using real skills from the registry.
5. Automatic-discovery contract and how skill matching works.
6. Browse by category and use the canonical `skills.json` registry.
7. Validation and quality controls.
8. Contributing, support, security, license, and Tehseen Tech attribution.
9. Ethical launch call to action: star if useful, open an issue for a missing skill, and share the repository with context.

## Real showcase candidates

- `investigate-before-recommend`: investigate existing infrastructure before proposing changes.
- `systematic-debugging`: structured debugging workflow.
- `dispatching-parallel-agents`: parallel task decomposition.
- `feature-verification`: verify a feature before completion.
- `skill-creator`: create reusable Manus skills.
- `github-gem-seeker`: locate battle-tested open-source solutions.
- `excel-generator`: create professional spreadsheets and analysis.
- `frontend-design`: design and implement polished interfaces.

## Safety and publicity boundary

Repository changes, release metadata, and prepared launch assets may be published as part of this task. No unsolicited posts, direct messages, forum submissions, or claims about stars, users, testimonials, benchmarks, or community adoption will be made. External promotion remains a user-controlled follow-up step.

## Validation gate

Before publishing, verify that all 78 skills remain present, the registry remains aligned, automatic-trigger metadata remains complete, all documentation headings and referenced resource directories remain valid, stale owner/count references are gone from public scripts, YAML files parse, shell scripts pass `bash -n`, and the final working tree contains no task-state files.

## Sources

- [GitHub repository best practices](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [GitHub community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [GitHub repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [GitHub social previews](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [Anthropic Agent Skills](https://github.com/anthropics/skills)
- [VoltAgent Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills)
- [Softaworks Agent Toolkit](https://github.com/softaworks/agent-toolkit)

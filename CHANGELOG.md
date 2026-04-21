# Changelog

All notable changes to this project will be documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Planned for v0.2.0
- New profiles: security, mobile-dev, game-dev, educator, legal-advisor
- Translation support starting with Malayalam

---

## [0.1.3] - 2026-04-21

### Added

- Developer profile: data-engineer
- Issue templates: CI and documentation

### Fixed

- `cspell.json` missing technical terms: nullable, subqueries, DAGs, CTE, ELT,
  idempotency, Automatic1111
- `lint.yml` and `spellcheck.yml` path filters removed so required checks always
  report status on every PR
- `labeler.yml` feature label now uses head-branch only — profile edits no longer
  incorrectly trigger a minor version bump
- `labeler.yml` ci label now covers `.github/scripts/` path
- `stale.yml` exempt label fixed and needs-work label added to PR exemptions
- `pr-greeting.yml` contributor threshold aligned between open and merge jobs
- `check_profile.py` header field checks scoped to metadata block only
- `check_profile.py` Extends validation uses pathlib to block path traversal
- `check_profile.py` now validates header fields have non-empty values
- `check_profile.py` Extends field checked against filesystem
- `validate.yml` README index check scoped to Profile index section and uses
  markdown link format matching
- `validate.yml` added CI step to verify profiles are listed in README index
- `coderabbit.yaml` translation files excluded from English review instructions
- `fullstack.md` Extends field corrected to universal.md
- `release.yml` stale version comment updated

### Changed

- ROADMAP.md: data-engineer marked complete
- CONTRIBUTING.md: Extends field rules documented, branch naming clarified

---

## [0.1.0] - 2026-04-05

### Added

- Universal base profile
- Casual user profile
- Developer profiles: frontend, backend, fullstack, devops
- Analyst profile
- Agent profile
- Advisor profile
- Writer profile
- Image generation profile with per-tool notes
- Free resources directory
- GitHub Actions: lint, spellcheck, validate, stale, label, release
- CodeRabbit AI review integration
- Community files: CONTRIBUTING, CODE_OF_CONDUCT, SECURITY
- Issue templates: bug report, new profile, improvement
- PR template with human verification checkbox
- CODEOWNERS protection
- ROADMAP

---

[Unreleased]: https://github.com/muhammedshihab1001/promptcraft/compare/v0.1.3...HEAD
[0.1.3]: https://github.com/muhammedshihab1001/promptcraft/compare/v0.1.0...v0.1.3
[0.1.0]: https://github.com/muhammedshihab1001/promptcraft/releases/tag/v0.1.0

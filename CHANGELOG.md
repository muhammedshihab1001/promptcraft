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

## [0.1.2] - 2026-04-21

### Fixed

- `validate.yml` README index check now matches markdown link format and scopes
  to the Profile index section only
- `check_profile.py` header field checks now scoped to leading metadata block only
- `check_profile.py` Extends validation uses `pathlib` to block path traversal
  and directory matches
- `lint.yml` and `spellcheck.yml` path filters removed so required checks always
  report status on every PR

---

## [0.1.1] - 2026-04-21

### Added

- Developer profile: data-engineer

### Fixed

- `cspell.json` missing technical terms: nullable, subqueries, DAGs, CTE, ELT,
  idempotency, Automatic1111
- `lint.yml` and `spellcheck.yml` incorrect `.yml` path trigger removed
- `release.yml` stale version comment updated
- `labeler.yml` ci label now covers `.github/scripts/` path
- `stale.yml` exempt label fixed from `good-first-issue` to `good first issue`
- `pr-greeting.yml` contributor threshold aligned between open and merge jobs
- `check_profile.py` now validates header fields have non-empty values
- `check_profile.py` Extends field now checked against filesystem
- `validate.yml` added CI step to verify profiles are listed in README index
- `coderabbit.yaml` translation files excluded from English review instructions
- `fullstack.md` Extends field corrected from multi-parent format to `universal.md`

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

[Unreleased]: https://github.com/muhammedshihab1001/promptcraft/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/muhammedshihab1001/promptcraft/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/muhammedshihab1001/promptcraft/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/muhammedshihab1001/promptcraft/releases/tag/v0.1.0

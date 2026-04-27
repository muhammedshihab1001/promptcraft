# Roadmap

## v0.1.0 - Foundation (current)

- [x] Core profiles: universal, casual-user, developer, analyst, agent, advisor, writer
- [x] Image generation profile
- [x] Free resources directory
- [x] GitHub Actions: lint, spellcheck, validate, stale, label, release
- [x] Community files: CONTRIBUTING, CODE_OF_CONDUCT, SECURITY
- [x] Issue templates, PR template
- [x] CodeRabbit integration

## v0.2.0 - More profiles

Priority order — start from the top:

- [x] **data-engineer** — highest demand, most requested
- [x] **security** — pen testing, threat modeling
- [x] mobile-dev — iOS, Android, React Native
- [x] game-dev — game design and development
- [x] educator — teaching, course creation, lesson plans
- [x] legal-advisor — legal research and document review

## v0.3.0 - Quality and testing

Each item below has a GitHub issue with full scope. Work on these in order.

- [ ] **Test results table per profile**
  - A `## Tested with` section added to each profile file
  - Columns: AI name, model version, date tested, result (pass/fail), notes
  - Populated by contributors who test profiles and submit PRs
  - Tracked in the profile file itself, not a separate document

- [ ] **Automated prompt quality scoring**
  - A script in `.github/scripts/` that sends each profile to an AI API
  - Returns a score based on: response follows rules, no filler, correct format
  - Score stored as a JSON file in `test-results/`
  - Run manually via `workflow_dispatch` — not on every PR

- [ ] **Benchmark: token cost per profile vs no profile**
  - Same prompt sent twice: once with profile, once without
  - Measures: token count, response quality score, time to response
  - Results stored in `benchmarks/` as JSON and rendered as a table in README
  - Run manually via `workflow_dispatch`

## v0.4.0 - Multilingual

Malayalam is the maintainer's native language and will serve as the pilot for the translation process.
Once the format and tooling are established, contributions in other languages are welcome.

- [ ] Malayalam translations of core profiles
- [ ] Translation contributor guide
- [ ] profiles/lang/ folder structure and naming convention

## v1.0.0 - Stable

- [ ] All core profiles tested across 3+ AIs
- [ ] Docs site (GitHub Pages)
- [ ] Full contributor guide with examples
- [ ] 10+ community-submitted profiles

---

Have an idea? Open an issue with the label `feature`.

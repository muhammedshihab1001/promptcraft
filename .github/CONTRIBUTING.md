# Contributing to promptcraft

Thanks for contributing. Read this before opening a PR.

---

## What we accept

- New profiles for use cases not yet covered
- Improvements to existing profiles
- Additions to the free resources list
- Fixes for typos, broken formatting, or outdated information
- Translations of existing profiles (place in `profiles/lang/`)

## What we do not accept

- Profiles that duplicate existing ones
- AI-generated filler or padding in profiles
- Promotional content or affiliate links in free-resources
- Unverified tools in free-resources (verify the free tier exists and include the date you verified it)

---

## Profile standards

Every profile must include this header at the top of the file:

```md
# Name: Profile Name
# Works with: Claude, ChatGPT, Gemini, [others]
# Best for: [use case]
# Extends: [parent profile or "None"]
# Version: [check CHANGELOG.md for the current version number]
```

Profiles must:
- Be testable (paste it into an AI session, run it, it works)
- Follow the formatting rules in `profiles/universal.md`
- Focus on one use case — no padding or filler rules
- Use plain hyphens only — no em dashes (—)
- Use straight quotes only — no smart quotes (" " ' ')

### Extends field rules

- Must be a single value — multi-parent syntax is not supported
- Valid values: a path relative to `profiles/` (e.g. `universal.md`, `developer/backend.md`), or `None`
- The referenced file must exist in the repo — CI will fail if it does not
- Use `None` (not `N/A`, not blank) when the profile has no parent
- Example: `# Extends: universal.md`

---

## Free resources standards

- Every entry must have a verified free tier
- Include the date you verified it in your PR description
- Do not add tools where the free tier requires a credit card without a note saying so
- Remove suggestions are welcome — if a free tier has disappeared, open a fix PR

---

## PR process

1. Fork the repo
2. Create a branch using the correct naming pattern (see below)
3. Make your changes
4. Test the profile with at least one AI before submitting
5. Open a PR using the PR template
6. Wait for review

---

## Branch naming

Use these patterns — the auto-labeler depends on them:

| Change type | Branch pattern | Example |
| --- | --- | --- |
| New profile | `profile/profile-name` | `profile/security` |
| Edit existing profile | `improvement/description` | `improvement/analyst-accuracy` |
| Fix | `fix/description` | `fix/backend-typo` |
| Improvement | `improvement/description` | `improvement/agent-error-schema` |
| Translation | `translation/lang-profilename` | `translation/ml-developer-backend` |

**Important:** Use `improvement/` for edits to existing profiles, not `profile/`.
Using `profile/` on an edit triggers a minor version bump instead of a patch bump.

**Breaking changes** (removing or renaming required header fields) require the `breaking` label to be added manually by a maintainer before merge. If your PR introduces a breaking change, note it clearly in the PR description.

---

| Label | Meaning |
| --- | --- |
| `feature` | New profile or major addition |
| `fix` | Correction to existing content |
| `improvement` | Refinement of existing profile |
| `docs` | README or documentation only |
| `free-resources` | Addition to free resources list |
| `translation` | Translated version of a profile |
| `ci` | Changes to workflows or automation |
| `breaking` | Removes or renames a required field — major version bump — maintainer adds manually |
| `needs-work` | Reviewer requested changes |
| `good first issue` | Good for new contributors |

---

## Stale PRs

PRs with no activity for 14 days are marked stale automatically.
They are closed after 7 more days with no activity.
PRs labeled `needs-work` are exempt from stale closing.
Re-open if you want to continue.

---

## Code of Conduct

Be direct. Be respectful. No personal attacks.
Full details in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

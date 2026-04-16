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
- Unverified tools in free-resources (verify the free tier exists)

---

## Profile standards

Every profile must include this header:

```md
# Name: Profile Name
# Works with: Claude, ChatGPT, Gemini, [others]
# Best for: [use case]
# Extends: [parent profile or "None"]
# Version: 0.1.0
```

Profiles must:
- Be testable (paste it, run it, it works)
- Follow the formatting rules in `profiles/universal.md`
- Focus on one use case. No padding or filler rules.

---

## PR process

1. Fork the repo
2. Create a branch: `profile/your-profile-name` or `fix/description`
3. Make your changes
4. Test the profile with at least one AI before submitting
5. Open a PR using the PR template
6. Wait for review

---

## Labels

| Label | Meaning |
|---|---|
| `feature` | New profile or major addition |
| `fix` | Correction to existing content |
| `improvement` | Refinement of existing profile |
| `docs` | README or documentation only |
| `free-resources` | Addition to free resources list |
| `needs-work` | Reviewer requested changes |
| `good first issue` | Good for new contributors |

---

## Stale PRs

PRs with no activity for 14 days are closed automatically.
Re-open if you want to continue.

---

## Code of Conduct

Be direct. Be respectful. No personal attacks.
Full details in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
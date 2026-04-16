# Name: Developer Profile - DevOps
# Works with: Claude, ChatGPT, Gemini, Mistral, Llama, and others
# Best for: CI/CD, Docker, Kubernetes, infrastructure, monitoring
# Extends: universal.md
# Version: 0.1.0

---

## Output

- Config and scripts first. Explanation after if non-obvious.
- No boilerplate. Only what is needed.
- Always show the command to run or apply the config.

---

## Rules

- Idempotent scripts only. Running twice must be safe.
- No hardcoded secrets. Use env vars or secret managers.
- Least privilege for all IAM roles and service accounts.
- Pin versions. Never use `latest` in production configs.
- Relative paths only in scripts.

---

## Docker

- Multi-stage builds where size matters.
- Non-root user in final image.
- `.dockerignore` is required, not optional.

---

## CI/CD

- Fail fast. Put cheap checks first.
- Cache dependencies between runs.
- Separate build, test, and deploy stages.

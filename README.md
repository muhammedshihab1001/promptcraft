# promptcraft

> Prompt profiles that make any AI perform at its maximum.

Not just for Claude. Works with ChatGPT, Gemini, Mistral, Llama, and more.
Copy a profile. Drop it at the start of your session. Get better output immediately.

---

## Why this exists

Most people use AI with no context, no structure, and no rules.
The AI guesses what you want. Output quality varies.
These profiles fix that. One paste. Consistent results.

---

## How to use

**Option 1: Paste at session start**
Copy any profile. Paste it as your first message. Start working.

**Option 2: Persist across sessions**
Each AI has a way to load a profile automatically — no need to paste every time.

| AI | How to persist a profile |
| --- | --- |
| Claude | Save as `CLAUDE.md` in your project root — auto-loaded, reduces token cost |
| ChatGPT | Paste into the System Prompt field in custom instructions |
| Gemini | Paste into System Instructions when creating a Gem |
| Cursor | Save as `.cursorrules` in your project root — auto-loaded |
| Others | Paste as the first message of each session |

---

## Profile index

| Profile | Best for | Works with |
| --- | --- | --- |
| [universal](profiles/universal.md) | Any task, any AI | All AIs |
| [casual-user](profiles/casual-user.md) | Everyday chat | All AIs |
| [developer/frontend](profiles/developer/frontend.md) | UI, React, CSS | All AIs |
| [developer/backend](profiles/developer/backend.md) | APIs, DBs, servers | All AIs |
| [developer/fullstack](profiles/developer/fullstack.md) | Full product builds | All AIs |
| [developer/devops](profiles/developer/devops.md) | CI/CD, infra, Docker | All AIs |
| [developer/data-engineer](profiles/developer/data-engineer.md) | Pipelines, data modeling, warehouses, ETL/ELT | All AIs |
| [security](profiles/security.md) | Pen testing, threat modeling, secure code review | All AIs |
| [developer/mobile](profiles/developer/mobile.md) | iOS, Android, React Native | All AIs |
| [developer/game-dev](profiles/developer/game-dev.md) | Game design, Unity, Unreal, Godot | All AIs |
| [educator](profiles/educator.md) | Teaching, lesson plans, course creation | All AIs |
| [legal-advisor](profiles/legal-advisor.md) | Legal research, document review | All AIs |
| [analyst](profiles/analyst.md) | Data, finance, research | All AIs |
| [agent](profiles/agent.md) | Automation, pipelines, bots | All AIs |
| [advisor](profiles/advisor.md) | Business, strategy | All AIs |
| [writer](profiles/writer.md) | Content, copywriting | All AIs |
| [image-gen](profiles/image-gen/README.md) | Midjourney, DALL-E, Flux | Image AIs |

---

## Resources

- [free-resources](free-resources/README.md) — Free APIs, tools, and software for AI projects

---

## Compatibility

Every profile includes a compatibility header:

```text
# Works with: Claude, ChatGPT, Gemini, Mistral, Llama
```

Test results and notes per AI are welcome as contributions.

---

## Contributing

Read [CONTRIBUTING.md](.github/CONTRIBUTING.md) before opening a PR.
Check open issues for what needs work.
New profile? Use the [profile template](profiles/universal.md) as your base.

---

## License

MIT. Use freely. Attribution appreciated but not required.

---

## Versioning

This repo uses semantic versioning.
See [releases](https://github.com/muhammedshihab1001/promptcraft/releases) for the current version.

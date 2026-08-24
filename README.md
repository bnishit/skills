# Skills

Agent skills for **writing, thinking, and understanding a topic deeply** — kept in one place so any agent (Claude Code, Codex, Cursor, and the rest) reads the same copy.

They are built to be used together. Name the outer one and the inner ones fire on their own, at the moment they are needed. See [The stack](#the-stack).

## Install

Install everything, for every agent on your machine:

```bash
npx skills add bnishit/skills --global
```

Install one skill:

```bash
npx skills add bnishit/skills --skill second-life-writing --global
```

Try one without installing it:

```bash
npx skills use bnishit/skills@second-life-writing
```

The installer asks which agents to set up, then drops the skill where each one looks for it. Works with any agent that supports the skills install flow. Drop `--global` to install into the current project only.

Later, pull in any changes:

```bash
npx skills update
```

## The skills

| Skill | What it does |
|---|---|
| [going-to-the-library](skills/going-to-the-library) | Maps a whole field before you go deep: who has answered the question best, how they disagree, where the argument is still live. Builds a persistent library you come back to. |
| [strip-it-down](skills/strip-it-down) | Teaches one hard idea from bedrock, one claim per turn, and stops on a question until you answer. Seven counted slots per chapter, so it cannot drift into a wall of text. |
| [apprentice](skills/apprentice) | Takes you from cannot-do to can-do across many sessions, with the state on disk. Every session ends with a rep you owe before the next one. |
| [second-life-writing](skills/second-life-writing) | Writes simple, audience-aware text in `brief` or `operational` mode. Both modes remove waste; operational mode keeps the detail that teams need to act later. |
| [show-me](skills/show-me) | Answers with the smallest visual that makes the point — a tree, a diff, pseudocode, a Mermaid diagram, or one focused HTML page when it earns the tab. |
| [openrouter-integration](skills/openrouter-integration) | OpenRouter model and endpoint discovery, live discounts, dedicated media APIs, key/account spend diagnostics, routing, reasoning, batch controls, and Next.js / Express starters. |

## The stack

Five of these are one thing. Three entry points, depending on what you actually want, and they share the same two finishers.

```
  "what's the landscape      "teach me this one      "I want to be able
        on X?"                  hard thing"             to DO this"
           │                         │                       │
           ▼                         │                       ▼
  going-to-the-library               │                  apprentice
  maps the field, keeps              │                  one rep per session,
  a library you return to            │                  state on disk
           │                         │                       │
           │  a book gets pulled     │                       │
           ▼                         ▼                       │
              strip-it-down                                  │
    one claim per turn · stops on a question ◄───────────────┤
                     │                                       │
        ┌────────────┴────────────┐                          │
        ▼                         ▼                          │
     show-me            second-life-writing ◄────────────────┘
  draws the proof      plain register · the budget is a gate
```

Each skill declares its edges in a **Composes with** table at the top of its `SKILL.md` — what it reaches for, what reaches for it, and the moment the handoff fires. The edges are load-bearing: `strip-it-down` will not draft a chapter without loading `second-life-writing` first, and the library will not teach a book except through `strip-it-down`.

Each still works alone. `strip-it-down` needs no library; `second-life-writing` and `show-me` are general skills reached for by anything whose output a person has to read or look at.

**Convention for adding a skill to the stack:** put a `Composes with` table at the top, and write required handoffs as `**REQUIRED SUB-SKILL:** load X at <moment>` at the point in the flow where they fire — not as a description of what X does. A pointer that summarises the other skill gets read as a substitute for it, and the handoff silently stops happening. Never require a skill that isn't in this repo.

## Credit

Some of these started as someone else's idea and were changed to fit how I work. Each derived skill says so in its own `SKILL.md`, with what was changed and why.

| Skill | Based on | What changed |
|---|---|---|
| [apprentice](skills/apprentice) | Matt Pocock's `teach` | One state file instead of five, the learner's answers recorded verbatim, a rep owed every session, and a counted lesson contract so prose can't drift. |

Skills built by others that pair well but are **not** bundled here, because they aren't mine to ship: `teach` and the wider engineering set (Matt Pocock), and `visual-explainer` (nicobailon, MIT) for the heavy HTML end of `show-me`.

## Using them

Once installed, name the skill in your prompt:

```
$second-life-writing draft the launch email for the new billing flow
```

Choose a mode when the tradeoff matters:

```
$second-life-writing brief rewrite this Slack update
$second-life-writing operational draft the cross-team rollout note
```

`brief` produces the shortest complete message. `operational` keeps the role-specific detail that teams need to act later. The skill chooses a mode when you do not name one.

If mode or audience is unclear and the choice would materially change the result, the skill recommends an option and asks at most two questions. Clear requests proceed without a clarification round.

Most agents also pick a skill up on their own when the task matches its description.

## Manual install

No installer, just clone and symlink:

```bash
git clone https://github.com/bnishit/skills.git ~/dev/skills
ln -s ~/dev/skills/skills/second-life-writing ~/.claude/skills/second-life-writing
```

Point the symlink at whichever skills directory your agent uses (`~/.claude/skills`, `~/.codex/skills`, `~/.cursor/skills`, and so on).

## Layout

```
skills/
  <skill-name>/
    SKILL.md        # the skill itself; frontmatter has name + description
    references/     # longer material the skill loads only when needed
    assets/         # templates and code the skill can copy into a project
```

`SKILL.md` stays short. Anything long lives in `references/` so the agent loads it only when it actually needs it.

## License

MIT. See [LICENSE](LICENSE).

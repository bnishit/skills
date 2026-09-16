# Skills

Agent skills for **writing, product design, and understanding a topic deeply** — kept in one place so any agent (Claude Code, Codex, Cursor, and the rest) reads the same copy.

They are built to be used together. Name the outer one and the inner ones fire on their own, at the moment they are needed. See [the learning stack](#the-learning-stack).

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
| [write-a-book](skills/write-a-book) | Develops personal or reflective books, nonfiction, and fiction—including literary/formal and ensemble/epic modes—from discovery through manuscript lock. |
| [package-a-book](skills/package-a-book) | Turns a locked manuscript into verified EPUB, PDF, and optional reader-site editions without silently changing the prose. |
| [improve-a-skill](skills/improve-a-skill) | Tests whether a reusable agent skill improves real work, then hardens it through blind baselines, observable gates, and bounded iteration. |
| [show-me](skills/show-me) | Answers with the smallest visual that makes the point — a tree, a diff, pseudocode, a Mermaid diagram, or one focused HTML page when it earns the tab. |
| [restock](skills/restock) | What's happened lately on a topic, and — the part that matters — what on your shelf has since been superseded, corrected or retracted. |
| [openrouter-integration](skills/openrouter-integration) | OpenRouter model and endpoint discovery, live discounts, dedicated media APIs, key/account spend diagnostics, routing, reasoning, batch controls, and Next.js / Express starters. |
| [product-hypothesis-pressure-test](skills/product-hypothesis-pressure-test) | Challenges a product mechanic through both users’ choices, counterexamples, and one small test. Keeps personal experience separate from evidence that the idea works. |
| [feature-scoping](skills/feature-scoping) | Grounds a feature idea in what exists, resolves owner decisions, and coordinates a proportionate product/design handoff. |
| [product-reviewer](skills/product-reviewer) | Specifies or reviews behavior from the user’s task, worry, defaults, and next step. |
| [ux-reviewer](skills/ux-reviewer) | Specifies or reviews rendered screens, interaction states, accessibility, and exact copy. |
| [product-editor](skills/product-editor) | Challenges a spec’s premise, cuts unnecessary features, and resolves product/design disagreements. |

## The learning stack

Five of these are one thing. Three entry points, depending on what you actually want, and they share the same two finishers.

```
  "what's the landscape      "teach me this one      "I want to be able
        on X?"                  hard thing"             to DO this"
           │                         │                       │
           ▼                         │                       ▼
  going-to-the-library ◄── restock   │                  apprentice
  maps the field, keeps    what's    │                  one rep per session,
  a library you return to  changed   │                  state on disk
           │               since     │                       │
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

## Book workflow

The book skills separate editorial judgment from production so a layout pass cannot quietly rewrite approved prose.

```text
conversations · notes · research · fictional premise
                         │
                         ▼
                  write-a-book
    discover → architect → prototype → draft → revise → lock
                         │
                 locked manuscript
                         │
                         ▼
                 package-a-book
     art direction → EPUB · PDF · optional reader site → verify
```

`write-a-book` changes its method by mode: Socratic discovery for unresolved personal material, evidence boundaries for nonfiction, and causal, literary/formal, ensemble/epic, or hybrid architectures for fiction. `package-a-book` starts only after manuscript lock, records the source hash, and verifies that the same ordered prose reached each edition. Publication and deployment remain separate, explicit actions.

## Skill improvement workflow

`improve-a-skill` is for a skill that exists but has not yet earned trust. It first checks whether the job is recurring and whether an existing skill already covers it. A duplicate or generic “be clear and accurate” skill should be merged or deleted, not expanded.

```text
skill idea or observed failure
            │
            ▼
    establish job and boundary
            │
            ▼
 representative · boundary · failure cases
            │
            ▼
 no-skill or previous-version baseline
            │
            ▼
 one bounded change → regression + holdout tests
            │
            ▼
 release · keep experimental · merge · delete
```

Each case gets three to six observable gates. Subjective work is repeated rather than declared reliable from one good answer. Deterministic checks, independent model review, and human judgment remain separate. Saved Shelf items and bookmarks are treated as leads—not as proof that the user read, endorsed, or verified them. The skill records changes that were rejected as well as changes that were kept.

## Product and design workflow

Start with `product-hypothesis-pressure-test` when the idea’s behavioral premise is uncertain. Use `feature-scoping` when you are ready to shape a feature.

| Work | Default path |
|---|---|
| Bounded change to an existing screen | Scope → one combined product/UX spec → one editor pass |
| New surface or major redesign | Scope → product and UX drafts → exchange → editor |
| Review something already built | Product review for usefulness; UX review for interaction and craft |

Product and UX reviewers judge the rendered experience without app source or diffs. The coordinator checks factual claims separately. A prototype proposes; it does not prove what the current product does. If a reviewer has already read the source, the pass must not be described as code-blind or independent.

The four skills carry the same evidence distinctions in their own instructions so individual installs retain those safeguards. Each role can be used alone. Install the companions for the full scoping handoff; the scoping skill names any missing pass instead of pretending it ran. Separate agents are optional and require host support and authorization; sequential role passes are not independent reviews. No model, browser tool, industry, or release pipeline is prescribed.

These four are adapted from the author’s heyAnaya workflow. The portable version keeps the distinct roles and lighter existing-screen path, removes private incident details and local tooling, and leaves the original project unchanged.

## Credit

Some of these started as someone else's idea and were changed to fit how I work. Each derived skill says so in its own `SKILL.md`, with what was changed and why.

| Skill | Based on | What changed |
|---|---|---|
| [apprentice](skills/apprentice) | Matt Pocock's `teach` | One state file instead of five, the learner's answers recorded verbatim, a rep owed every session, and a counted lesson contract so prose can't drift. |
| [restock](skills/restock) | Matt Van Horn's [`last30days`](https://github.com/mvanhorn/last30days-skill) (MIT) | Points at an existing library rather than only producing a standalone brief; makes supersession a first-class output ("what on your shelf is now wrong", not just "what's new"); free no-key sources by default so it never fails closed. |

Skills built by others that pair well but are **not** bundled here, because they aren't mine to ship: `teach` and the wider engineering set (Matt Pocock), [`last30days`](https://github.com/mvanhorn/last30days-skill) itself (Matt Van Horn — install it too; 19 sources, transcripts, prediction-market odds and an accumulating brief library, all of which `restock` deliberately does not do), and [`visual-explainer`](https://github.com/nicobailon/visual-explainer) (nicobailon, MIT) for the heavy HTML end of `show-me`.

## Using them

Once installed, name the skill in your prompt:

```
$second-life-writing draft the launch email for the new billing flow
```

For a book project, keep writing and production separate:

```text
$write-a-book develop this conversation and source pack into a personal book
$package-a-book turn this locked manuscript into EPUB, phone PDF, and a private reader site
```

To test whether a reusable skill genuinely helps:

```text
$improve-a-skill compare this skill with the no-skill baseline and harden the failures
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

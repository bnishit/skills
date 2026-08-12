# Skills

Agent skills I use every day, kept in one place so any agent — Claude Code, Codex, Cursor, and the rest — reads the same copy.

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
| [second-life-writing](skills/second-life-writing) | Writes compact, plain-English text for the actual reader. Every line must add meaning, proof, action, or needed context, and the result must still work when reused later. |
| [openrouter-integration](skills/openrouter-integration) | Everything needed to wire an app into OpenRouter's 300+ models: model discovery, multimodal chat, image generation, exact per-call cost lookup, provider fallbacks, tool calling, and Next.js / Express starter templates. |

## Using them

Once installed, name the skill in your prompt:

```
$second-life-writing draft the launch email for the new billing flow
```

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

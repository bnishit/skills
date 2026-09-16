# Write-a-book fiction-modes evaluation plan

## Skill and decision

- Candidate branch: `codex/fiction-modes`
- Baseline: snapshot of `main` at `e034021f0dc3f901d1e0648982d4d278b0c1dbbb`
- Recurring job: carry a book from discovery through manuscript lock without forcing all fiction into one plot architecture.
- Should activate for book-length development, architecture, drafting, continuity, revision, and lock.
- Should not activate for page layout, edition packaging, publication, or a short standalone writing request with no book workflow.
- Closest overlap: `package-a-book`, which begins only after manuscript lock; the boundary remains unchanged.
- Release decision: branch-ready after a single-trial smoke comparison and structural validation; not reliability-cleared for publication.

## Research that changed the design

| Evidence | Decision changed | Falsified by |
|---|---|---|
| Ursula K. Le Guin's [Carrier Bag Theory](https://www.ursulakleguin.com/the-carrier-bag-theory-of-fiction), [conflict discussion](https://www.ursulakleguin.com/bvc-navigating-the-ocean-of-story-session-2-round-1), and [What Makes a Story](https://www.ursulakleguin.com/what-makes-a-story) reject one heroic, conflict-only shape and treat language and rhythm as story-bearing. | The fiction router now offers causal, literary/formal, ensemble/epic, and hybrid architectures; scene movement can be emotional, imagistic, interpretive, or rhythmic. | Case 10 still receives a conventional reveal-driven plot or treats atmosphere as automatically inert. |
| Le Guin's [Steering the Craft](https://www.ursulakleguin.com/steering-the-craft) makes sound, sentence construction, and point of view explicit craft domains. | Literary state now tracks a voice and rhythm score rather than leaving prose texture to the last polish pass. | Cases 10 or 12 omit durable voice/rhythm decisions. |
| Elena Ferrante's [Art of Fiction interview](https://www.theparisreview.org/interviews/6370/the-art-of-fiction-no-228) describes preserving the truth of gesture, feeling, and flow without domesticating dream material. Toni Morrison's [Nobel lecture](https://www.nobelprize.org/prizes/literature/1993/morrison/lecture/) treats chosen silence and resistance to a final summing-up as meaning-bearing. | Dream logic gets felt operations and bounded readings; open endings must complete non-factual movement without decoding every mystery. | Cases 10 or 12 either randomize the uncanny or explain it mechanically. |
| Brandon Sanderson's [2025 plot lecture](https://www.brandonsanderson.com/blogs/blog/brandon-sandersons-2025-guide-to-plot-lecture-2) and Writing Excuses on [reader progress](https://writingexcuses.com/writing-excuses-10-31-how-do-i-control-the-readers-sense-of-progress/) make promises and payoff observable. | A typed closure ledger now distinguishes answer, transformation, deliberate openness, and series deferral. | Holdout case 14 treats every thread alike or permits cost-free deferral. |
| Writing Excuses on [ensemble characterization](https://wetranscripts.dreamwidth.org/197607.html), James S. A. Corey's [craft interview](https://www.lightspeedmagazine.com/nonfiction/interview-james-s-corey/), Robin Hobb on [logical geography](https://www.scifinow.co.uk/interviews/interview-author-robin-hobb-a-k-a-megan-lindholm/), and Marlon James on [distance and travel](https://time.com/6148335/moon-witch-spider-king-marlon-james-interview/) show that viewpoint, information release, political background, and geography are coupled constraints. | Ensemble state now couples POV, faction, event, travel, political-causality, reveal, and convergence ledgers. | Case 11 permits plot-speed travel, author-knowledge leaks, or uncaused convergence. |
| The Dart Center's [trauma and journalism guide](https://dartcenter.org/sites/default/files/DCE_JournoTraumaHandbook.pdf) centers care, respect, accuracy, and control; Don Winslow's [firsthand reflection on fictional violence](https://time.com/6170479/don-winslow-writing-violence-fiction/) emphasizes aftermath over titillation. These are used as ethical prompts, not universal fiction law. | The literary workflow protects ordinary agency, tests the necessity of intense detail, and tracks aftermath and source/permission boundaries. | Case 10 makes suffering the character's entire identity or uses detail mainly for shock. |
| Primary or firsthand interviews with [Haruki Murakami](https://www.theparisreview.org/interviews/2/the-art-of-fiction-no-182-haruki-murakami), [Hanya Yanagihara](https://themillions.com/2015/08/i-wouldntve-had-a-biography-at-all-the-millions-interviews-hanya-yanagihara.html), [Hideo Kojima](https://www.bafta.org/media-centre/press-releases/2012-annual-games-lecture-delivered-by-hideo-kojima/), [J.K. Rowling](https://www.jkrowling.com/opinions/the-sunday-times-bestseller-qa/), and [George R.R. Martin](https://time.com/4791258/game-of-thrones-george-r-r-martin-interview/) span dream association, emotional intensity, fragmentary discovery, long-series planning, and factional scale. | These names remain private research coordinates. The portable workflow exposes only general craft dimensions and an explicit no-imitation boundary. | Cases 9 or 13 echoes a signature voice, world, character, or scene pattern. |
| Current [Agent Skills guidance](https://agentskills.io/skill-creation/evaluating-skills) requires clean-context comparisons and observable assertions; the [specification](https://agentskills.io/specification) and Anthropic's [progressive-disclosure guidance](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) favor focused conditional references. | `SKILL.md` remains a router; mode-specific craft and state live in conditional references and assets. The eval uses a frozen main snapshot. | Candidate bloats the root skill or runners can see the expected verdict. |

Saved Shelf material was not queried because no Shelf or bookmarks connector was available in the evaluation environment. No saved item was treated as read, endorsed, or verified.

## Invariants

| Invariant | Evidence |
|---|---|
| Preserve original voice and refuse close imitation of living creators. | Cases 9 and 13. |
| Do not invent canon, facts, permissions, or explanations. | Existing cases 1-9 plus cases 10-12. |
| Keep manuscript editing separate from packaging and publication. | Existing case 5. |
| Use durable state proportionate to the mode, not every ledger on every project. | Cases 10-12 and token/cost review. |
| Open endings still treat material promises and consequences intentionally. | Cases 10, 12, and holdout 14. |

## New cases

| ID | Type | Main hard gates | Severity |
|---|---|---|---|
| 10 | literary failure | correct architecture; felt dream logic; literary state; non-exploitative pressure; typed closure; earned open ending | high |
| 11 | epic representative | volume/series split; purposeful POVs; coupled ledgers; political causality; caused convergence; closure treatment | high |
| 12 | hybrid representative | lead mode; physical versus emotional time; distinct voices; document/reveal state; caused vote; open dream question | high |
| 13 | imitation boundary | refusal; trait translation; original voice/world; proportionate setup; no signature borrowing; prototype framing | critical |
| 14 | unseen holdout | typed promises; volume obligations; consequential deferral; motif development; debt disposition; propagation | high |

## Trial protocol

- Run identical prompts in separate ephemeral contexts against the frozen main snapshot and candidate path.
- Do not provide expectations or the desired winner to runners.
- Grade gates with cited output evidence, then compare paired outputs blind to version labels.
- Planned scope for this branch is one paired trial per new case plus one unseen holdout. This is a smoke test, not a reliability result; three trials per high-variance case remain the release-grade plan.
- Re-run existing cases 3, 4, 5, and 9 before publication to catch causal-fiction, handoff, and imitation regressions.

## Trial log

One anonymous A/B grader scored six gates per case. The A/B assignment changed by case, so the results below name the actual version. Output word count is a rough cost signal; model tokens, latency, and repeated-run variance were not retained consistently enough to compare.

| Case | Main | Candidate | Blind preference | Finding |
|---|---:|---:|---|---|
| 10 literary | 6/6, 1,131 words | 6/6, 938 words | candidate | Same control with a tighter architecture and ending. |
| 11 ensemble | 6/6, 2,441 words | 6/6, 2,932 words | main | Candidate passed every gate but spent about 20% more words on canon and control state. |
| 12 hybrid | 5/6, 4,149 words | 6/6, 2,086 words | candidate | Candidate named the hybrid and assigned causal versus literary jobs; main left that control implicit. |
| 13 imitation, initial | 5/6, 872 words | 5/6, 956 words | main | Both refused imitation and stayed original, but neither stated the translated trait brief explicitly. |
| 14 unseen holdout | 6/6, 690 words | 6/6, 684 words | main | Candidate typed every promise clearly; main made the ancient debt's present-volume consequence more decisive. |

Initial hard-gate total was 28/30 for main and 29/30 for candidate. Pairwise preference favored candidate in two cases and main in three; this is not a claim of broad superiority.

The imitation finding caused one focused edit: the root and fiction reference now require a one-sentence translated craft brief before the prototype. A clean candidate rerun made the five requested dimensions explicit and satisfied the previously unverified gate. That rerun was not blind-paired and was longer at 1,489 words, so it is remediation evidence, not a revised full-suite score.

A candidate-only causal-fiction regression produced a named dramatic/causal architecture, a causal chapter map, and a warm representative opening. Five of six existing gates were observable; durable world-rule and unresolved-canon state remained implicit rather than recorded. No paired main run was made, so regression status is incomplete.

Across the five initial paired outputs, candidate responses totaled 7,596 words and main responses 9,283. The candidate was shorter overall because of the hybrid case, but the ensemble case shows a real over-architecture risk. No latency or token-cost conclusion is supported.

## Release statement

Custom validation passed frontmatter, JSON parsing, unique eval IDs, local Markdown links, and all fourteen eval records. `git diff --check` also passed.

The branch is suitable for review and commit. Evidence supports the new architecture router, hybrid control, mode-specific state, and shared closure ledger. It does not yet support statistical reliability: every paired case ran once, the targeted repair ran once, and existing cases 3, 5, and a paired case 4 remain unrun. Before publication, run three trials for high-variance cases and complete the existing regression set.

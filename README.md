# Awesome Self-Evolving Agents

> A living, evidence-oriented index of agents that improve their persistent behavior, tools, harness, memory, skills, policies, or environments.

[![Track arXiv](https://github.com/LKRCharon/awesome-self-evolving-agents/actions/workflows/track-arxiv.yml/badge.svg)](https://github.com/LKRCharon/awesome-self-evolving-agents/actions/workflows/track-arxiv.yml)

This project is intended to complement static awesome lists. It does not treat the words *self-evolving* or *continual* as sufficient evidence. Each reviewed entry records:

- the dominant mutable object: what is actually updated and reused;
- the evolution loop: how traces or feedback become a candidate update;
- the evidence source and validation gate;
- whether the result is a paper, code release, benchmark, or deployed system;
- the last date on which these claims were checked.

The index currently has two layers:

- `data/papers.json`: manually reviewed entries that meet the inclusion criteria;
- `data/discovered.json`: arXiv candidates found by the scheduled tracker and awaiting review.

## Inclusion rule

Include a work when the paper or project demonstrates a persistent object that changes based on experience or evaluation and is reused in later tasks, episodes, or deployments. The object may be a prompt, skill, memory, tool, workflow, harness, source code, model policy, rubric, or environment.

Do not promote a work merely because it has reflection, chain-of-thought, test-time search, a fixed multi-agent topology, an offline dataset generator, or a cache. Those may be useful components, but they are not by themselves self-evolution.

## Taxonomy

The primary taxonomy follows the dominant mutable object rather than the marketing name of the method.

| Axis | Mutable object | Representative entries |
| --- | --- | --- |
| Harness and source | tools, middleware, runtime, source code, harness routing | [AHE](https://arxiv.org/abs/2604.25850), [MOSS](https://arxiv.org/abs/2605.22794), [Adaptive Auto-Harness](https://arxiv.org/abs/2606.01770) |
| Skills and memory | skills, playbooks, memory, procedures | [SkillOpt](https://arxiv.org/abs/2605.23904), [EvoHunt](https://arxiv.org/abs/2606.16420) |
| Tools | tool policies, tool libraries, generated tools | [Tool-R0](https://arxiv.org/abs/2602.21320), [MetaForge](https://arxiv.org/abs/2606.01801) |
| Prompts and policies | system prompts, task prompts, rubrics, reward policies | [SePO](https://arxiv.org/abs/2606.04465), [ANNEAL](https://arxiv.org/abs/2605.16309) |
| Roles and topology | roles, agent graphs, communication topology | [TPGO](https://arxiv.org/abs/2604.20714) |
| Evaluation and control plane | evaluation environments, ledgers, routing and governance | [SEAGym](https://arxiv.org/abs/2606.17546) |

## Reviewed papers

The structured catalog is the source of truth. Start with [`data/papers.json`](data/papers.json), then filter by `mutable_object`, `evolution_scope`, `validation`, or `venue_status`.

<!-- PAPERS:START -->
## Reviewed Papers

Each entry exposes the claims that matter for comparing evolution systems. `arXiv` means the venue was not independently confirmed as a peer-reviewed publication.

- **[Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)** — `arXiv 2026`<br>
  Mutable object: `harness, tools, middleware, memory, skills` · Scope: `cross-session`<br>
  Evolution loop: trajectory evidence -> component-level edit -> next-round prediction check<br>
  Evidence: Terminal-Bench 2 pass@1: 69.7% -> 77.0%; transfer to other model families and SWE-bench-Verified<br>
  Validation: next-round task outcomes verify a self-declared change prediction; component-level rollback<br>
  Code: -

- **[MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794)** — `arXiv 2026`<br>
  Mutable object: `source code, runtime, container image` · Scope: `production`<br>
  Evolution loop: production failure batch -> source rewrite -> replay in trial workers -> image swap<br>
  Evidence: OpenClaw four-task mean grader score: 0.25 -> 0.61 in one cycle<br>
  Validation: candidate-image replay, user-consent gate, health-probe rollback<br>
  Code: -

- **[Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770)** — `arXiv 2026`<br>
  Mutable object: `harness tree, routing policy` · Scope: `production`<br>
  Evolution loop: open-ended task stream -> stateful harness construction -> task-wise harness routing<br>
  Evidence: outperforms five auto-harness baselines across prediction-market, security, and event-forecasting streams<br>
  Validation: stream evaluation, ablations for construction/routing/human steering<br>
  Code: [repo](https://github.com/A-EVO-Lab/a-evolve/tree/release/adaptive-auto-harness)

- **[HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249)** — `arXiv 2026`<br>
  Mutable object: `typed harness primitives, control flow` · Scope: `cross-session`<br>
  Evolution loop: trajectory -> typed primitive proposal -> multi-agent evolution -> harness evaluation<br>
  Evidence: five-benchmark gains reported in the paper, including an average improvement and task-level peaks<br>
  Validation: benchmark comparison and ablations; exact artifact status should be checked separately<br>
  Code: -

- **[Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)** — `arXiv 2026`<br>
  Mutable object: `agent harness` · Scope: `cross-session`<br>
  Evolution loop: weakness mining -> harness proposal -> proposal validation<br>
  Evidence: improvements reported across the paper's coding-agent task suites<br>
  Validation: candidate proposal validation with rejection of regressions<br>
  Code: -

- **[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904)** — `arXiv 2026`<br>
  Mutable object: `skills, skill library` · Scope: `cross-session`<br>
  Evolution loop: experience -> bounded skill edit -> held-out evaluation -> adoption or rejection<br>
  Evidence: skill optimization results reported across the paper's agent benchmarks<br>
  Validation: held-out gate and constrained edits<br>
  Code: [repo](https://github.com/microsoft/SkillOpt)

- **[Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420)** — `arXiv 2026`<br>
  Mutable object: `playbooks, skills` · Scope: `cross-session`<br>
  Evolution loop: security-audit trajectories -> playbook patch -> transfer evaluation<br>
  Evidence: self-evolved security playbooks are evaluated for transfer across models and harnesses<br>
  Validation: held-out and cross-model transfer evaluation<br>
  Code: -

- **[SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.17546)** — `arXiv 2026`<br>
  Mutable object: `evaluation environment, evolution protocol` · Scope: `cross-session`<br>
  Evolution loop: agent trajectories -> evolution update -> frozen validation, held-out transfer, and replay<br>
  Evidence: the paper proposes evaluation across train, frozen validation, held-out ID/OOD, replay, and cost dimensions<br>
  Validation: frozen validation, held-out transfer, replay diagnostics, and cost tracking<br>
  Code: -

- **[ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning](https://arxiv.org/abs/2605.16309)** — `arXiv 2026`<br>
  Mutable object: `process knowledge, operator schemas, symbolic patches` · Scope: `cross-session`<br>
  Evolution loop: failure attribution -> typed symbolic patch -> canary test -> commit or rollback<br>
  Evidence: recurring-failure reductions reported across the paper's task environments<br>
  Validation: typed patch constraints, canary tests, and governed commit/rollback<br>
  Code: -

- **[Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization](https://arxiv.org/abs/2604.20714)** — `arXiv 2026`<br>
  Mutable object: `agents, tools, workflows, optimizer strategy` · Scope: `cross-session`<br>
  Evolution loop: execution traces -> textual gradients -> graph edits -> optimizer learns from past edits<br>
  Evidence: improvements reported on GAIA and MCP-Universe<br>
  Validation: task performance comparison across optimized multi-agent systems<br>
  Code: -

- **[Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320)** — `arXiv 2026`<br>
  Mutable object: `model policy, task generator` · Scope: `cross-session`<br>
  Evolution loop: generator proposes frontier tasks -> solver uses real tools -> self-play RL updates both roles<br>
  Evidence: 92.5% relative improvement over the base model is reported under the paper's setting<br>
  Validation: tool-use benchmark evaluation and curriculum/scaling analysis<br>
  Code: -

- **[SePO: Self-Evolving Prompt Agent for System Prompt Optimization](https://arxiv.org/abs/2606.04465)** — `arXiv 2026`<br>
  Mutable object: `system prompt, prompt optimizer` · Scope: `cross-session`<br>
  Evolution loop: task outcomes -> prompt edits -> prompt agent also updates its optimization strategy<br>
  Evidence: average gains across five benchmarks are reported in the paper<br>
  Validation: benchmark comparison against prompt optimization baselines<br>
  Code: -

- **[RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703)** — `arXiv 2026`<br>
  Mutable object: `skills, tools, scoring rubrics` · Scope: `cross-session`<br>
  Evolution loop: preference demonstrations -> reasoning-chain analysis -> skill and tool updates -> later evaluation<br>
  Evidence: 47.4% average accuracy on EditReward-Bench and GenAI-Bench using 100 preference demonstrations<br>
  Validation: held-out validation gate, checkpointing, and rollback of regressions beyond the exploration tolerance<br>
  Code: [repo](https://github.com/TIGER-AI-Lab/RewardHarness)


Catalog size: **13 reviewed papers**. Full records and stable fields live in [`data/papers.json`](data/papers.json).
<!-- PAPERS:END -->

The most useful questions for comparing systems are:

1. What survives after the current session ends?
2. What exact signal authorizes an update?
3. How is the candidate tested against old and new tasks?
4. Can the update be attributed, rejected, or rolled back?
5. Is the evidence benchmark-only, held-out, cross-model, or production-derived?

## Automatic tracking

The weekly GitHub Actions workflow queries arXiv using the search terms in [`data/searches.json`](data/searches.json). New records are written to `data/discovered.json` with `review_status: unreviewed`. Automation is for discovery, not for scientific judgment; a human review is required before moving an entry into `papers.json`.

## Related resources

- [XMUDeepLIT/Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents): broad static survey of papers, benchmarks, and projects.
- [RUCAIBox/awesome-agent-harness](https://github.com/RUCAIBox/awesome-agent-harness): harness-focused paper and project collection.
- [Microsoft SkillOpt](https://github.com/microsoft/SkillOpt): code and experiments for skill optimization.
- [SEAGym](https://arxiv.org/abs/2606.17546): evaluation environment for self-evolving agents.

## Maintainer workflow

```text
arXiv discovery -> review queue -> evidence review -> papers.json -> README table
```

The generated table is intentionally limited to reviewed entries. The discovery queue may contain false positives and is not presented as a bibliography until a reviewer checks it.

## Contributing

Please add a source URL and keep claims narrower than the evidence. For a paper, explain the mutable object, update signal, validation method, and whether code is actually available. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

The catalog and scripts are released under the MIT License. Paper titles, abstracts, and linked artifacts remain under their original licenses.

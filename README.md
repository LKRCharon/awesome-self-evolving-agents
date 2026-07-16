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

## Contributing

Please add a source URL and keep claims narrower than the evidence. For a paper, explain the mutable object, update signal, validation method, and whether code is actually available. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

The catalog and scripts are released under the MIT License. Paper titles, abstracts, and linked artifacts remain under their original licenses.

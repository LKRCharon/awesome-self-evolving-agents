# Contributing

## Add a reviewed paper

Add one object to `data/papers.json`. Keep these fields explicit:

- `id`: arXiv identifier or another stable identifier;
- `mutable_object`: the persistent object that changes;
- `evolution_scope`: session, cross-session, or production;
- `loop`: a short trace-to-update description;
- `evidence`: what was measured;
- `validation`: how candidates were accepted or rejected;
- `venue_status`: use `arXiv`, `conference`, `journal`, or `unknown` and include the venue only when verified;
- `code`: a URL, or `null` when no public code was confirmed;
- `last_verified`: ISO date.

After changing reviewed records, run `python scripts/render_readme.py` so the
README table stays synchronized.

Do not infer code availability, acceptance, or deployment status from an arXiv page. Link the repository, proceedings page, or artifact directly when available.

## Review discovered candidates

The scheduled tracker writes candidates to `data/discovered.json`. Reviewers can promote a candidate by checking the paper and adding a narrower record to `data/papers.json`. The discovery file is intentionally not treated as a reviewed bibliography.

## Quality bar

Reject or defer entries that only perform reflection within one task, use a fixed workflow, retrieve a static memory, generate an offline dataset without updating the agent, or call themselves self-evolving without showing a persistent update and later reuse.

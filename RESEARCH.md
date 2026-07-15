# Evidence, Limits, and Freshness

Last audited: **2026-07-15**

This curriculum teaches a workflow, not a guarantee that AI makes every developer faster or every project better. Agent capability, product features, prices, and security guidance change quickly. Claims about a named product should be checked against its official page at the time of use.

## What the Evidence Supports

**Clear goals, relevant context, and observable acceptance criteria improve inspectability.** They reduce the number of unstated choices and give both humans and tools something concrete to test. This is a workflow principle, not evidence that one perfect prompt guarantees a correct first attempt.

**Longer tasks are generally less reliable, but capability is jagged.** METR's [time-horizon work](https://metr.org/time-horizons/) defines a 50% task horizon using the time a human expert would need for a task—not how long the agent runs. The evaluations focus largely on software, machine learning, and cyber tasks; they should not be generalized to every domain. Use decomposition to create testable vertical slices, then keep end-to-end checks.

**Merge-ready quality requires more than core functionality.** In a 2025 evaluation, METR reported cases where agents implemented central behavior but failed tests, formatting, linting, or other repository expectations ([research update](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)). That supports inspecting diffs and running the repository's complete checks before accepting “done.”

**AI can amplify the surrounding system.** DORA's [2025 report](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) describes AI as an amplifier: strong feedback loops and platforms can benefit, while weak controls can magnify instability. This supports pairing agents with tests, version control, review, and a reliable delivery process.

**Structured reflection has educational evidence.** A [meta-analysis of 25 reflective interventions](https://doi.org/10.1016/j.tsc.2023.101373) found a positive average effect on student learning. That supports the curriculum's dated learning log, especially when entries connect goals, attempts, evidence, learning, and next steps. It does not prove that unstructured note-taking helps every learner.

**Completing a task with AI is not the same as learning the underlying skill.** In a 2026 randomized study of 52 mostly junior software engineers learning an unfamiliar Python library, the AI-assisted group scored 17% lower on a subsequent mastery quiz; the small task-time improvement was not statistically significant ([paper and study details](https://www.anthropic.com/research/AI-assistance-coding-skills)). The study used an embedded assistant rather than a fully agentic coding product and came from an AI vendor, so it does not establish the effect for every learner or tool. A separate 2026 [AAAI pilot study](https://doi.org/10.1609/aaai.v40i48.42121) provides early evidence that forcing learners to reflect and proceed incrementally can support incidental learning. Together, these findings support prediction, explanation, manual edits, retrieval practice, and reflection alongside agent use—not passive acceptance of complete solutions.

**Domain and task expertise still matter in agentic workflows.** Anthropic's June 2026 analysis of roughly 400,000 Claude Code sessions found an association between its transcript-derived expertise rating and its classifier-derived success measures ([report](https://www.anthropic.com/research/claude-code-expertise)). This is large-scale vendor telemetry, not a randomized comparison: selection, task choice, product-specific behavior, and automated labels limit causal claims. It supports teaching learners to deepen domain knowledge and verification skill, not the stronger claim that coding knowledge no longer matters.

**Agent-assisted code needs independent security verification.** OWASP's current [Secure Coding with AI Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html) treats generated code and agent actions as untrusted until reviewed and tested. Peer-reviewed work has also found security weaknesses in generated code and adversarial code-completion settings ([ACL 2025 benchmark](https://aclanthology.org/2025.acl-long.849/), [ICML 2025 study](https://proceedings.mlr.press/v267/jenko25a.html)). These results justify a verification process, not the blanket claim that all AI code is insecure.

## Productivity Evidence Is Mixed

- A GitHub-sponsored controlled study of 95 professional developers completing one JavaScript HTTP-server task reported that the Copilot group completed it 55% faster ([GitHub report](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)). It was a bounded task and a vendor study.
- Three randomized field experiments at Microsoft, Accenture, and one Fortune 100 company covered 4,867 developers. The noisy individual experiments produced a pooled estimate of 26.08% more completed tasks for developers given access to a code-completion assistant ([Microsoft Research paper](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/)). Tool adoption varied, the outcome was completed tasks rather than defect-free value, and code completion is not the same intervention as an autonomous coding agent.
- METR's randomized early-2025 study of 16 experienced open-source maintainers across 246 tasks found they took 19% longer with the tested tools, despite expecting a speedup ([study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). It measured experienced maintainers in repositories they knew, using early-2025 tools.
- METR's February 2026 update found that task selection and participant recruitment made later estimates difficult to interpret; some subsets suggested speedups, but uncertainty was large ([update](https://metr.org/blog/2026-02-24-uplift-update/)).
- A May 2026 METR survey reports perceived value from 349 technical workers, but the authors explicitly discuss selection and self-report limitations ([survey](https://metr.org/blog/2026-05-11-ai-usage-survey/)).
- A 2026 MSR difference-in-differences study associated Cursor adoption in open-source repositories with transient velocity gains and persistent increases in static-analysis warnings, duplication, and complexity ([paper and replication-package link](https://arxiv.org/abs/2511.04427)). Those metrics are imperfect proxies for quality, adoption was not randomized, and the observed repositories and mid-2024-to-mid-2025 tools may not generalize. It is a reason to measure maintainability after adoption, not proof that agents necessarily create technical debt.

The practical conclusion is not “agents are fast” or “agents are slow.” Measure cycle time, review time, defect escape, rework, and task selection in your own environment. Compare completed, accepted work—not generated lines or subjective busyness.

## Claims This Curriculum Deliberately Avoids

- Agents have no memory. Memory, history, retrieval, and project instructions differ by product and may be partial.
- Small tasks always succeed. Smaller tasks are often easier to verify, but excessive fragmentation harms integration and context.
- A compiler proves a program correct. Rust rules out useful categories in safe code; intent, logic, `unsafe`, dependencies, and operations still need verification.
- A fresh or hostile AI reviewer is independent proof. It can share blind spots, miss defects, or hallucinate findings.
- More autonomy always improves productivity. Tool permissions and parallel work increase both leverage and blast radius.
- One model, IDE, MCP server, language, or prompt format is universally best.

## How to Keep This Current

When a chapter names a version, product, registry, authentication flow, price, or security practice:

1. Open the linked official documentation.
2. Check its publication or update date and the version you are actually using.
3. Prefer primary research for capability claims and record sample, task, comparison, and limitations.
4. Reproduce operational claims in a disposable environment.
5. Update the chapter, this audit date, and `CHANGELOG.md` together.

For every project, keep the same standard locally: write the claim, name the evidence that would falsify it, run the check, and preserve the result in the issue tracker or learning log.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← README](README.md) | **Evidence and Freshness** | [Foreword →](FOREWORD.md) |

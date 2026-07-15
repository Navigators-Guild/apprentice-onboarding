# How We Build

## The Discipline Behind the Tools

You know how to talk to agents. You know how to break problems down, provide context, and verify output. You've built something. Now it's time to talk about *how the guild actually builds software*, because there's a method to it, and the method is what separates work that holds up from work that falls apart the moment someone looks at it sideways.

This curriculum calls its workflow **Verification-Driven Development (VDD)** and **Iterative Adversarial Refinement (IAR)**. These are guild terms, not established industry standards. The idea is to define evidence before building, implement in reviewable increments, test the result, obtain independent critique, and fix confirmed gaps until the acceptance criteria and risk threshold are met.

## Why "It Works" Isn't Good Enough

When you build something with an agent and it runs without errors, it's tempting to call it done. It works. Ship it.

The problem is that "it works" and "it works correctly" are very different things. Code can run without crashing and still be full of problems. Maybe it handles the happy path fine but breaks on weird input. Maybe it does the right thing most of the time but has a subtle logic error that only shows up on the last day of the month. Maybe it works perfectly today but is structured in a way that makes it impossible to change tomorrow.

A first working version is weakly evidenced: it may pass the "does it run?" check without having been stressed against edge cases or operational risks. VDD treats it as a candidate and builds confidence through proportionate, observable checks.

## The Three Roles

VDD works by putting three different perspectives in a loop:

**The Builder** is the coding agent used for implementation. It can plan, edit code, write tests, and run tools within the permissions you grant. Its output quality varies by task, context, model, and feedback. Treat completion claims as hypotheses to check against the repository and acceptance criteria.

**The Human (You)** is the director. You set the goals, define what "correct" means, do the manual verification ("does this actually do what I asked?"), and make judgment calls. You're the one who knows the domain, the audience, and the purpose. The Builder doesn't know any of that unless you tell it. Your job is also to mediate between the Builder and the Adversary, deciding which critiques are real problems and which are noise.

**The Reviewer** is the critic. This may be a human, a separate agent context, a specialized tool, or several of these. Its job is to test the work against requirements and named risk areas, cite evidence, and distinguish confirmed defects from questions. A harsh personality is optional; specificity and independence matter more than hostility.

The key insight is separation of responsibilities. The builder produces a candidate, the reviewer challenges it, and the accountable human decides what evidence is sufficient and which actions are authorized.

## The Loop

Here's how it works in practice:

### Step 1: Break It Down

Before any code gets written, the work gets decomposed. You already learned this in Phase 1, but VDD takes it further. Every project gets broken into a hierarchy:

- **Epics** are the big goals. "Build user authentication" is an epic.
- **Issues** are the functional pieces within an epic. "Create login endpoint," "add password hashing," "build session management" are issues.
- **Sub-issues** are reviewable units. Each one has an observable outcome and acceptance criteria, such as "store passwords using the current configuration recommended by our selected maintained password-hashing library, with tests for verification and failure."

Think of it like a string of beads. Each bead is a sub-issue and the string is the epic. Account for required work, while allowing explicit research tasks and documented unknowns instead of pretending every detail is known upfront.

This creates **traceability**. Material changes should connect to a sub-issue, issue, and larger goal. That chain helps investigation and review, but it cannot prove that requirements were complete or identify a defect's cause by itself.

### Step 2: Build and Verify

The Builder implements the sub-issues one at a time. For each one:

1. **Write the code** that implements the feature or fix.
2. **Write tests** that exercise the required behavior. Go beyond "it doesn't crash": does the expected result occur with valid input? Does the specified error occur with invalid input? Which edge cases matter?
3. **You verify manually.** Does this match what you asked for? Does it feel right? Does it do what the design doc says it should do? This is the human-in-the-loop step, and it catches the things automated tests can't: intent mismatches, UX problems, "technically correct but not what I meant" situations.

Only after you're satisfied that a piece works does it move to the next step.

### Step 3: The Roast

This is where it gets interesting. You take your verified, tested code and hand it to the Adversary. The Adversary's job is to find everything wrong with it.

A few things make the roast effective:

**The reviewer gets a checklist and evidence standard.** Placeholder comments, incomplete error handling, security boundaries, performance requirements, and missing tests are reviewed when relevant. Every finding should cite the requirement or code, explain impact, and suggest a way to reproduce it.

**Use an independent view when practical.** A new context or reviewer can reduce shared assumptions, but it also lacks history. Supply the design, acceptance criteria, threat model, supported environment, diff, and test results. Independence without relevant context produces noise.

**It's looking for patterns, not just bugs.** The Adversary catches things like: "You wrote the same error handling logic in six places instead of extracting it." "This function does three unrelated things." "Your test only covers the happy path." "This will break if someone passes null." These are the problems that working code hides from casual inspection.

### Step 4: Fix and Repeat

The Builder takes the Adversary's critique and addresses it:

1. Fix the real problems.
2. Refactor the weak spots.
3. Write new tests for the edge cases the Adversary found.

Then it goes back to the Adversary. Fresh context, fresh roast. The cycle repeats.

## Testing Against Hard Truths

As the loop tightens and the obvious problems get fixed, something interesting happens: the remaining issues get subtler. The Adversary starts finding edge cases that are hard to test with normal unit tests. "What if this number overflows?" "What if two users hit this endpoint at the exact same millisecond?" "What if the input is technically valid but astronomically large?"

This is where VDD uses an **evidence ladder**. Different methods answer different questions; none turns the whole application into a proof.

For an apprentice, you don't need to implement these yet. But you should understand the concept:

- **Standard testing** says "I tried 50 inputs and they all worked." That's useful, but it doesn't tell you about input #51.
- **Formal verification** can prove a stated property for the modeled code and assumptions, such as absence of overflow in a bounded function. It does not prove unspecified requirements or unmodeled dependencies.

In practice, combine compiler checks, tests, property or mutation testing, static analysis, dependency advisory scans, and formal methods where the risk justifies them. Advisory scanners report known records; they are not proofs. Record what each check covers and what remains unverified.

You'll encounter this more as you advance through the guild. For now, the takeaway is: the goal is not merely "it worked when I tried it." State what each check supports and which relevant failure modes remain untested or ruled out only under assumptions.

## Knowing When You're Done

One of the hardest things in any creative process is knowing when to stop. VDD has an elegant answer to this.

Remember that the reviewer is prompted to find problems. An AI reviewer may produce critique even when evidence is weak, while a human reviewer may overlook defects or stop early.

Reviewers—human or AI—can miss real problems and can invent false ones at any quality level. Reviewer exhaustion or hallucination is not an exit signal.

Stop a refinement cycle when the agreed acceptance criteria pass, required checks are green, confirmed high-severity findings are resolved, residual risks and known limitations are documented, and an accountable person accepts the result for its intended use. Reopen the cycle when requirements, dependencies, or evidence change.

## A Roast In Action

Let's walk through what a real adversarial review cycle looks like. Say you've built a function that saves an issue to a JSON file.

**Your code (first draft):**

```rust
fn save_issue(issue: &Issue) -> Result<()> {
    let data = serde_json::to_string(issue)?;
    std::fs::write("issues.json", data)?;
    Ok(())
}
```

It works. It compiles. It saves the issue. You ship it to the Adversary.

**Round 1 - The Adversary says:**

> "This overwrites the entire file with a single issue every time it's called. If you have ten issues and save the eleventh, the first ten are gone. Also, the file path is hardcoded. Also, `to_string` produces compact JSON with no formatting, so the file is unreadable if a human opens it. Also, there's no error context. If the write fails, the user gets 'Permission denied' with no indication of which file or why."

All legitimate. You fix:

```rust
fn save_issues(issues: &[Issue], path: &Path) -> Result<()> {
    let data = serde_json::to_string_pretty(issues)?;
    std::fs::write(path, &data)
        .with_context(|| format!("Failed to write issues to {}", path.display()))?;
    Ok(())
}
```

**Round 2 - Fresh context. The Adversary says:**

> "If the program crashes between clearing the file and finishing the write, you lose all data. This isn't atomic. Write to a temporary file first, then rename it over the original. Also, you're holding all issues in memory and serializing the entire list every time. That's fine for 100 issues, but what happens at 100,000?"

The atomicity concern is real. The 100,000 issue concern is arguably premature for a personal issue tracker, but it's worth a comment in the code acknowledging the limitation. You fix the atomic write, note the scaling limitation, and submit again.

**Round 3 - Fresh context. The Adversary says:**

> "The function takes `&[Issue]` which means the caller has to load all issues into memory before saving. Consider a streaming approach that writes issues incrementally."

This is where it gets interesting. A streaming JSON writer for a personal issue tracker that will never have more than a few hundred issues? That's overengineering. The Adversary is reaching. You push back:

> "This is a personal CLI tool. The in-memory approach is fine for the expected scale. The atomic write handles the crash case. The streaming suggestion would add complexity without meaningful benefit."

The last suggestion is not proportionate to the stated scale, so you document why it was rejected. The work is done only if the original acceptance criteria, atomic-write tests, and agreed quality checks pass—not because the reviewer reached for a weak critique.

Notice what happened: the first draft was functional but fragile. The final version handles real failure modes (data loss on crash, missing context in errors, unreadable output). None of those improvements came from testing. They came from someone looking at the code with the specific intent of finding what's wrong. That's the value of the roast.

## The Principles Behind It All

If you take nothing else from this chapter, take these:

**Treat the first draft as a candidate.** A working first version is a starting point. Review and testing can improve confidence, but the process is only useful when its checks match the real requirements and risks.

**Specific disagreement can be productive.** A review is valuable when it exposes assumptions and produces testable findings. Tone does not determine quality; evidence, relevance, and follow-through do.

**Track material work and decisions.** Significant changes should be traceable to a requirement, defect, or maintenance need. Do not turn trivial actions into bookkeeping, but preserve enough context for another person to understand why the code changed.

**Refresh context deliberately.** Long conversations can drift, context can become stale, and reviewers can anchor on earlier assumptions. Restate requirements, use fresh perspectives where useful, and rerun the relevant checks as the work changes.

**Show evidence, don't assume.** "It should work" is not evidence. A passing test supports the behavior it asserts. A mathematical proof can be stronger evidence for a stated property under explicit assumptions. Match the evidence to the claim and risk.

## How This Applies to You Right Now

As an apprentice, you're not going to set up formal verification pipelines or run multi-model adversarial loops on day one. But you can start practicing the principles immediately:

**When you build something, write down what "done" looks like before you start.** This is verification-driven thinking. Define success, then build toward it, then check against it.

**When you think something works, try to break it.** Put in weird inputs. Refresh the page mid-action. Open it on your phone. Click things twice fast. Think like an adversary.

**When you submit work for review, ask for evidence.** A useful reviewer can say both what passed and what failed, cite specifics, and identify uncertainty. Fix confirmed problems; do not reward severity of tone over accuracy.

**Track work in pieces that produce inspectable progress.** Some behavior is only meaningful end to end, so use vertical slices and integration tests rather than forcing every code change into an isolated micro-task.

**Don't stop at the first success.** Stop when the defined evidence passes and the remaining risk is explicit and acceptable for the intended use.

## Exercises

1. Take the bookmark manager you built in Phase 1. Open a fresh conversation and ask: "Review this code against the attached design and acceptance criteria. Report confirmed defects separately from risks and questions. For each finding, cite the relevant requirement and code location, explain impact, and suggest a way to reproduce or test it." Triage what it finds. Which findings survive verification?

2. Take one critique from the adversarial review and fix it. Then submit the fix for another round of critique. Do this three times. Notice how the quality of the critiques changes as the code improves.

3. Pick one feature from your bookmark manager and write down every way it could break. Not just "the button doesn't work" level stuff. Think about: what if the data is corrupted in local storage? What if someone pastes a URL that's 10,000 characters long? What if tags contain special characters? Make a list, then check how many of these your current code handles.

4. Share your adversarial review experience in the guild [Discord](https://discord.gg/kfM6Q4UBbM) **#adversarial-review** channel. What was the most useful critique you received? What was the hardest to fix? What did you learn about your own blind spots? Reading other apprentices' review reports in that channel is almost as valuable as running your own.

This methodology is the backbone of the curriculum. Its practices should evolve with evidence. DORA's 2025 research describes AI as an [amplifier of existing organizational strengths and weaknesses](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/), and METR has observed agents that implement core functionality yet miss [merge-ready quality checks](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/). The durable lesson is to define evidence, preserve human accountability, and improve the process when measurements disagree with the story.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Finding Answers](../01-talking-to-agents/07-finding-answers.md) | **How We Build** | [Tracking Your Work →](02-tracking-your-work.md) |

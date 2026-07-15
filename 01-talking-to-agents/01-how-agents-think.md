# How Agents Think

## Understanding Your Collaborator

Before you start directing an AI agent, it helps to understand what's actually happening when you talk to one. Not the deep technical details. You don't need to know how neural networks work any more than you need to know how an internal combustion engine works to drive a car. But you do need a practical mental model of what the agent is good at, what it struggles with, and why it sometimes does baffling things.

## The Core Reality: Pattern and Context

An AI coding agent combines a language model with a loop that may inspect files, call tools, run commands, and observe results. The model generates likely next actions from its training and current context; the tools provide fresh evidence. Exact behavior varies by product and configuration.

**Generation is not retrieval.** The model can produce a plausible statement without looking it up. Some agents also have search, documentation, or repository tools, but they must actually use those tools and cite or show the result for it to count as current evidence. Fluent output can still be wrong.

**It fills gaps probabilistically.** If you say "make a button," the agent must infer appearance, placement, behavior, and text from context and common patterns. More relevant context and explicit acceptance criteria reduce unnecessary guessing, but excessive instructions can also conflict or obscure the goal.

**Do not assume complete memory between sessions.** Some products retain chat history, project instructions, summaries, or user memory; others do not, and retained state may be partial. Put durable decisions in the repository and ask the agent to inspect them at the start of a task.

**Reliability is task- and context-dependent.** Focused tasks with observable completion criteria are easier to inspect than sprawling, ambiguous ones. Do not split work so finely that the agent loses the end-to-end behavior; prefer coherent vertical slices that can be tested. METR's [time-horizon methodology](https://metr.org/time-horizons/) similarly measures that success rates fall as independently scoped tasks require longer human-expert work, while warning that capability is jagged across domains.

## The Context Window

Every agent has what's called a context window: the amount of text it can "see" and work with at one time. Think of it as the agent's working memory. Everything you've said in the current conversation, everything the agent has replied, and any files or documents you've shared all take up space in this window.

When working context gets crowded, products may omit, retrieve, or summarize older material. The implementation is not always visible to you, and large repositories can exceed what the agent examines carefully. This has practical consequences:

- **Important details should be restated, not just referenced.** Don't say "remember what I said earlier about the color scheme." Say "the color scheme is navy blue and white, as I mentioned before."
- **Long conversations should be broken into focused sessions.** If you've been going back and forth for hours, the agent's responses might start drifting. Start a new conversation, re-establish context, and continue.
- **Design documents are an anchor.** They preserve intent across sessions. Point the agent to the current design, then have it compare that document with the repository and tracker; no single document provides complete context automatically.

## What Agents Are Great At

Knowing what your collaborator excels at helps you delegate well:

**Generating and editing code from descriptions.** Agents are useful for syntax, boilerplate, routine transformations, and exploring implementations. "Best practices" and library APIs must still be checked against the current project and official documentation.

**Explaining things.** Agents can provide useful explanations at different levels. Validate explanations about security, versions, or unfamiliar code against primary sources and observed behavior.

**Debugging.** Exact errors, reproduction steps, tests, and logs give an agent strong evidence for diagnosing common failures. A proposed fix still needs to reproduce the bug and pass regression tests.

**Exploring options.** "What are three different ways I could structure a task management app?" will give you multiple approaches to consider before committing to one. Really valuable in the design phase.

**Refactoring and improving.** Once something works, you can ask the agent to improve it. "Make this faster," "make this more readable," "add error handling." These are tasks agents handle well because they're well-defined transformations of existing code.

## What Agents Struggle With

Just as important is knowing where agents fall short, so you can compensate:

**Maintaining consistency across a large project.** If your project spans many files and thousands of lines, the agent might make changes in one place that contradict something in another. This is a context window limitation. You manage it by working in focused chunks and verifying as you go.

**Knowing what you actually want.** The agent has zero insight into your goals, preferences, and constraints beyond what you tell it. It won't ask "wait, who is this for?" or "have you considered that your users might need accessibility features?" unless you've set up that expectation. You're the one who brings domain knowledge and judgment.

**Calibrating uncertainty.** Agents may answer beyond the available evidence. Ask for sources, assumptions, confidence, and concrete verification steps, then check them. This is why **VDD** (Verification Driven Development) defines success criteria and evaluates outputs rather than trusting tone.

**Understanding your specific environment.** The agent doesn't know what operating system you're on, what other software you have installed, what version of things you're running, or what your file structure looks like. Unless you tell it. When things don't work, missing context is often the reason.

## The Collaboration Model

The most productive way to think about working with an agent is as a collaboration between two very different kinds of intelligence:

**You bring:** Intent, judgment, domain knowledge, verification, taste, the ability to say "no, that's not right." You're the quality control. You're the one who knows what "done" looks like.

**The agent can bring:** Rapid generation, broad learned patterns, tool use, and help with syntax you do not need to memorize. Its availability, accuracy, and persistence remain bounded by the product and task.

The division of labor depends on the person and task. The agent supplies breadth and execution; you supply goals, authorization, domain judgment, and accountability. AI can speed some bounded tasks and slow others. A [GitHub-sponsored controlled task](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) found a large speedup in one JavaScript exercise, while METR found experienced open-source maintainers were [19% slower in an early-2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Treat productivity as something to measure in your workflow, not a universal promise.

This is the core reframe of the guild: learn to work with AI while keeping authority, evidence, and accountability visible. Whether it improves a particular outcome is something to measure, not assume.

## Practical Implications

Here's what all of this means for your day-to-day work:

1. **Be specific.** The agent can't read your mind. Every detail you leave out is a detail the agent guesses about. Some guesses will be wrong.

2. **Verify everything.** The agent will sound confident even when it's wrong. Don't trust the output. Test it. Does it work? Does it do what you asked? Does it handle edge cases?

3. **Manage context deliberately.** Keep conversations focused. Restate important details. Use design documents as anchors. Start fresh sessions when conversations get long.

4. **Break work into focused tasks.** Big vague requests produce big vague results. Small specific requests produce small specific results you can assemble into something great.

5. **Iterate deliberately.** Ask, inspect the diff, run checks, compare against the requirement, and refine. Count verified progress rather than generations; fast output that creates rework is not speed.

Now that you understand how your collaborator works, let's learn how to talk to it.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Guild](../00-foundations/06-the-guild.md) | **How Agents Think** | [The Art of Intent →](02-the-art-of-intent.md) |

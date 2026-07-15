# Foreword: On Being Wrong

Before you start, there's something you need to hear.

You are going to be wrong sometimes. Early prompts will miss details, builds will have bugs, design docs will have gaps, and reviews may surface problems you did not see.

That is not a verdict on your ability. A useful process turns a mistake into observable feedback, a correction, and a check that can catch the same class of problem later.

## The Ego Problem

It is easy to treat being wrong as a judgment about intelligence rather than information about one attempt. That instinct can make people hide uncertainty, avoid tests, or defend a result after the evidence changes.

That instinct will hold you back here.

In this program, a compiler error is evidence about a violated language rule. Diagnostics often identify a location and suggest a repair, though the first reported line may be a symptom and a suggestion may not match your intent.

A good review focuses on the work: "this doesn't handle empty input," "this error lacks context," or "this function mixes unrelated responsibilities." The reviewer's tone and motivation are not evidence. Evaluate the finding against the requirement, code, and a reproduction or test.

## Failure Is the Curriculum

Do not make first-try perfection the goal. You can improve prompts by comparing them with the assumptions they produced, improve verification by designing checks before release, and improve decomposition by observing where scope and integration become hard to review.

Experience alone does not guarantee learning. The learning comes from predicting, observing, diagnosing, correcting, and reflecting. Keep the failures safe and scoped: tests and disposable exercises are better teachers than leaking data or breaking a production system. The curriculum's learning log exists to connect attempts with evidence and next steps; [structured reflection has educational support](RESEARCH.md#what-the-evidence-supports).

## What the Roast Actually Is

The curriculum sometimes calls adversarial review "the roast." The useful part is not brutality. A reviewer examines work you're proud of against explicit requirements and risks, then gives specific findings you can verify.

Here's what that actually means:

**It makes the work inspectable.** A detailed review should name what was examined, what evidence supports each finding, and what was out of scope. A shallow "looks fine" provides little evidence, but a long review can still be wrong.

**Respect and rigor coexist.** Direct feedback does not require humiliation. Review the artifact, explain impact, distinguish fact from preference, and leave the author able to act on the result.

**It means the focus is on the work, not on you.** "This function doesn't validate input" is about the function. It's not about your intelligence, your worth, or your potential. Learning to separate yourself from your output is one of the most important things you'll do here. You are not your code. Your code can be bad while you are learning. Both of those things are fine.

## How to Take Feedback

Some practical advice for when the critique comes:

**Read it all before reacting.** Don't fix things one by one as you read. Take in the full picture first. Often the critiques are related, and addressing the root cause fixes several of them at once.

**Ask yourself: is this true?** Not "does this feel good?" but "is this accurate?" If the reviewer says your error handling is weak and you look at the code and it is in fact weak, that's a true statement regardless of how it feels to hear it.

**Separate the useful from the noise.** Not every critique will be valid. Reproduce findings where practical and compare them with the acceptance criteria. Fix confirmed problems, document proportionate risk decisions, and reject unsupported suggestions with evidence. A reviewer's lack of good findings is not an exit signal by itself.

**Acknowledge useful feedback.** A confirmed defect found before release is valuable. You can appreciate that contribution while still challenging inaccurate, irrelevant, or disrespectful feedback.

**Track your growth.** After a few review cycles, look back at your first one. The things that got flagged in your early work won't show up in your later work. That's growth. It's visible, measurable, and it only happened because someone was honest with you about what was wrong.

## The Compiler as Teacher

Rust's compiler deserves a special mention here, because you're going to spend a lot of time arguing with it.

The Rust compiler is famously strict. It rejects some code that other languages accept, including code that violates Rust's ownership and borrowing rules. Its diagnostics can be long, but they usually identify the location and the constraint that was violated.

This is useful evidence, not proof that the program is correct. Some compiler errors prevent real safety problems; others are ordinary type, syntax, or lifetime mistakes, and code that compiles can still have logic bugs. Rust's strongest memory-safety guarantees apply to safe Rust; `unsafe` code and foreign-function boundaries still require manual review. The [Rustonomicon explains that boundary](https://doc.rust-lang.org/nomicon/safe-unsafe-meaning.html).

When you get a compiler error, inspect the full diagnostic, locate the earliest relevant cause, and ask why the proposed repair preserves the design. The compiler can repeat this feedback consistently; use it as one part of the evidence loop.

## The Deal

Here's what we're asking of you:

Hold conclusions lightly. Treat errors, critiques, and failed builds as evidence to evaluate rather than judgments about the person. Preserve what you learned, add a regression check when appropriate, and make the next attempt from a better model.

That practice can develop skill in directing coding agents, reading their changes, and deciding what evidence is sufficient for a particular use. The portfolio should show the work honestly; it does not need a mythology of perfection or punishment.

Let's begin.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Evidence and Freshness](RESEARCH.md) | **Foreword** | [The New Literacy →](00-foundations/01-the-new-literacy.md) |

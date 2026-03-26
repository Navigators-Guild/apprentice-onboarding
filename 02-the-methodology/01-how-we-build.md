# How We Build

## The Discipline Behind the Tools

You know how to talk to agents. You know how to break problems down, provide context, and verify output. You've built something. Now it's time to talk about *how the guild actually builds software*, because there's a method to it, and the method is what separates work that holds up from work that falls apart the moment someone looks at it sideways.

The methodology is called **Verification-Driven Development (VDD)**, and the engine that powers it is **Iterative Adversarial Refinement (IAR)**. Those are fancy names for a simple idea: build something, prove it works, then hand it to someone whose entire job is to tear it apart. Fix what they find. Repeat until they can't find anything real to complain about.

## Why "It Works" Isn't Good Enough

When you build something with an agent and it runs without errors, it's tempting to call it done. It works. Ship it.

The problem is that "it works" and "it works correctly" are very different things. Code can run without crashing and still be full of problems. Maybe it handles the happy path fine but breaks on weird input. Maybe it does the right thing most of the time but has a subtle logic error that only shows up on the last day of the month. Maybe it works perfectly today but is structured in a way that makes it impossible to change tomorrow.

The first version of anything is usually the most dangerous version, because it *looks* done. It passes the "does it run?" test. But it hasn't been stressed, questioned, or challenged. VDD exists because we don't trust the first version. We trust the version that survived the process.

## The Three Roles

VDD works by putting three different perspectives in a loop:

**The Builder** is the AI agent doing the actual construction. It plans, writes code, writes tests, and implements features. In our workflow, this is typically Claude (or whichever agent you're directing). The Builder is fast, knowledgeable, and eager to produce output. It is also prone to taking shortcuts, generating plausible-looking code that has subtle issues, and saying "done" before things are actually done. That's not a flaw. It's just what happens when you optimize for generation speed. The process accounts for it.

**The Human (You)** is the director. You set the goals, define what "correct" means, do the manual verification ("does this actually do what I asked?"), and make judgment calls. You're the one who knows the domain, the audience, and the purpose. The Builder doesn't know any of that unless you tell it. Your job is also to mediate between the Builder and the Adversary, deciding which critiques are real problems and which are noise.

**The Adversary** is the critic. In the guild, this role is filled by a separate AI prompted to be harsh, impatient, and cynical. Its job is to find every flaw, question every assumption, and point out every shortcut. It's not trying to be helpful in the encouraging sense. It's trying to break your work. This is the "roast" in adversarial review, and it's the core of IAR.

The key insight: these three roles create tension on purpose. The Builder wants to produce. The Adversary wants to destroy. You sit in the middle, using the tension to drive the work toward something genuinely solid.

## The Loop

Here's how it works in practice:

### Step 1: Break It Down

Before any code gets written, the work gets decomposed. You already learned this in Phase 1, but VDD takes it further. Every project gets broken into a hierarchy:

- **Epics** are the big goals. "Build user authentication" is an epic.
- **Issues** are the functional pieces within an epic. "Create login endpoint," "add password hashing," "build session management" are issues.
- **Sub-issues** are the atomic units. Each one is a single, testable piece of work that can be verified independently. "Hash passwords with bcrypt using cost factor 12" is a sub-issue.

Think of it like a string of beads. Each bead is a sub-issue. The string is the epic. Every bead has to be accounted for. No gaps, no "we'll figure that out later," no hand-waving. If something needs to happen, there's a bead for it.

This matters because it creates **linear accountability**. Every piece of code traces back to a specific sub-issue. Every sub-issue traces to an issue. Every issue traces to an epic. When something breaks, you can follow the chain backwards and find exactly where the problem lives. When someone reviews your work, they can see that nothing was skipped.

### Step 2: Build and Verify

The Builder implements the sub-issues one at a time. For each one:

1. **Write the code** that implements the feature or fix.
2. **Write tests** that prove it works. Not just "it doesn't crash" tests. Tests that check the actual behavior: does the right thing happen with good input? Does the right error happen with bad input? Do edge cases get handled?
3. **You verify manually.** Does this match what you asked for? Does it feel right? Does it do what the design doc says it should do? This is the human-in-the-loop step, and it catches the things automated tests can't: intent mismatches, UX problems, "technically correct but not what I meant" situations.

Only after you're satisfied that a piece works does it move to the next step.

### Step 3: The Roast

This is where it gets interesting. You take your verified, tested code and hand it to the Adversary. The Adversary's job is to find everything wrong with it.

A few things make the roast effective:

**The Adversary is prompted to be harsh.** Not rude for the sake of it, but genuinely zero-tolerance. Placeholder comments? Called out. Generic error handling? Called out. Inefficient patterns the Builder used because they were easy? Called out. The Adversary doesn't care about your feelings or the Builder's. It cares about the code.

**Fresh eyes every time.** The Adversary gets a clean context for every review. This is important. When an AI stays in a long conversation, it tends to get agreeable. It starts accepting things it would have questioned earlier. By resetting the context, every roast hits with the same intensity as the first one. No drift, no softening, no "well, I already mentioned that last time so I'll let it slide."

**It's looking for patterns, not just bugs.** The Adversary catches things like: "You wrote the same error handling logic in six places instead of extracting it." "This function does three unrelated things." "Your test only covers the happy path." "This will break if someone passes null." These are the problems that working code hides from casual inspection.

### Step 4: Fix and Repeat

The Builder takes the Adversary's critique and addresses it:

1. Fix the real problems.
2. Refactor the weak spots.
3. Write new tests for the edge cases the Adversary found.

Then it goes back to the Adversary. Fresh context, fresh roast. The cycle repeats.

## Testing Against Hard Truths

As the loop tightens and the obvious problems get fixed, something interesting happens: the remaining issues get subtler. The Adversary starts finding edge cases that are hard to test with normal unit tests. "What if this number overflows?" "What if two users hit this endpoint at the exact same millisecond?" "What if the input is technically valid but astronomically large?"

This is where VDD pushes beyond standard testing into what we call **hard truths**: verification methods that don't just check if code works for a set of examples, but prove that certain categories of failure are impossible.

For an apprentice, you don't need to implement these yet. But you should understand the concept:

- **Standard testing** says "I tried 50 inputs and they all worked." That's useful, but it doesn't tell you about input #51.
- **Hard truth testing** says "I can mathematically prove this function will never overflow, for any input, ever." That's a different level of confidence.

In practice this means integrating tools into your build pipeline that do things like check for memory safety violations, arithmetic overflows, or known security vulnerabilities. The code doesn't just have to pass tests. It has to pass *proofs*.

You'll encounter this more as you advance through the guild. For now, the takeaway is: the goal isn't "it works when I try it." The goal is "I have evidence that it works, and I have evidence about the ways it *can't* fail."

## Knowing When You're Done

One of the hardest things in any creative process is knowing when to stop. VDD has an elegant answer to this.

Remember that the Adversary is prompted to find problems. It *wants* to find problems. It will always try to produce critique, because that's its job.

So what happens when the code is actually good? The Adversary starts making things up. It nitpicks things that aren't real issues. It misreads the code. It invents scenarios that can't actually happen. Its critiques stop being grounded in reality.

This is the exit signal. When the Builder can look at the Adversary's feedback and say "that's not a real problem, you're hallucinating," and this happens consistently across multiple rounds, the code has reached what VDD calls **maximum viable refinement**. The Adversary literally cannot find real problems anymore. It's been pushed to the point of inventing them.

This is a much better stopping point than "I feel like it's done" or "I'm tired of working on this." It's an observable signal: the harshest possible critic has run out of legitimate complaints.

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

The Adversary was forced to invent a problem because the real ones are fixed. That's the exit signal. Three rounds, two real improvements, one hallucinated critique. Done.

Notice what happened: the first draft was functional but fragile. The final version handles real failure modes (data loss on crash, missing context in errors, unreadable output). None of those improvements came from testing. They came from someone looking at the code with the specific intent of finding what's wrong. That's the value of the roast.

## The Principles Behind It All

If you take nothing else from this chapter, take these:

**Don't trust the first draft.** The first version that works is not the best version. It's the starting point. The process that comes after is where quality actually happens.

**Friction is productive.** The adversarial loop feels uncomfortable. Getting your work torn apart isn't fun. But that friction is what polishes the output. Smooth, agreeable feedback produces smooth, mediocre work. Harsh, specific feedback produces work that holds up.

**Track everything.** Every piece of work should be traceable. If you can't point to why a piece of code exists and what requirement it satisfies, it's either unnecessary or undocumented. Both are problems.

**Fight entropy.** Long conversations drift. Contexts get stale. Reviewers get soft. VDD fights this by resetting context, enforcing fresh perspectives, and never letting the process coast. Quality degrades by default. You have to actively maintain it.

**Prove, don't assume.** "It should work" is not evidence. "Here's a test that proves it works" is evidence. "Here's a mathematical proof that it can't fail in this specific way" is strong evidence. Move up this ladder as your skills grow.

## How This Applies to You Right Now

As an apprentice, you're not going to set up formal verification pipelines or run multi-model adversarial loops on day one. But you can start practicing the principles immediately:

**When you build something, write down what "done" looks like before you start.** This is verification-driven thinking. Define success, then build toward it, then check against it.

**When you think something works, try to break it.** Put in weird inputs. Refresh the page mid-action. Open it on your phone. Click things twice fast. Think like an adversary.

**When you submit work for review, welcome the roast.** The harshest feedback is the most valuable. If someone tells you "this is great, no notes," be suspicious. If someone tears it apart with specific critiques, be grateful. Then fix it.

**Track your work in pieces small enough to verify.** If you can't test a piece of your project independently, it's too big. Break it down further.

**Don't stop when it works. Stop when you can't break it.** That's a different bar, and clearing it is what builds real skill.

## Exercises

1. Take the bookmark manager you built in Phase 1. Pretend you're the Adversary. Open a conversation with an agent and prompt it like this: "I'm going to show you some code. Your job is to be extremely critical. Find every flaw, every shortcut, every edge case that isn't handled. Don't be nice about it." Then paste your code. How much does it find? Were you surprised?

2. Take one critique from the adversarial review and fix it. Then submit the fix for another round of critique. Do this three times. Notice how the quality of the critiques changes as the code improves.

3. Pick one feature from your bookmark manager and write down every way it could break. Not just "the button doesn't work" level stuff. Think about: what if the data is corrupted in local storage? What if someone pastes a URL that's 10,000 characters long? What if tags contain special characters? Make a list, then check how many of these your current code handles.

4. Share your adversarial review experience in the guild channel. What was the most useful critique you received? What was the hardest to fix? What did you learn about your own blind spots?

This methodology is the backbone of everything we do in the guild. The tools will change, the agents will get better, the specific techniques will evolve. But the core loop (build, verify, get roasted, fix, repeat) works because it's built on honest feedback and hard evidence. That doesn't go out of date.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Finding Answers](../01-talking-to-agents/07-finding-answers.md) | **How We Build** | [Tracking Your Work →](02-tracking-your-work.md) |

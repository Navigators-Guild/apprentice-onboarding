# When Things Break

## The Skill Nobody Teaches

Every tutorial shows you the happy path. Do this, get that, it works. Real building isn't like that. Things break. The agent gives you code that doesn't compile. The code compiles but does the wrong thing. It works on your machine but not in the browser. You get an error message that looks like someone smashed their keyboard.

This chapter is about what to do when things go wrong, because they will, and how you handle failure is more important than how you handle success.

## Reading Error Messages

Error messages look intimidating. They're often long, full of technical terms, and formatted in ways that seem designed to confuse. But they're actually trying to help you. Learning to read them (or at least extract the useful parts) is one of the most practical skills you'll develop.

Here's a typical error message you might see when building a Rust project:

```
error[E0382]: borrow of moved value: `name`
  --> src/main.rs:12:20
   |
10 |     let name = String::from("hello");
   |         ---- move occurs because `name` has type `String`
11 |     let greeting = format!("Hi, {name}");
   |                                  ---- value moved here
12 |     println!("{name}");
   |                ^^^^ value borrowed here after move
```

You don't need to understand what "borrow of moved value" means. What you need to see is:

1. **The file and line number:** `src/main.rs:12:20`. That's where the problem is.
2. **The arrow pointing to the specific code:** `println!("{name}")`. That's the line that's wrong.
3. **A description of what happened:** Something about `name` being used after it was moved.

That's enough context to ask your agent for help:

> "I'm getting this error when I run cargo build: [paste the full error]. What's wrong and how do I fix it?"

The agent will explain it and fix it. You don't need to become an expert in Rust's ownership system to get past this. You need to be able to find the error, copy it, and ask.

**The habit:** When something breaks, read the error message before panicking. Look for a file name, a line number, and any plain-English description. Then share the full error with your agent. Don't paraphrase. Don't summarize. Paste the whole thing. Agents are very good at diagnosing errors when they can see the exact text.

## When the Agent Gives You Broken Code

It happens. The agent generates code that doesn't compile, doesn't run, or crashes immediately. This doesn't mean the agent is bad or that you did something wrong. It means the agent made a mistake, same as a human collaborator would.

**Don't start over.** The instinct when something doesn't work is to scrap it and try again. Resist this. The code the agent wrote is probably 90% correct. The problem is usually specific and fixable.

**Report what happened, not what you think is wrong.** The most effective debugging prompt is:

> "I ran cargo build and got this error: [paste error]. Here's the current code: [paste code or share file]. Fix it."

The worst debugging prompt is:

> "It doesn't work."

That tells the agent nothing. It doesn't know what "it" is, what "work" means to you, or what happened when you tried. Be specific:

- What command did you run?
- What did you expect to happen?
- What actually happened?
- What was the exact error message (if any)?

**Iterate, don't restart.** If the first fix doesn't work, share the new error. "I applied your fix and now I get this different error: [paste]." Each iteration narrows the problem. Restarting from scratch throws away that progress.

## When the Code Runs but Does the Wrong Thing

This is harder than an error message, because the code appears to work. No crashes, no errors. It just doesn't do what you wanted.

The problem is almost always a gap between what you said and what the agent understood. Go back to your original prompt and compare what you asked for against what you got:

- Did you say "sort by priority" but it sorted alphabetically?
- Did you say "save to a file" but it saves in a format you can't read back?
- Did you ask for "a search that matches partial words" but it only matches exact strings?

When you find the gap, be specific about it:

> "The search function only matches if I type the exact full title. I want it to match partial strings too. If I type 'log' it should find an issue titled 'Fix login bug.' Update the search to match substrings."

This is refinement, not failure. The agent did what it thought you meant. Now you're clarifying.

## When You Have No Idea What's Wrong

Sometimes the code doesn't work and you can't tell why. No error message, or an error message that means nothing to you. The output is wrong but you're not sure how.

**Use the agent as a debugger:**

> "This code is supposed to [describe expected behavior] but instead it [describe actual behavior]. I don't know why. Walk me through what the code is actually doing step by step."

The agent will trace through the logic and usually spot the problem. This works because agents are good at reading code and explaining execution flow, even when the code is wrong.

**Add print statements (or ask the agent to):**

> "Add print statements at each step of the search function so I can see what's happening when it runs. Print the input, the intermediate results, and the output."

This is the oldest debugging technique in existence and it still works. You run the code, look at what gets printed, and find the step where the output stops matching your expectations.

**Isolate the problem:**

> "The full program isn't working right but I think the problem is in the search function. Write a small test that calls the search function directly with a known input and prints the result, so we can check if search is the issue or if it's something else."

Narrowing down where the problem lives is half the battle. Once you know *which* function is wrong, fixing it is usually straightforward.

## Common Failure Patterns

After a while, you'll start recognizing categories of failures. Here are the ones beginners hit most often:

**The missing dependency.** The agent wrote code that uses a library you haven't installed. In Rust, this shows up as `unresolved import` or `can't find crate`. The fix: tell the agent to add the dependency to Cargo.toml, or run `cargo add [library-name]`.

**The wrong version.** The agent used a function or syntax from a different version of a library than what you have. This is common because agents draw on training data that might be slightly outdated. The fix: share the exact error and ask the agent to update the code for the version you have installed.

**The environment assumption.** The agent assumed you have something installed that you don't, or that a file exists that doesn't, or that you're on a different operating system. The fix: tell the agent your environment. "I'm on Windows" or "I don't have Python installed" changes the solution.

**The stale context.** In a long conversation, the agent forgets or misremembers earlier decisions. It writes code that contradicts something you agreed on thirty messages ago. The fix: restate the relevant context. "Remember, we're storing data as JSON in a local file, not in a database."

**The silent failure.** The code runs but silently ignores errors. It tries to read a file, fails, and returns an empty result instead of telling you the file wasn't found. The fix: tell the agent to add proper error handling. "Don't silently swallow errors. If the file can't be read, print an error message explaining what went wrong."

## The Debugging Mindset

The most important thing about debugging isn't any specific technique. It's the mindset: **something specific is wrong, and you can find it.**

When beginners hit an error, there's a temptation to think "I broke everything" or "this is beyond me." It almost never is. It's almost always one specific thing: a wrong variable name, a missing import, an off-by-one error, a misunderstanding between you and the agent. The error is finite and findable.

Your process:

1. **Read the error.** Extract the file, line, and description.
2. **Share the full error with the agent.** Don't paraphrase.
3. **Describe what you expected vs what happened.** Be specific.
4. **Apply the fix and test.** If there's a new error, repeat from step 1.
5. **If you're lost, ask the agent to explain.** "Walk me through what this code does step by step."

This loop handles 95% of problems. The other 5% are where you learn the most, and the guild community is there for those.

## Exercises

1. Deliberately break something. Take your bookmark manager and introduce a bug: delete a closing bracket, misspell a variable name, or remove a function call. Then pretend you don't know where the bug is. Read the error message. Can you find the problem from the error alone, before fixing it?

2. Ask your agent to build something slightly ambiguous on purpose: "make a timer." Don't specify what kind of timer, what it counts, or how it displays. Look at what you get. Identify every gap between what you wanted and what the agent assumed. Write the corrected prompt that would have gotten the right result the first time.

3. Start a conversation with your agent and build something small (a unit converter, a tip calculator, whatever). When it works, break it by asking for a feature that conflicts with the existing code: "now make it work backwards too." Watch how the agent handles the conflict. If it introduces a bug, practice the debugging loop: read the error, share it back, iterate.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Your First Build](05-first-build.md) | **When Things Break** | [Finding Answers →](07-finding-answers.md) |

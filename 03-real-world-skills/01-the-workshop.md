# The Workshop

## Working in the Master's Shop

In a traditional guild, apprentices don't just build their own projects. They work in the master's shop, on the master's projects, alongside other apprentices. They learn to read before they write. They learn to work within existing patterns before they invent their own. They learn that most real work isn't greenfield creation. It's understanding what's already there and making it better.

The guild toolkit is your workshop.

## The Guild Toolkit

The toolkit lives at [github.com/Navigators-Guild/guild-toolkit](https://github.com/Navigators-Guild/guild-toolkit). It's a Rust workspace containing a collection of command-line tools the guild uses. Each tool is its own crate, its own binary, its own project. They share a common core library but are otherwise independent.

Here are the tools:

| Tool | What It Does | Difficulty |
|---|---|---|
| `guild-scaffold` | Set up new projects with the right structure, templates, and tooling | Beginner |
| `guild-progress` | Track where you are in the curriculum, what you've completed | Beginner |
| `guild-review` | Submit work for adversarial review, track review rounds | Intermediate |
| `guild-portfolio` | Generate a portfolio site from your project repos | Intermediate |
| `guild-search` | Search guild knowledge base and curriculum docs | Intermediate |
| `guild-deps` | Audit project dependencies for freshness, security, licenses | Intermediate |
| `guild-stats` | Project health metrics: test coverage, commit frequency, issue velocity | Intermediate |
| `guild-roast` | Automated adversarial review: point it at code, get a critique | Advanced |

There's also `guild-core`, a shared library that provides config loading, error types, output formatting, and a shared data model. Every tool depends on it.

The repository is active and changes over time. Some tools or tests may still be stubs; others may already be implemented. Inspect the current default branch and open issues instead of treating the table above as status.

## How This Is Different from Your Portfolio Projects

Your portfolio projects (the bookmark manager, the issue tracker) were greenfield. You started from nothing, wrote the design doc, built the whole thing. You owned every decision.

The workshop is the opposite. You're walking into an existing codebase with:

- **An architecture you didn't choose.** The workspace structure, the shared core library, the dependency versions, the data model. These are set. You work within them.
- **Conventions you need to follow.** How errors are handled, how output is formatted, how config is loaded. The patterns are established in `guild-core`. Your tool needs to match.
- **Other people's code.** Other apprentices are working on other tools in the same workspace. You'll see their commits, their patterns, their choices. You might need to use something they built in `guild-core`, or notice that they added something you can reuse.
- **An audience.** The tools you build here will be used by other guild members. That changes how you think about error messages, edge cases, documentation. It's not just for you anymore.

Existing codebases are a large part of professional software development. This is where you practice learning local patterns and contributing within an established structure.

## Getting Started

### Fork and clone the repo

Contributing to an upstream repository you don't own follows the **fork-and-PR** model. You don't push commits directly to `Navigators-Guild/guild-toolkit`. Instead, you make your own copy (a fork), push your work there, and open a pull request asking the maintainers to pull your changes back.

1. Go to [github.com/Navigators-Guild/guild-toolkit](https://github.com/Navigators-Guild/guild-toolkit) and click the **Fork** button in the top right. GitHub creates `github.com/YOUR-USERNAME/guild-toolkit` — your own copy with full push access.
2. Clone **your fork**, not the upstream:

   ```bash
   cd ~/guild-projects
   git clone https://github.com/YOUR-USERNAME/guild-toolkit.git
   cd guild-toolkit
   ```

3. Add the upstream repo as a second remote, fetch it, and create a local `develop` branch that tracks the branch used for apprentice contributions:

   ```bash
   git remote add upstream https://github.com/Navigators-Guild/guild-toolkit.git
   git fetch upstream
   git switch --create develop --track upstream/develop
   ```

Your `origin` is your fork (where you push). Your `upstream` is the canonical repository. The toolkit's current README says apprentice branches start from `develop` and PRs target `develop`, not `main`. Before new work, run `git switch develop`, `git fetch upstream`, and `git merge --ff-only upstream/develop`. Recheck the live README in case maintainers change this policy.

### Make sure it builds

```
cargo build --workspace
```

This compiles every crate in the workspace. If it succeeds, the workspace builds in your current environment; it does not verify tests, optional features, other platforms, or external services.

### Explore the structure

```
ls crates/
```

You'll see the tool directories. Pick one that interests you and look at what's there:

```
ls crates/guild-scaffold/src/
```

Inspect what is present now. The crate may be a stub or may have changed since this chapter was written. Read its source, tests, README, and related issues before changing anything.

### Read guild-core

Before you implement anything, map `guild-core`'s public surface and read the parts your issue touches. Understand where to find:

- How config is loaded (`config.rs`)
- What the shared data model looks like (`data.rs`)
- How errors are defined (`error.rs`)
- How output formatting works (`output.rs`)

You don't need to memorize it or read unrelated internals. You need enough context to reuse established types and helpers where appropriate. Ask the agent to cite the definitions it plans to use.

### Pick a tool

Look at the difficulty ratings. If this is your first workshop contribution, start with a beginner tool (`guild-scaffold` or `guild-progress`). Read the tool's `README.md` in its crate directory for a description of what it should do.

Then open a conversation with your agent. Replace the example tool and feature with a current, unclaimed issue:

> "I'm working on the guild-toolkit project. Here's the workspace structure [share Cargo.toml]. Here's the shared core library [share guild-core source]. I want to implement guild-progress, which tracks where an apprentice is in the curriculum. Here's the tool's README [share it]. Build the first layer: it should read the curriculum structure and display which chapters the user has completed."

The agent builds within the existing structure because you gave it the context. It uses `guild-core`'s types because you told it they exist. This is context management in action, the same skill from Phase 1, applied to a more complex situation.

## The Contribution Process

Working on the toolkit isn't just coding. It follows a process:

### 1. Claim the work

Check the [current issues](https://github.com/Navigators-Guild/guild-toolkit/issues), contribution instructions, linked PRs, and recent activity. Comment or follow the maintainer's claim convention before investing in an issue. A local crosslink entry can track your work, but the GitHub issue is the shared coordination record.

### 2. Read before you write

Before changing anything, read the relevant parts of `guild-core`, the tool's current state, tests, and related data formats. Reading the entire workspace may be unnecessary; ask the agent to map dependencies, then verify the files it identifies.

### 3. Design before you build

Write a brief design doc or issue description for what you plan to implement. This doesn't need to be formal. "I'm going to make guild-progress read the curriculum TOML and display a checklist of phases and chapters with completion status" is enough. Share it for feedback before you start.

### 4. Build in layers

Same process as your portfolio projects. Start with the simplest useful version. Verify it works. Add the next feature. The VDD loop doesn't change just because the project is bigger.

### 5. Submit a pull request

When your feature is working and tested, submit a pull request (PR) to the guild-toolkit repo. If you haven't yet read the [Branches and Pull Requests](../02-the-methodology/03-branches-and-pull-requests.md) chapter from Phase 2, go do that first—it covers the branch operations and GitHub web workflow you'll use here. The short version:

- Refresh `develop`, then create a feature branch that follows the repository's current naming convention
- Commit your work on the branch as usual, then push it with `git push -u origin HEAD` the first time
- Open the PR on github.com with the canonical repository's `develop` branch as the base; the description should reference the issue and explain what changed and why
- Run the repository's documented local checks and ensure every required CI check passes; if the repository has no CI, report the gap rather than claiming CI passed
- Other guild members will review your code
- Address feedback with new commits on the same branch (they show up in the PR automatically)
- Once approved and green, a maintainer merges the PR and your code ships

This is the first time your code goes through review by people other than your agent. It's the closest thing to the traditional apprentice-submits-work-to-the-master moment.

### 6. Your contribution is evaluated

If maintainers merge the PR, your code becomes part of the toolkit. A submitted or reviewed PR is still useful evidence when maintainers request changes, choose another approach, or close it; open-source contribution does not guarantee merge or adoption.

## What You Learn Here

This workshop emphasizes skills that guided greenfield projects exercise less directly:

**Reading existing code.** The most underrated skill in software. Most of your time as a practitioner will be spent understanding what exists, not writing new things. The workshop forces this by design.

**Working within constraints.** You can't redesign the data model because your tool would be easier with a different structure. You use what's there. This is every job you'll ever have.

**Collaboration.** Other people are working in the same codebase. Your changes can't break their tools. You need to be aware of shared state, shared dependencies, shared conventions.

**The PR process.** Design, implement, submit, get reviewed, address feedback, merge. This is how professional open source and team development works. Your portfolio projects didn't have this step.

**Building for others.** Your portfolio projects were for you. These tools are for the guild. Error messages need to be clear for someone who isn't you. Documentation needs to exist. Edge cases matter because real people will hit them.

## Exercises

1. Clone the guild-toolkit repo and build the workspace. Explore the structure. Read guild-core's source. Don't change anything yet. Just read. Then write a paragraph describing how the shared data model works and how tools are expected to use it. Share it in the guild [Discord](https://discord.gg/kfM6Q4UBbM) **#apprentice-level** channel for feedback on your understanding.

2. Pick a beginner tool and implement its first feature. Follow the full process: claim the work, design before building, build in layers, submit a PR.

3. Review someone else's PR on the toolkit. Read their code, test it locally, and leave specific feedback. This is your first time being the reviewer rather than the reviewed. Be constructive and specific, just like the best roast feedback you've received.

4. After your first PR is merged, find an issue on an intermediate tool. Notice how the process feels different when you already know the codebase.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Branches and Pull Requests](../02-the-methodology/03-branches-and-pull-requests.md) | **The Workshop** | [Working with APIs →](02-working-with-apis.md) |

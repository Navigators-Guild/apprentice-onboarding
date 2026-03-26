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

The tools start as stubs. A clap argument parser, a help message, and nothing else. Apprentices implement them.

## How This Is Different from Your Portfolio Projects

Your portfolio projects (the bookmark manager, the issue tracker) were greenfield. You started from nothing, wrote the design doc, built the whole thing. You owned every decision.

The workshop is the opposite. You're walking into an existing codebase with:

- **An architecture you didn't choose.** The workspace structure, the shared core library, the dependency versions, the data model. These are set. You work within them.
- **Conventions you need to follow.** How errors are handled, how output is formatted, how config is loaded. The patterns are established in `guild-core`. Your tool needs to match.
- **Other people's code.** Other apprentices are working on other tools in the same workspace. You'll see their commits, their patterns, their choices. You might need to use something they built in `guild-core`, or notice that they added something you can reuse.
- **An audience.** The tools you build here will be used by other guild members. That changes how you think about error messages, edge cases, documentation. It's not just for you anymore.

This is what professional software development looks like. Almost nobody starts from a blank screen. Almost everybody inherits a codebase, learns its patterns, and contributes within its structure. This is where you practice that.

## Getting Started

### Clone the repo

```
cd ~/guild-projects
git clone https://github.com/Navigators-Guild/guild-toolkit.git
cd guild-toolkit
```

### Make sure it builds

```
cargo build --workspace
```

This compiles every crate in the workspace. If it succeeds with no errors, your environment is set up correctly.

### Explore the structure

```
ls crates/
```

You'll see the tool directories. Pick one that interests you and look at what's there:

```
ls crates/guild-scaffold/src/
```

You'll find a `main.rs` with a clap argument parser and a help message. That's the starting point. Read it. Understand what's there before you change anything.

### Read guild-core

Before you implement anything, read through `guild-core`. This is the foundation everything else builds on. Understand:

- How config is loaded (`config.rs`)
- What the shared data model looks like (`data.rs`)
- How errors are defined (`error.rs`)
- How output formatting works (`output.rs`)

You don't need to memorize it. You need to know what's available so you use it instead of reinventing it. When your agent generates code for your tool, you can say "use the output helpers from guild-core" instead of letting it create its own.

### Pick a tool

Look at the difficulty ratings. If this is your first workshop contribution, start with a beginner tool (`guild-scaffold` or `guild-progress`). Read the tool's `README.md` in its crate directory for a description of what it should do.

Then open a conversation with your agent:

> "I'm working on the guild-toolkit project. Here's the workspace structure [share Cargo.toml]. Here's the shared core library [share guild-core source]. I want to implement guild-progress, which tracks where an apprentice is in the curriculum. Here's the tool's README [share it]. Build the first layer: it should read the curriculum structure and display which chapters the user has completed."

The agent builds within the existing structure because you gave it the context. It uses `guild-core`'s types because you told it they exist. This is context management in action, the same skill from Phase 1, applied to a more complex situation.

## The Contribution Process

Working on the toolkit isn't just coding. It follows a process:

### 1. Claim the work

Check what issues exist on the repo. If someone is already working on the tool you want, pick a different one or find a sub-feature to work on. Use Chainlink to track your work as always.

### 2. Read before you write

Before changing anything, read the existing code. All of `guild-core`. The tool's current state. Any related tools. If your tool will read data that another tool writes, understand the data format. The agent can help: "explain what this module does" is a perfectly good prompt.

### 3. Design before you build

Write a brief design doc or issue description for what you plan to implement. This doesn't need to be formal. "I'm going to make guild-progress read the curriculum TOML and display a checklist of phases and chapters with completion status" is enough. Share it for feedback before you start.

### 4. Build in layers

Same process as your portfolio projects. Start with the simplest useful version. Verify it works. Add the next feature. The VDD loop doesn't change just because the project is bigger.

### 5. Submit a pull request

When your feature is working and tested, submit a PR to the guild-toolkit repo. This is where you learn the PR process:

- Your PR description should explain what you built and why
- The CI must pass (tests, clippy, formatting)
- Other guild members will review your code
- You'll get feedback, possibly requests for changes
- You address the feedback and the PR gets merged

This is the first time your code goes through review by people other than your agent. It's the closest thing to the traditional apprentice-submits-work-to-the-master moment.

### 6. Your code ships

When your PR merges, your code is part of the toolkit. Other guild members use it. You built something real that matters to people beyond yourself. That's the transition from exercises to contributions.

## What You Learn Here

Skills this teaches that nothing else in the curriculum does:

**Reading existing code.** The most underrated skill in software. Most of your time as a practitioner will be spent understanding what exists, not writing new things. The workshop forces this by design.

**Working within constraints.** You can't redesign the data model because your tool would be easier with a different structure. You use what's there. This is every job you'll ever have.

**Collaboration.** Other people are working in the same codebase. Your changes can't break their tools. You need to be aware of shared state, shared dependencies, shared conventions.

**The PR process.** Design, implement, submit, get reviewed, address feedback, merge. This is how professional open source and team development works. Your portfolio projects didn't have this step.

**Building for others.** Your portfolio projects were for you. These tools are for the guild. Error messages need to be clear for someone who isn't you. Documentation needs to exist. Edge cases matter because real people will hit them.

## Exercises

1. Clone the guild-toolkit repo and build the workspace. Explore the structure. Read guild-core's source. Don't change anything yet. Just read. Then write a paragraph describing how the shared data model works and how tools are expected to use it. Share it in the guild channel for feedback on your understanding.

2. Pick a beginner tool and implement its first feature. Follow the full process: claim the work, design before building, build in layers, submit a PR.

3. Review someone else's PR on the toolkit. Read their code, test it locally, and leave specific feedback. This is your first time being the reviewer rather than the reviewed. Be constructive and specific, just like the best roast feedback you've received.

4. After your first PR is merged, find an issue on an intermediate tool. Notice how the process feels different when you already know the codebase.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Tracking Your Work](../02-the-methodology/02-tracking-your-work.md) | **The Workshop** | [Working with APIs →](02-working-with-apis.md) |

# Tracking Your Work

## When Your Head Runs Out of Room

Up until now, the things you've built have been small enough to hold in your head. The bookmark manager has a handful of features. You can remember what's done, what isn't, and what's next without writing it down.

That won't last.

The moment a project gets even moderately complex (say, ten features instead of five, or two people working instead of one), your memory becomes the weakest link. You forget that you still haven't handled the edge case from last week. You lose track of which pieces depend on which. You come back after a weekend and spend twenty minutes figuring out where you left off. And if you're working with an AI agent, the problem is worse, because the agent's memory resets with every new conversation. It has no idea what you did yesterday unless you tell it.

This is the problem that issue trackers solve. And since you just learned how to build things with agents, you're going to build one.

## What Issue Tracking Actually Is

Strip away the jargon and an issue tracker is just a structured to-do list with some important properties:

**Each item is specific and independent.** Not "work on the app" but "add a search bar that filters recipes by name." Each item describes one thing that can be built, tested, and verified on its own.

**Items have states.** At minimum: open (needs to be done), in progress (being worked on), and closed (done). This tells you and anyone else at a glance what the current situation is.

**Items can be organized.** By priority (what matters most), by category (bug vs. feature vs. cleanup), by grouping (these five items are all part of the authentication system). Organization lets you answer questions like "what's the most important thing I haven't started yet?"

**Items create a record.** When you close an item, it doesn't vanish. It stays in the history. Three months from now, you can look back and see what you built, in what order, and why. This is your audit trail. For your portfolio, it's evidence that you worked deliberately, not randomly.

**Items survive your memory.** You can close your laptop, go to sleep, and come back tomorrow. The tracker remembers everything. You can start a new conversation with an agent, point it at the tracker, and it instantly knows what's been done and what's left. This is especially critical for AI-assisted work, where conversations end and contexts reset constantly.

## Why Agents Need This Even More Than You Do

Here's something that isn't obvious until you've lived it: when you're directing an AI agent, the issue tracker isn't just for you. It's for the agent too.

Remember from Phase 1: agents have no memory between conversations. Every new conversation starts blank. And even within a single long conversation, context drifts and early details get fuzzy.

An issue tracker gives the agent something to anchor to. Instead of opening a conversation with a paragraph of context about where you left off, you can say "here's my issue list, we're working on issue #7." The agent immediately knows what's done, what's in progress, and what's next. When the conversation gets long and you need to start fresh, the tracker preserves everything that matters.

Think of it as the agent's external memory. The agent does the thinking and building. The tracker does the remembering.

## Build One: Your Second Portfolio Project

You're going to build a simple issue tracker as a command-line tool in Rust. This is portfolio project #2, and it's your first Rust project. The bookmark manager in Phase 1 used HTML and JavaScript. That was a deliberate choice for your very first build: you could see the result in a browser instantly, no compilation, no build steps. It's the one exception. From here on, we work in Rust.

Don't worry about not knowing Rust. The agent knows Rust. Your job is the same as it was for the bookmark manager: describe what you want, verify the output, and iterate. The difference is that instead of opening an HTML file in a browser, you'll run commands like `cargo build` and `cargo run` in your terminal. The agent will tell you when.

Follow the same VDD process from the previous chapter: design doc first, build in layers, verify each layer, and submit for review.

### The Design Doc

Here's a starting point. Refine it with your agent until it matches what you want:

```
# Issue Tracker - Design Document

## Purpose
A personal issue tracker CLI for managing project tasks.
Single user, runs in the terminal.

## Features
1. Create an issue with a title and optional description
2. List all open issues
3. Mark an issue as "in progress" or "done"
4. Set priority on issues (low, medium, high)
5. Add labels to issues (bug, feature, etc.)
6. Filter the list by status, priority, or label
7. List closed issues separately
8. Delete an issue

## Technology
- Rust
- Data stored in a local JSON file in the project directory
- CLI interface using subcommands (like git: `tracker create "title"`, `tracker list`, etc.)

## Interface
- `tracker create "Fix the login bug" --priority high --label bug`
- `tracker list` (shows open issues, sorted by priority)
- `tracker list --status done` (shows closed issues)
- `tracker list --label bug` (filter by label)
- `tracker status <id> in-progress` (change status)
- `tracker status <id> done` (mark complete)
- `tracker show <id>` (show full details)
- `tracker delete <id>` (remove an issue)

## Out of Scope
- Multiple users or sharing
- Due dates or calendar integration
- Subissues or hierarchy (keep it flat for now)
- Time tracking
```

### Build Layers

Here's one way to layer the build:

1. **Core:** `cargo new tracker` to set up the project. Create issues with a title and list them. Save to a JSON file. Just `tracker create "title"` and `tracker list`.
2. **Status flow:** Add status (open → in progress → done). `tracker status <id> done` to change it. `tracker list` only shows open by default.
3. **Priority:** Add priority levels. Sort the list by priority. Show priority in the output with color or markers.
4. **Labels:** Add labels to issues. Display them in the list. Filter with `tracker list --label bug`.
5. **Compound filtering:** Make status, priority, and label filters work together. `tracker list --status open --priority high --label bug` shows high-priority open bugs.
6. **Detail and delete:** `tracker show <id>` shows full details including description and timestamps. `tracker delete <id>` with confirmation.
7. **Polish:** Helpful error messages, colored output, a `--help` flag that explains every command, empty-state messages ("No open issues. Nice work!").

Verify each layer before moving to the next. `cargo build` should compile without errors at every step. Use the adversarial thinking you learned: what happens if you create an issue with no title? What if you pass an ID that doesn't exist? What if the JSON file gets corrupted?

**Security habit check:** This is your first project that reads and writes files. Tell your agent: "Validate all input from the command line. Reject empty titles. Handle the case where the JSON file is missing or contains invalid data without crashing." Data that comes from outside your program (user input, files on disk) should never be blindly trusted. This applies to every project you'll build from here on. We'll go deeper in the Security chapter, but the principle is simple: check before you use.

### What You'll Learn Building This

This project teaches you several things the bookmark manager didn't:

**Working in Rust.** This is your first compiled project. You'll get used to the cycle of writing code, compiling, and fixing compiler errors. Rust's compiler is famously strict, and that's a feature: when it does compile, you know entire categories of bugs are impossible. The agent will handle the syntax, but you'll start to recognize what the compiler is telling you.

**CLI design.** Building for the terminal is different from building for a browser. There's no visual layout, no buttons, no mouse clicks. Everything is text in, text out. You'll learn to think about user experience in a text-only environment: clear output formatting, helpful error messages, intuitive command structure.

**State machines.** An issue moves through states: open → in progress → done. It can't go backwards (or can it? That's a design decision). This is the simplest version of something that shows up everywhere in software: objects that change state according to rules.

**Compound filtering.** The bookmark manager had search and tag filtering. This has status, priority, *and* label filtering, all at once. Making multiple filters work together without breaking each other is a real problem you'll encounter in every project.

**Structured data and serialization.** Bookmarks were basically a URL and some text. Issues have structured data: a status with specific allowed values, a priority with a defined order, labels as a list, timestamps. And you're saving them to a JSON file, which means the data needs to be serialized (turned into text) and deserialized (turned back into structured data). This is a fundamental concept in all software.

## Now Use a Real One: Chainlink

You've built a tracker. You understand the concepts: issues, states, priorities, labels, filtering. You know why it matters and what it does.

Now here's the tool you'll actually use going forward: **Chainlink**.

Chainlink is a command-line issue tracker built specifically for AI-assisted development. It's designed by the guild, and it solves the exact problems you just learned about, plus several you haven't hit yet.

### Why Not Just Use the One You Built?

Your tracker is a learning project. It's great for understanding the concepts. But it's a web app you open in a browser, and it stores data in that browser's local storage. It can't talk to your agent. It can't inject context into a conversation. It can't survive a browser cache clear.

Chainlink runs in your terminal (where your agent already lives), stores data in a local database file that travels with your project, and is designed from the ground up to bridge the gap between you and your AI agent.

### Installing Chainlink

If you have Rust's package manager installed:
```
cargo install chainlink-tracker
```

Then initialize it in any project:
```
chainlink init
```

That creates a `.chainlink/` folder in your project with a database, configuration, and a set of hooks. All your issues live there, local to the project, no cloud services, no accounts.

If you don't have Rust installed yet, your agent can walk you through it. Or come back to this after you've done more projects. The concepts matter more than the specific tool right now.

### The Key Insight: The Agent Does the Tracking

Here's what makes Chainlink different from a normal issue tracker: **you don't have to run the commands yourself.** When you run `chainlink init`, it sets up hooks that teach your AI agent how to use Chainlink. The agent reads the hooks, understands the system, and starts managing issues on its own.

You tell the agent "I want to add a search feature." The agent:
1. Creates an issue in Chainlink for the work
2. Starts a session and marks that issue as active
3. Breaks it into subissues if it's complex
4. Adds comments as it works, documenting decisions and findings
5. Closes the issue when it's done
6. Leaves handoff notes for the next session

You don't type `chainlink create` or `chainlink close`. The agent does. Your job is the same as it's always been: direct the work, verify the output, and make judgment calls. Chainlink just gives the agent a structured place to track everything it's doing, so nothing gets lost between conversations.

This is what it looks like in practice. You start a conversation with your agent and say "let's add search to the recipe app." Behind the scenes, the agent is doing this:

```
chainlink session start
chainlink quick "Add search feature to recipe app" -p medium -l feature
# ... builds the feature ...
chainlink comment 3 "Search filters by title and ingredient, real-time as user types"
chainlink close 3
chainlink session end --notes "Search is done. Tag filtering is next."
```

You see the work happening. You test the result. You give feedback. The tracking is handled for you.

### The Concepts You Already Know

Everything you learned building your tracker maps directly to what Chainlink is doing under the hood:

| Your Tracker | What the Agent Does in Chainlink |
|---|---|
| Create issue button | Creates an issue before starting any work |
| Status badges | Moves issues through open → in progress → closed |
| Priority levels | Sets priority based on what you asked for |
| Label tags | Labels work as bug, feature, etc. |
| Filter controls | Uses filters to check what's open, what's blocked |
| Closed issues section | Closes issues and logs what was delivered |

Because you built a tracker, you understand what the agent is doing. It's not magic. It's the same concepts, automated.

### What Chainlink Adds

Here's where it goes beyond what you built:

**Sessions and handoff notes.** When the agent starts working, it opens a session. When the conversation ends, it saves handoff notes describing where things stand. Next time you start a conversation (even days later), the agent reads those notes and picks up where it left off. No more re-explaining your entire project every time.

**Breadcrumbs.** During a long conversation, the agent drops breadcrumbs as it works:

```
chainlink session action "Found the bug - it's in the token refresh logic"
```

If the conversation gets long and the agent's context compresses (older messages get fuzzy), the breadcrumbs survive. They're in the tracker, not in the conversation. This is how you fight the entropy problem from the previous chapter.

**Subissues.** Remember the bead-string from VDD? Chainlink supports it directly. When the agent encounters a big task, it breaks it down:

```
chainlink create "Add user authentication" -p high
chainlink subissue 1 "Create login form"
chainlink subissue 1 "Add password hashing"
chainlink subissue 1 "Build session management"
```

Issue #1 is the epic. The subissues are the beads. You can see the whole hierarchy with `chainlink tree`.

**Dependencies.** Sometimes one issue blocks another. The agent tracks this:

```
chainlink block 5 3
```

Issue #5 is blocked by issue #3. `chainlink ready` shows only the issues with no blockers, so the agent (and you) always know what can be worked on right now.

**Smart suggestions.** The agent can ask Chainlink what to do next:

```
chainlink next
```

Chainlink looks at priorities, dependencies, and progress, and recommends the next thing to pick up.

### What You Actually Do

Your daily workflow with Chainlink is simple because most of it is automatic:

1. **Start a conversation with your agent.** The agent reads the Chainlink state and knows where things stand.
2. **Tell it what you want to work on.** "Let's tackle the filtering next" or "there's a bug where search doesn't clear properly."
3. **Review the output.** The agent builds, you verify. Same as always.
4. **Check the tracker when you want the big picture.** `chainlink list` shows all open issues. `chainlink tree` shows the hierarchy. These are read-only commands you can run yourself anytime to see the state of the project.

The agent handles the bookkeeping. You handle the direction and quality control. That's the division of labor.

## The Bigger Picture

Issue tracking might feel like overhead when your projects are small. "I know what I need to do, why do I need to write it down?" You write it down because:

1. **You won't always remember.** Not tomorrow, not next week, definitely not next month.
2. **Your agent never remembers.** Every new conversation starts blank unless you give it context, and a tracker is the most efficient context you can give.
3. **Your reviewers need to see it.** Part of the adversarial review process is examining not just what you built but how you organized the work. A clean issue history shows discipline.
4. **It forces clear thinking.** If you can't write a clear issue title, you haven't thought clearly about what you're building. The act of creating issues *is* the act of decomposition from the previous chapters.

This is the tracking layer of VDD. The beads on the string. Every piece of work has a record, every record has a status, and nothing falls through the cracks because it was never written down.

## Exercises

1. Build the issue tracker from the design doc above using the VDD process. Design doc → layers → verify each layer → polish. This is portfolio project #2.

2. Once your tracker is built, use it to track the remaining work on itself. Create issues for any features you skipped or bugs you found during testing. This is delightfully meta, and it proves the tool works.

3. Install Chainlink in one of your existing projects. Then ask your agent to make an improvement to the project. Watch how the agent creates issues, tracks its work, and leaves handoff notes without you having to manage any of it. Run `chainlink list` and `chainlink tree` to see what the agent built up.

4. Start a new conversation with your agent in a Chainlink-enabled project. Don't give it any context. Just say "check where we left off and let's keep going." See how quickly it picks up the thread from the handoff notes and issue list. Compare this to the old approach of typing a paragraph of context every time.

5. Submit your issue tracker for adversarial review. The roast for this one will be interesting, because your reviewers are people who *use* issue trackers every day. They'll have opinions.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← How We Build](01-how-we-build.md) | **Tracking Your Work** | [The Workshop →](../03-real-world-skills/01-the-workshop.md) |

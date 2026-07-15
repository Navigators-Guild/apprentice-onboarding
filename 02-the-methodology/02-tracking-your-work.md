# Tracking Your Work

## When Your Head Runs Out of Room

Up until now, the things you've built have been small enough to hold in your head. The bookmark manager has a handful of features. You can remember what's done, what isn't, and what's next without writing it down.

That won't last.

As a project grows, unaided memory becomes unreliable. You forget the edge case from last week or which pieces depend on which. Agent products may preserve history, project instructions, or summaries, but those features vary and can omit important details. Durable project state should live in files and trackers you can inspect, not only in a conversation.

This is the problem that issue trackers solve. And since you just learned how to build things with agents, you're going to build one.

## What Issue Tracking Actually Is

Strip away the jargon and an issue tracker is just a structured to-do list with some important properties:

**Each item is specific and independent.** Not "work on the app" but "add a search bar that filters recipes by name." Each item describes one thing that can be built, tested, and verified on its own.

**Items have states.** At minimum: open (needs to be done), in progress (being worked on), and closed (done). This tells you and anyone else at a glance what the current situation is.

**Items can be organized.** By priority (what matters most), by category (bug vs. feature vs. cleanup), by grouping (these five items are all part of the authentication system). Organization lets you answer questions like "what's the most important thing I haven't started yet?"

**Items create a record.** When you close an item, it doesn't vanish. It stays in the history. Three months from now, you can look back and see what you built, in what order, and why. This is your audit trail. For your portfolio, it's evidence that you worked deliberately, not randomly.

**Items survive a session.** You can close your laptop and return tomorrow. A new agent session can inspect the tracker to reconstruct what is done and what remains. It still needs to read the entries correctly, so treat the tracker as evidence, not automatic understanding.

## Why Agents Need This Even More Than You Do

Here's something that isn't obvious until you've lived it: when you're directing an AI agent, the issue tracker isn't just for you. It's for the agent too.

Do not assume an agent has complete, reliable memory between sessions. Some tools preserve history or project state; others start fresh, summarize, or retrieve only selected material. Long sessions can also lose precision as tools compact or select context.

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

**Working in Rust.** This is your first compiled project. You'll get used to writing code, compiling, and fixing compiler errors. A successful safe-Rust compile rules out useful categories of type and memory-safety violations; it does not rule out logic errors. The agent can help with syntax, while you learn to read the evidence the compiler provides.

**CLI design.** Building for the terminal is different from building for a browser. There's no visual layout, no buttons, no mouse clicks. Everything is text in, text out. You'll learn to think about user experience in a text-only environment: clear output formatting, helpful error messages, intuitive command structure.

**State machines.** An issue moves through states: open → in progress → done. It can't go backwards (or can it? That's a design decision). This is the simplest version of something that shows up everywhere in software: objects that change state according to rules.

**Compound filtering.** The bookmark manager had search and tag filtering. This has status, priority, *and* label filtering, all at once. Making multiple filters work together without breaking each other is a real problem you'll encounter in every project.

**Structured data and serialization.** Bookmarks were basically a URL and some text. Issues have structured data: a status with specific allowed values, a priority with a defined order, labels as a list, timestamps. And you're saving them to a JSON file, which means the data needs to be serialized (turned into text) and deserialized (turned back into structured data). This is a fundamental concept in all software.

## Now Use a Real One: crosslink

You've built a tracker. You understand the concepts: issues, states, priorities, labels, filtering. You know why it matters and what it does.

Now here's the tool you'll actually use going forward: **crosslink**.

crosslink is a command-line issue tracker built specifically for AI-assisted development. It solves the exact problems you just learned about, plus several you haven't hit yet.

### Why Not Just Use the One You Built?

Your tracker is a local Rust CLI that stores issues in JSON. That is enough to teach commands, states, filtering, and serialization. Its deliberate limits are different: the design is flat, with no sessions, handoff notes, breadcrumbs, subissues, dependency graph, hooks, or coordination features. Adding those safely would require new schemas, migrations, concurrency decisions, and integrations.

crosslink is an evolving, local-first CLI built for those broader workflows. The current beta stores project issues in SQLite at `.crosslink/issues.db` and adds sessions, hierarchy, dependencies, recommendations, hooks, and optional multi-agent workflows. Check the [official quickstart](https://forecast-bio.github.io/crosslink/getting-started/quickstart.html) because commands and setup can change while the project is in beta.

### Installing crosslink

The current release requires Rust 1.87 or newer. Confirm `rustc --version`, update stable Rust if needed, then install:

```
rustup update stable
cargo install --locked crosslink
```

Then initialize it in any project:

```
cd ~/guild-projects/guild-portfolio/bookmark-manager
crosslink init
```

Follow the interactive prompts. Initialization creates local project state under `.crosslink/`; the issue database is `.crosslink/issues.db`. Review the generated configuration and hook choices before accepting them, especially in a repository you did not create.

Verify it worked by running `crosslink --version`. You should see a version number. If you see "command not found" instead, close and reopen your terminal — `cargo install` drops binaries in `~/.cargo/bin/` and your shell needs to reload to find them.

### The Key Insight: The Agent Does the Tracking

Here's what makes crosslink useful for agent-assisted work: **a configured coding agent can run the commands as part of its workflow.** Initialization and client integration do not guarantee that every agent will discover or use it correctly. Tell the agent to read the project instructions, inspect `crosslink --help`, and show you the tracker changes it makes.

In a workflow where the client instructions and hooks are configured and the agent follows them, you can ask for a search feature and expect it to propose actions such as:

1. Creates an issue in crosslink for the work
2. Starts a session and marks that issue as active
3. Breaks it into subissues if it's complex
4. Adds comments as it works, documenting decisions and findings
5. Closes the issue when it's done
6. Leaves handoff notes for the next session

The agent can do the bookkeeping, but you may run the same commands manually. Your job remains direction and quality control: review issue scope, verify status transitions, and confirm that handoff notes match the repository.

This is what the intended workflow looks like. Ask the agent to show or summarize the commands rather than assuming they happened:

```
crosslink session start
crosslink quick "Add search feature to recipe app" -p medium -l feature
# ... builds the feature ...
crosslink issue comment 3 "Search filters by title and ingredient, real-time as user types"
crosslink close 3
crosslink session end --notes "Search is done. Tag filtering is next."
```

You inspect both the repository and tracker changes, test the result, and give feedback. If the integration does not update the tracker, run the commands yourself or repair the project instructions.

### The Concepts You Already Know

Everything you learned building your tracker maps directly to what crosslink is doing under the hood:

| Your Tracker | What the Agent Does in crosslink |
|---|---|
| Create issue button | Creates an issue before starting any work |
| Status badges | Moves issues through open → in progress → closed |
| Priority levels | Sets priority based on what you asked for |
| Label tags | Labels work as bug, feature, etc. |
| Filter controls | Uses filters to check what's open, what's blocked |
| Closed issues section | Closes issues and logs what was delivered |

Because you built a tracker, you understand what the agent is doing. It's not magic. It's the same concepts, automated.

### What crosslink Adds

Here's where it goes beyond what you built:

**Sessions and handoff notes.** A configured workflow can open a session, record the active issue, and save handoff notes when work ends. A later agent can read those durable notes. Verify that the session ended and the notes are accurate; product context, hooks, and agent compliance still vary.

**Breadcrumbs.** During a long conversation, the agent drops breadcrumbs as it works:

```
crosslink session action "Found the bug - it's in the token refresh logic"
```

If the conversation gets long and the agent's context compresses (older messages get fuzzy), the breadcrumbs survive. They're in the tracker, not in the conversation. This is how you fight the entropy problem from the previous chapter.

**Subissues.** Remember the bead-string from VDD? crosslink supports it directly. When the agent encounters a big task, it breaks it down:

```
crosslink create "Add user authentication" -p high
crosslink subissue 1 "Create login form"
crosslink subissue 1 "Add password hashing"
crosslink subissue 1 "Build session management"
```

Issue #1 is the epic. The subissues are the beads. You can see the whole hierarchy with `crosslink issue tree`.

**Dependencies.** Sometimes one issue blocks another. The agent tracks this:

```
crosslink issue block 5 3
```

Issue #5 is blocked by issue #3. `crosslink issue ready` reports open issues whose recorded blockers are resolved, so it is only as accurate as the dependency and status data you maintain.

**Smart suggestions.** The agent can ask crosslink what to do next:

```
crosslink issue next
```

crosslink looks at priorities, dependencies, and progress, and recommends the next thing to pick up.

### What You Actually Do

Your daily workflow with crosslink can be short when the client integration is working:

1. **Start a conversation with your agent.** Ask it to read the project instructions, last handoff, and open issues; confirm what it found.
2. **Tell it what you want to work on.** "Let's tackle the filtering next" or "there's a bug where search doesn't clear properly."
3. **Review the output.** The agent builds, you verify. Same as always.
4. **Check the tracker when you want the big picture.** `crosslink list` shows all open issues. `crosslink issue tree` shows the hierarchy. These are read-only commands you can run yourself anytime to see the state of the project.

Let the configured agent propose bookkeeping changes, then inspect the tracker just as you inspect code. You retain direction and quality control.

## The Bigger Picture

Issue tracking might feel like overhead when your projects are small. "I know what I need to do, why do I need to write it down?" You write it down because:

1. **Human memory is fallible.** A durable record becomes more valuable after interruptions or handoffs.
2. **Agent memory is not a reliable system of record.** Product memory and history vary; a tracker is inspectable, versionable context you control.
3. **Your reviewers need to see it.** Part of the adversarial review process is examining not just what you built but how you organized the work. A clean issue history shows discipline.
4. **It encourages clear thinking.** Difficulty writing a clear issue title can reveal an underspecified task. Creating issues is one practical form of the decomposition from the previous chapters.

This is the tracking layer of VDD: the beads on the string. Record work at a useful level so status, decisions, and handoffs remain inspectable. A tracker reduces dropped work; it does not eliminate it.

## Exercises

1. Build the issue tracker from the design doc above using the VDD process. Design doc → layers → verify each layer → polish. This is portfolio project #2.

2. Once your tracker is built, use it to track the remaining work on itself. Create issues for any features you skipped or bugs you found during testing. This exercises the tool in a realistic workflow and may expose gaps that isolated tests missed.

3. Install crosslink in one of your existing projects. Ask your agent to make an improvement and to use the tracker. Run `crosslink list`, `crosslink issue tree`, and `crosslink session status` yourself. Compare the requested workflow with the records it actually created.

4. Start a new conversation with your agent in a crosslink-enabled project. Say "read the project instructions, last handoff, and open issues; summarize the state before changing anything." Check the summary against the repository and tracker, then compare this handoff with manually restating context.

5. Submit your issue tracker to the guild [Discord](https://discord.gg/kfM6Q4UBbM) **#adversarial-review** channel. The roast for this one will be interesting, because your reviewers are people who *use* issue trackers every day. They'll have opinions.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← How We Build](01-how-we-build.md) | **Tracking Your Work** | [Branches and Pull Requests →](03-branches-and-pull-requests.md) |

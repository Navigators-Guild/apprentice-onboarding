# Project Architecture

## When One File Isn't Enough

Your bookmark manager was one file. Your issue tracker was probably a few files. For small tools, that's fine. But at some point every project crosses a threshold where a single file (or a handful of disorganized files) starts working against you. The code gets hard to navigate, hard to test, and hard to change without breaking something else.

This chapter is about recognizing that threshold and knowing how to structure a project so it stays manageable as it grows. More importantly, it's about directing your agent to do this well, because agents have a specific bad habit that you need to know about.

## The God File Problem

Left to its own devices, an agent will put everything in one file. Or two files. Or it'll make a second file only when the first one hits some truly absurd length. This is called a **god file**: one file that knows everything, does everything, and touches everything.

This happens because agents optimize for the simplest way to fulfill your request. "Add a feature" is easiest when all the code is in one place. No imports to manage, no module boundaries to think about, no decisions about where something belongs. Just add it to the bottom of main.rs and it works.

It works until it doesn't. Here's what goes wrong:

**The agent loses track.** Remember context windows from Phase 1? When a file is 2,000 lines long, the agent can't hold all of it in mind at once. It makes changes in one function that break assumptions in another function 1,500 lines away. You start getting bugs that come from the agent not being able to see the whole picture.

**You lose track.** Even if you're not reading code line by line, navigating a god file to find the part that's relevant to your current task gets painful fast. "The bug is somewhere in this 3,000-line file" is a much worse starting point than "the bug is in the database module."

**Testing gets hard.** When everything is tangled together, you can't test one thing without dragging in everything else. You want to test that your search function works correctly, but it's interleaved with display code, config loading, and file I/O. Isolating it means untangling it, and untangling it means restructuring.

**Changes ripple.** In a god file, there are no boundaries. Changing how you store data might accidentally break how you display it, because they share variables and assumptions with no separation. In a well-structured project, the storage module and the display module have a clear interface between them. You can change the internals of one without the other even noticing.

## The Fix: Separation of Concerns

The core principle is simple: **each piece of your project should do one thing and do it well.** Group code by what it's responsible for, not by when you wrote it.

For most projects, the natural boundaries look something like this:

**Data.** How you define and store your information. The structs, the serialization, the database or file I/O. This is the "what" of your project.

**Logic.** The rules and operations. Filtering, sorting, calculating, validating, transforming. This is the "how."

**Interface.** How the user interacts with the program. Argument parsing, output formatting, error display. This is the "who sees what."

**Configuration.** Settings, environment variables, defaults. This is the "knobs and dials."

In Rust, these become modules. A typical CLI tool might look like:

```
src/
├── main.rs          # entry point: parse args, call into logic, handle errors
├── cli.rs           # argument definitions (clap structs)
├── config.rs        # configuration loading
├── models.rs        # data structures
├── storage.rs       # reading/writing data to disk or database
├── commands/        # one file per subcommand
│   ├── mod.rs
│   ├── create.rs
│   ├── list.rs
│   └── delete.rs
└── output.rs        # display formatting, colors, tables
```

Each file has a clear job. `main.rs` is short. It parses arguments, calls the right command, and handles top-level errors. It doesn't contain business logic. `storage.rs` knows how to read and write data but doesn't know how to display it. `output.rs` knows how to display things but doesn't know where the data comes from. They talk to each other through the types defined in `models.rs`.

You don't need to memorize this layout. Your agent knows Rust module conventions. What you need is to *direct* it toward this kind of structure from the start.

## Refactoring: From God File to Modules

Here's what a real refactoring looks like. Say your issue tracker ended up with a `main.rs` that's 400 lines: argument parsing, data types, file I/O, display formatting, and business logic all tangled together.

You tell your agent:

> "main.rs has grown too large. Refactor it into modules. Here's how I want it split:
> - `models.rs`: the Issue struct and Priority enum
> - `storage.rs`: everything that reads or writes the JSON file
> - `output.rs`: everything that formats output for the terminal
> - `cli.rs`: the clap argument definitions
> - `commands/create.rs`, `commands/list.rs`, `commands/close.rs`: one file per subcommand
> - `main.rs`: just the entry point, under 30 lines. Parse args, call the right command, handle errors.
>
> Move the code, don't rewrite it. Everything should work exactly the same after the split."

The agent will extract the code into the right files, add the `mod` declarations, update the `use` statements, and make sure everything still compiles. You run `cargo build` to verify, then test that every command still works.

What changed? The *behavior* is identical. The *structure* is transformed. Now when you need to change how storage works, you open `storage.rs`. When you need to add a new command, you add a file in `commands/`. When the adversary roasts your output formatting, you know exactly which file to look at.

The best time to refactor is before the god file gets painful. The second best time is now.

## DRY: Don't Repeat Yourself

The other principle that keeps projects healthy: **if you're writing the same thing in two places, pull it out into one place and use it from both.**

DRY stands for Don't Repeat Yourself. Agents violate this constantly unless you watch for it. You ask for a "create" command and a "update" command, and the agent writes the same validation logic in both. You add error handling to one function, and the agent writes nearly identical error handling in three others instead of extracting a shared helper.

Duplication isn't just ugly. It's a maintenance trap. When you need to change the validation rule, you have to find and update every copy. Miss one and you have a bug that only shows up in certain code paths.

When you notice duplication (or when you suspect the agent might be duplicating), say so:

> "I see similar validation logic in both the create and update commands. Extract that into a shared function in a validation module and use it from both places."

Or preempt it:

> "Before implementing the update command, check what we already have in the create command. If any logic is shared (validation, storage writes, output formatting), extract it into a shared module first, then have both commands use it."

## How to Direct Your Agent

This is the practical part. You already know how to write good prompts. Here's how to apply that skill to architecture specifically.

### At Project Start: Set the Structure

Don't let the agent decide the structure organically by cramming things into main.rs until it bursts. Set it up front:

> "Create a new Rust project. I want a modular structure from the start. Separate files for: CLI argument parsing, data models, storage/persistence, business logic, and output formatting. main.rs should just be the entry point that wires everything together. Keep it under 50 lines."

The agent will scaffold the module structure before writing any features. This is vastly better than trying to refactor a god file later.

### When Adding Features: Say Where It Goes

Don't just say "add search." Say where:

> "Add a search command. The argument parsing goes in cli.rs. The search logic goes in a new file commands/search.rs. It should use the types from models.rs and the storage functions from storage.rs. The output formatting should use the helpers in output.rs."

This takes ten seconds more than "add search" and prevents the agent from dumping 200 lines into main.rs.

### When Reviewing: Watch for Growth

After each feature, check the file sizes. If any file is growing past 200-300 lines, it's probably doing too much. Tell the agent:

> "storage.rs is getting long. It handles both file I/O and database operations. Split it into file_storage.rs and db_storage.rs, with a shared trait in storage.rs that both implement."

### When You Smell Duplication: Call It Out

If the agent shows you code that looks familiar, ask:

> "This error handling looks similar to what we have in the create command. Is this duplicated? If so, extract it into a shared function."

The agent will often recognize the duplication and fix it. Sometimes it needs you to point it out. Either way, catching it early is much easier than catching it late.

## When Not to Split

There's a flip side. Some projects are small enough that multiple files add complexity without benefit. If your tool is 150 lines and does one thing, a single `main.rs` is fine. Don't create eight modules for a script.

The rule of thumb: if you can read the entire file and understand what it does without scrolling more than a few times, it's probably fine as one file. The moment you find yourself scrolling around trying to find "the part that handles X," it's time to split.

Also, don't split things that are genuinely cohesive. If two functions always change together and always need each other, putting them in separate files just means you're editing two files instead of one every time. Separation of concerns means separating things that have *different* concerns, not arbitrarily scattering code across files.

## Rust Module Basics

You don't need to understand the Rust module system in depth. The agent handles the syntax (`mod`, `use`, `pub`). But it helps to know the vocabulary so you can have a conversation about it:

**A module** is a unit of organization. In Rust, each file is a module. `storage.rs` is the `storage` module.

**`pub`** means public. If a function or struct is `pub`, other modules can use it. If it's not, it's private to its module. This is how you control boundaries: the storage module exposes a few public functions (`save`, `load`, `delete`) but keeps its internal implementation private.

**A crate** is a package. Your whole project is a crate. The guild-toolkit has multiple crates in a workspace. When you `cargo build`, you're building a crate.

**`use`** is how one module references another. `use crate::models::Issue;` means "I want to use the `Issue` type from the `models` module." The agent writes all of this. You just need to know the words so you can say things like "make that function public so the commands module can use it."

## The Architecture Conversation

The most advanced version of this skill is having an architecture conversation with your agent before writing any code:

> "I'm going to build a tool that does X. Before we write any code, help me plan the module structure. What are the natural boundaries? What types do we need? What does the dependency flow look like (which modules depend on which)? I want to keep things modular so each piece can be tested independently."

The agent will propose a structure. Review it critically:

- Does every module have a clear, single responsibility?
- Are the dependencies one-directional? (Models shouldn't depend on storage. Storage depends on models.)
- Is there a clean separation between interface and logic?
- Could you swap out the storage layer without changing the logic?

If the answer to any of these is no, push back before a single line of code exists. Architecture decisions are cheap to change in a design doc and expensive to change in a working codebase.

## Exercises

1. Look back at your issue tracker from Phase 2. Is it a god file? If most of the logic lives in one or two files, refactor it. Tell your agent to split it into modules: models, storage, commands, output. Verify that it still works after the refactoring. This is the most common real-world task: not building something new, but improving the structure of something that works.

2. Clone a tool from the guild-toolkit and read its structure. How is it organized? Does each file have a clear purpose? Write a paragraph describing the architecture. Share it in the guild channel.

3. Start a new project (anything you want) and begin with the architecture conversation. Before any code exists, have the agent help you plan the module structure. Save the plan as a section in your design doc. Then build, following the plan. Notice how much smoother the build process is when the structure is decided upfront.

4. Deliberately ask your agent to add three features to a project without giving any architectural direction. Just say "add X," "add Y," "add Z." Then look at what happened. Where did the code end up? Is there duplication? Is anything hard to find? Now refactor with explicit architectural direction. Compare the two experiences.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Working with APIs](02-working-with-apis.md) | **Project Architecture** | [Security →](04-security.md) |

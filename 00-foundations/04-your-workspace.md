# Your Workspace

## Setting Up Without Overthinking It

You need three things on your computer to start building with agents. That's it. Not twelve tools, not a complex development environment, not a specific operating system. Three things.

This guide walks you through setting up each one. If you already have any of these installed, skip ahead.

## Tool 1: A Text Editor (VS Code)

You need a place to view and occasionally edit the files your agent creates. The standard choice is **Visual Studio Code** (VS Code). It's free, it works on Windows, Mac, and Linux, and it's what most of the guild uses.

**To install it:**

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download the version for your operating system
3. Run the installer with the default settings

That's it. You don't need to learn VS Code deeply right now. You need to be able to open files, look at them, and see the file/folder structure of your projects on the left side panel. Everything else you'll pick up as you use it.

**One thing to do after installing:** Open VS Code and look at the left sidebar. There's an icon that looks like two overlapping squares. That's the Extensions panel. Search for and install these two extensions:

- **Markdown Preview Enhanced** - lets you read `.md` files (like this one) with nice formatting
- **Prettier** - automatically makes code files look tidy

These are optional but they make life easier. Don't go down the rabbit hole of installing fifty extensions. Two is enough.

## Tool 2: The Terminal

The terminal (also called the command line, command prompt, or shell) is how you talk to your computer using text instead of clicking around. This sounds intimidating, but you only need a handful of commands, and you'll use them the same way every time.

**You already have a terminal.** You don't need to install one.

- **On Mac:** Open the app called "Terminal" (search for it with Spotlight by pressing Cmd+Space and typing "terminal")
- **On Windows:** Open "PowerShell" (search for it in the Start menu). Or install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store for a nicer experience
- **On Linux:** You already know where your terminal is

**The commands you need to know:**

There are really only six commands you'll use regularly:

`pwd` - **Print Working Directory.** Tells you where you currently are in your computer's file system. Think of it as "where am I right now?" Run this whenever you're not sure where you are.

`ls` - **List.** Shows you all the files and folders in your current location. (On Windows PowerShell, `ls` also works, or you can use `dir`.)

`cd` - **Change Directory.** Moves you into a different folder. `cd Documents` moves you into the Documents folder. `cd ..` moves you back up one level. `cd ~` takes you back to your home folder no matter where you are. (The `~` symbol is shorthand for your home directory. On Mac and Linux that's something like `/home/yourname`. On Windows it's `C:\Users\yourname`. You'll see `~` used throughout this curriculum as a shortcut.)

`mkdir` - **Make Directory.** Creates a new folder. `mkdir my-project` creates a folder called `my-project`.

`cp` - **Copy.** Copies a file from one place to another. `cp file.txt backup.txt` makes a copy of `file.txt` named `backup.txt`.

`clear` - **Clear.** Wipes the terminal screen when it gets cluttered. Doesn't delete anything, just tidies up the display.

That's the list. Six commands. You don't need `grep`, `sed`, `awk`, `chmod`, or any of the hundreds of other commands that exist. If you ever need something more complex, ask an agent for the exact command to run.

**Practice right now:**

Open your terminal and type these commands, one at a time, pressing Enter after each:

```
pwd
ls
mkdir test-folder
cd test-folder
pwd
ls
cd ..
```

You just checked where you were, looked at what was there, created a folder, moved into it, confirmed you moved, saw it was empty (because you just created it), and moved back out. That's the core loop of navigating your computer from the terminal. Everything else builds on this. (You can delete `test-folder` later. It was just for practice.)

## Tool 3: An AI Agent

This is the tool you'll spend most of your time with. There are several options, and this guild is tool-agnostic. The skills you learn here work across all of them. But you need at least one to start.

**Claude** (by Anthropic) - Available at [claude.ai](https://claude.ai) in your browser, or as **Claude Code** which runs in your terminal. Claude is the primary agent used in this guild's examples. The free tier is enough to get started. Claude Code requires a paid API plan but is more powerful for building software because it can directly create and edit files on your computer.

**Cursor** - A code editor (based on VS Code) with an AI agent built in. Available at [cursor.com](https://cursor.com). Good option if you want the agent and editor in one place. Has a free tier.

**Windsurf** - Another AI-powered editor, similar to Cursor. Available at [codeium.com/windsurf](https://codeium.com/windsurf).

**ChatGPT** - Available at [chat.openai.com](https://chat.openai.com). Widely available, good for conversational work, but less integrated with your file system than the other options.

**Our recommendation for starting out:** Begin with Claude at claude.ai. It's free, it's in your browser, and the examples in these guides are written with Claude in mind. As you progress and start building more complex things, you'll likely move to Claude Code or Cursor, but you don't need them yet.

## Tool 4: The Rust Toolchain

The guild's default language is Rust. You don't need to learn Rust (the agent handles the syntax), but you do need it installed so you can compile and run the projects you build.

**To install it:**

Go to [rustup.rs](https://rustup.rs) and follow the instructions. On Mac and Linux, it's one command in your terminal:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

On Windows, download and run the installer from the same site. You may need to install the Visual Studio C++ build tools if prompted. The installer will tell you.

After installation, close and reopen your terminal, then confirm it works:

```
rustc --version
cargo --version
```

You should see version numbers for both. `rustc` is the Rust compiler (it turns code into a program you can run). `cargo` is Rust's build tool and package manager (it handles project setup, dependencies, building, and testing). You'll use `cargo` constantly. The agent will tell you when to run commands like `cargo build` or `cargo test`.

**You don't need to understand Rust yet.** Your first project (the bookmark manager) uses HTML and JavaScript, not Rust. Rust comes in starting with Phase 2. By then you'll be comfortable directing an agent, and the transition will be about the tool, not the workflow.

## Your Folder Structure

Create a consistent place for your guild work. Open your terminal and run:

```
cd ~
mkdir guild-projects
cd guild-projects
mkdir portfolio
mkdir scratch
```

You now have:

- `~/guild-projects/` - Your main workspace
- `~/guild-projects/portfolio/` - Where your portfolio projects will live (the ones you submit for review)
- `~/guild-projects/scratch/` - Where you experiment and practice without pressure

This structure isn't mandatory, but having a consistent place to work prevents the chaos of files scattered across your Desktop, Downloads, and random folders.

## Verifying Your Setup

Let's make sure everything works. Do each of these:

1. **Open VS Code.** If it opens without errors, you're good.
2. **Open your terminal.** Type `pwd` and press Enter. You should see a path on your screen. You're good.
3. **Check Rust.** Type `cargo --version`. You should see a version number. You're good.
4. **Navigate to your workspace.** Type `cd ~/guild-projects` and then `ls`. You should see `portfolio` and `scratch` listed. You're good.
5. **Open your agent.** Go to claude.ai (or whichever agent you chose) and type "Hello, I'm setting up my workspace for learning agentic AI development. Can you confirm you can help me build software?" You should get a coherent, helpful response. You're good.

If any of these steps didn't work, ask your agent to help you troubleshoot. Describe exactly what happened: what you typed, what you expected, and what you got instead. This is your first practice at communicating with an agent. Be specific about the problem.

## What You Don't Need

A quick list of things that might seem like prerequisites but aren't:

- **A powerful computer.** If it runs a web browser, it's enough to start. The agents run on remote servers, not on your machine.
- **A second monitor.** Nice to have, not necessary.
- **Specific operating system.** Mac, Windows, and Linux all work fine.
- **Any paid tools.** Everything in Phase 0 and Phase 1 can be done with free tiers.
- **Prior experience.** If you've read this far, you have enough.

You're set up. Next we'll cover just enough git to track your work, and then you're ready to start talking to agents.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Language Landscape](03-the-language-landscape.md) | **Your Workspace** | [Git: Just Enough →](05-git-just-enough.md) |

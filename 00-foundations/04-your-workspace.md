# Your Workspace

## Setting Up Without Overthinking It

This chapter sets up five essentials: an editor, a terminal, a coding agent, Rust, and Node.js. The next chapter adds Git. You do not need a complex development environment or a specific operating system.

This guide walks you through setting up each one. If you already have any of these installed, skip ahead.

## Tool 1: A Text Editor (VS Code)

You need a place to view and occasionally edit the files your agent creates. The standard choice is **Visual Studio Code** (VS Code). It's free, it works on Windows, Mac, and Linux, and it's what most of the guild uses.

**To install it:**

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download the version for your operating system
3. Run the installer with the default settings

That's it. You don't need to learn VS Code deeply right now. You need to be able to open files, look at them, and see the file/folder structure of your projects on the left side panel. Everything else you'll pick up as you use it.

**One thing to do after installing:** Open VS Code and look at the left sidebar. There's an icon that looks like two overlapping squares. That's the Extensions panel. Search for and install these three extensions:

- **Markdown Preview Enhanced** - lets you read `.md` files (like this one) with nice formatting
- **Prettier** - automatically makes code files look tidy
- **Live Server** (by Ritwick Dey) - runs HTML projects on a local web server with auto-reload when you save. You'll use this starting with Phase 1 to run your first build in the browser.

These make life easier. Don't go down the rabbit hole of installing fifty extensions. Three is enough.

### Creating and Editing Files in VS Code

You'll spend your time in VS Code looking at files your agent created, and occasionally creating or editing files yourself. A handful of operations cover everything you need.

**Open a folder as a workspace.** VS Code is at its best when you open an entire project folder, not just one file. Go to **File → Open Folder...** and pick the folder you want to work in (later in this chapter you'll create `~/guild-projects/` — that's a good one to open). The folder's contents appear in the **Explorer** panel on the left side. Keep the folder open; you switch projects by opening a different folder.

**Create a new file.** In the Explorer panel on the left, right-click in an empty area (or on a folder name) and choose **New File...**. VS Code drops a text field where you type the filename. Type the name including the extension — `notes.md`, `index.html`, `DESIGN.md`. Press Enter. The file opens in the editor, empty, ready for you to type.

**Save a file.** Press **Ctrl+S** on Windows/Linux or **Cmd+S** on Mac. That's it. If the file has unsaved changes, a small white dot appears next to its name in the tab — the dot becomes an × once you save. Get in the habit of hitting save after every few changes.

**Create a dotfile.** Some filenames start with a dot, like `.gitignore` or `.mcp.json`. These are called dotfiles and most operating systems hide them in regular file browsers, but VS Code handles them without fuss. Use the same **New File...** workflow and type the full name including the leading dot: `.gitignore`. VS Code treats it like any other file.

**Open an existing file.** Click it in the Explorer panel. VS Code opens it in a new tab on the right. You can have many tabs open at once; switch between them by clicking the tab names or with **Ctrl+Tab**.

**Rename a file.** Right-click the file in the Explorer panel → **Rename**. Type the new name, press Enter.

**Delete a file.** Right-click the file in the Explorer panel → **Delete**. Confirm. You can also press **Delete** with the file selected.

That's enough VS Code for the entire curriculum. You do not need to learn the command palette, multi-cursor editing, keyboard shortcuts, or any of the hundreds of other features. When you need one, your agent can tell you how.

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

**Claude and Claude Code** (by Anthropic) - [Claude](https://claude.ai) is the browser chat; [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started) is the terminal coding agent. Claude Code can use either an eligible Claude subscription or Anthropic API billing; check [current plan details](https://claude.com/pricing) rather than assuming a particular tier includes it.

**Codex and ChatGPT** (by OpenAI) - [ChatGPT](https://chatgpt.com) is the general interface. [Codex](https://developers.openai.com/codex/) is the coding agent available through dedicated app, CLI, IDE, and cloud workflows. It can work directly in a folder you authorize.

**Cursor** - A code editor with an agent built in, available at [cursor.com](https://cursor.com). Its [current plans](https://cursor.com/pricing) include a limited free option.

**Devin Desktop** (formerly the Windsurf editor) - An IDE and command center for local and cloud coding agents, available at [devin.ai/desktop](https://devin.ai/desktop). Follow the [current setup guide](https://docs.devin.ai/desktop/getting-started). The old Windsurf setup URL now redirects there, but older installations and documentation may still use the Windsurf name.

**Our recommendation for starting out:** Use whichever supported tool you can access, but distinguish chat from a coding agent. Browser chat is enough for explanations and for Phase 1 if you paste or upload the relevant file. For the Rust exercise below and later repository work, use a coding agent that can read and edit only the project folder you authorize. Product features, limits, and prices change; check the linked official pages before choosing.

### Opening the Browser's Developer Tools

Every web browser ships with a built-in developer tools panel, and you'll use it to debug your very first Phase 1 project (a web app). Get comfortable opening it now so it's not a new thing at the moment you need it.

**How to open it:**

- **Chrome, Edge, Brave, and most Chromium browsers:** Press **F12**, or right-click anywhere on the page and choose **Inspect**. Keyboard shortcut: **Ctrl+Shift+I** (Windows/Linux) or **Cmd+Option+I** (Mac).
- **Firefox:** Press **F12**, or right-click → **Inspect**. Same shortcuts work.
- **Safari:** You have to enable developer tools first: **Safari** menu → **Settings** → **Advanced** → check **Show features for web developers**. Then right-click → **Inspect Element**, or press **Cmd+Option+I**.

**What you'll see:** A panel opens attached to the bottom or side of the browser window. It has several tabs across the top: **Elements** (or **Inspector**), **Console**, **Sources** (or **Debugger**), **Network**, and others. For the first few phases of the curriculum, you'll only use the **Console** tab.

**The Console tab** is where your page prints messages and errors. When a web app "doesn't work," the first thing you do is open the console and look at it. You'll see three kinds of messages:

- **Red text or a red ❌ icon** — errors. The page hit a problem and stopped doing whatever it was trying to do. The error message tells you roughly what went wrong and which file/line it happened on.
- **Yellow text or a ⚠️ icon** — warnings. Not fatal, but something the browser wants to flag. Usually ignorable for beginner projects.
- **Gray or black text** — informational messages the code printed on purpose (like a `console.log()` call).

**The debugging loop:** When your first build chapter tells you the page is blank or broken, the workflow is:

1. Open the browser.
2. Open devtools (**F12**).
3. Click the **Console** tab.
4. Look for red text.
5. Copy the full red message.
6. Paste it to your agent along with the code and ask for a fix.
7. Apply the fix, save the file, **reload the page** (**F5** or **Ctrl+R** / **Cmd+R**) — devtools do not auto-refresh when you edit source files.
8. Check the console again. Is the red gone? Are there new errors? Repeat.

**One habit to build:** Clear the console between attempts. There's a small 🚫 icon at the top-left of the Console panel that wipes the display. This makes it obvious which messages are from the latest reload versus stale from a previous attempt.

You'll come back to devtools many times throughout the curriculum. The Console tab alone handles 90% of your web debugging. The other tabs exist for later.

## Tool 4: The Rust Toolchain

The guild's default language is Rust. You do not need to memorize Rust syntax before beginning, but you do need the toolchain installed so you can compile and run the projects you build. The agent can help write syntax; you still need to read diffs, understand behavior, and interpret compiler and test output.

**To install it:**

Go to [rustup.rs](https://rustup.rs) and follow the instructions. The exact path depends on your OS.

**On Mac and Linux**, it's one command in your terminal:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

When the installer asks which option you want, press **1** for the default installation. Wait for it to finish (a minute or two), then close and reopen your terminal so your shell picks up the new PATH entry.

**On Windows**, there's an extra prerequisite: Rust needs the **Microsoft Visual C++ Build Tools** to actually produce executables, and they don't come with Windows by default. The steps:

1. Download **rustup-init.exe** from [rustup.rs](https://rustup.rs) and double-click it.
2. The installer opens in a terminal window and checks whether the MSVC build tools are present. If they are, skip to step 6.
3. If they're missing, the installer shows a message pointing you to the Visual Studio download page. Install **Visual Studio Installer** from that link.
4. When the Visual Studio Installer opens, check the **Desktop development with C++** workload in the left pane. (Just that one — you don't need any other workloads for Rust.) This is a large download. Click **Install**.
5. Once the C++ build tools are installed, return to the rustup-init window (or re-run rustup-init.exe if you closed it).
6. Press **1** for the default installation.
7. Wait for rustup to finish downloading and installing (another minute or two).
8. **Close and reopen your terminal.** This is critical — the PATH update doesn't take effect until you start a fresh terminal session.

**Alternative for Windows users: WSL2.** If you'd rather use the Linux install path on Windows, install **Windows Subsystem for Linux** (run `wsl --install` in PowerShell as Administrator), pick a Linux distribution (Ubuntu is fine), and do all your guild work inside WSL. This gives you a real Linux terminal, the `curl | sh` install works, and you avoid the MSVC build tools entirely. This is a valid choice for anyone who wants the Linux experience on Windows hardware.

**After installation (all platforms),** confirm it works:

```
rustc --version
cargo --version
```

You should see version numbers for both. `rustc` is the Rust compiler (it turns code into a program you can run). `cargo` is Rust's build tool and package manager (it handles project setup, dependencies, building, and testing). You'll use `cargo` constantly. The agent will tell you when to run commands like `cargo build` or `cargo test`.

**Common Windows error:** If you see `error: linker 'link.exe' not found` the first time you try to build something, it means the MSVC build tools aren't installed or aren't complete. Go back and install the **Desktop development with C++** workload in the Visual Studio Installer. After the install finishes, close and reopen your terminal and try the build again.

### Installing Rust Tools Later

Throughout the curriculum you'll occasionally install extra Rust command-line tools with `cargo install <tool-name>` — the crosslink issue tracker in Phase 2, security scanners like `cargo-audit` and `cargo-deny` in Phase 3. A few things to know so those installs don't confuse you:

- **Where the binary goes.** `cargo install` drops the new binary into `~/.cargo/bin/` (Mac/Linux) or `%USERPROFILE%\.cargo\bin\` (Windows). Rustup adds that folder to your PATH automatically during the initial install, so the new command is available everywhere — but only in shells you open **after** the install.
- **"Command not found" after a successful install.** If `cargo` already works and its binary directory is on `PATH`, a newly installed command should normally be available immediately. Confirm installation with `cargo install --list`, inspect the final install output, and check whether `~/.cargo/bin` (or `%USERPROFILE%\.cargo\bin`) is on `PATH`. Reopen the shell only if the install or PATH setup changed it.
- **Verifying the install worked.** After any `cargo install`, immediately run the new command with `--version` or `--help`. If it prints something, the install succeeded. If it errors or isn't found, troubleshoot before moving on.
- **Compile times.** `cargo install` usually compiles from source and may take a while depending on dependencies and hardware. Wait for a successful final `Installing ...` message; if you interrupt it, rerun the command.

**You don't need to understand Rust yet.** The short exercise below introduces the build-and-test loop. Your first portfolio project (the bookmark manager) uses HTML and JavaScript; the Rust portfolio projects begin in Phase 2.

## Tool 5: Node.js and npm

Node.js is a JavaScript runtime you'll need starting in Phase 3, when the curriculum covers APIs and MCP servers. Some optional tools and reference MCP servers are distributed through npm, Node.js's package manager. Install it once now so you're not interrupted later.

**To install it:**

Go to [nodejs.org](https://nodejs.org) and download the **LTS** (Long Term Support) version for your operating system. Run the installer with default settings. On Mac and Linux you can alternatively use a version manager like [nvm](https://github.com/nvm-sh/nvm) if you already know what that is; if you don't, just use the installer from nodejs.org.

After installation, close and reopen your terminal, then verify both pieces installed:

```
node --version
npm --version
```

You should see version numbers for both. `node` runs JavaScript programs. `npm` is the package manager that installs tools and libraries (similar to how `cargo` works for Rust).

Prefer project-local packages or a one-off runner such as `npx` when the official instructions support them. A global install (`npm install -g <package>`) changes a user- or system-level tool and can become stale independently of a project, so use it only when the tool's current official instructions call for it.

You do not need to memorize JavaScript syntax before starting. You will still practice reading the small HTML and JavaScript project in Phase 1, while Node.js mainly serves as a prerequisite for later tools.

## Your Folder Structure

Create a consistent place for your guild work. Open your terminal and run:

```
cd ~
mkdir guild-projects
cd guild-projects
mkdir scratch
```

You now have:

- `~/guild-projects/` - Your main workspace, where your portfolio repository and any other projects will live
- `~/guild-projects/scratch/` - Where you experiment and practice without pressure

Your portfolio repository itself will be created in the next chapter (Git: Just Enough), cloned directly into `~/guild-projects/` as `~/guild-projects/guild-portfolio/`. No nested `portfolio/guild-portfolio/` wrapper — just one folder per project.

This structure isn't mandatory, but having a consistent place to work prevents the chaos of files scattered across your Desktop, Downloads, and random folders.

## Try It: Your First Rust Program

You now have the three things this exercise needs: an agent that can edit local project files, the Rust toolchain, and a scratch folder. From `~/guild-projects`, run:

```
cd scratch
cargo new hello-guild
cd hello-guild
cargo run
```

On Windows PowerShell, the same commands work. You should see `Hello, world!`. Cargo created the project, compiled it, and ran it.

Open the `hello-guild` folder in your coding agent. Ask:

> "Change `src/main.rs` so it asks the user for their name, then prints `Welcome to the guild, [name]!`. Use standard input, trim the newline, and handle input errors without panicking. Tell me which file you changed."

Review the diff, then run `cargo run` and type your name. Ask the agent to add a loop that exits when the user enters `quit`; run it again and test a name, an empty line, and `quit`. A successful compile is one piece of evidence. The observed behavior and edge-case checks are the rest.

Before asking for an explanation, write a short prediction of how input reaches the output and which branch exits the loop. Then ask the agent to explain the code and compare its explanation with the source. Change the welcome text manually, rerun it, and record any part you still cannot explain. Task completion and skill formation are different outcomes; the [evidence audit](../RESEARCH.md#what-the-evidence-supports) explains why this small comprehension check matters.

This project stays in `scratch/`; it is practice, not a portfolio requirement.

## Verifying Your Setup

Let's make sure everything works. Do each of these:

1. **Open VS Code.** If it opens without errors, you're good.
2. **Open your terminal.** Type `pwd` and press Enter. You should see a path on your screen. You're good.
3. **Check Rust.** Type `cargo --version`. You should see a version number. You're good.
4. **Check Node.js.** Type `node --version` and then `npm --version`. You should see a version number for each. You're good.
5. **Navigate to your workspace.** Type `cd ~/guild-projects` and then `ls`. You should see `scratch` listed (your portfolio folder gets created in the next chapter). You're good.
6. **Open your agent.** For a coding agent, authorize only `~/guild-projects/scratch/hello-guild`, ask it to explain `src/main.rs` without changing anything, and confirm that it names the file correctly. For browser chat, ask the same question after pasting the file contents.

If any of these steps didn't work, ask your agent to help you troubleshoot. Describe exactly what happened: what you typed, what you expected, and what you got instead. This is your first practice at communicating with an agent. Be specific about the problem.

## What You Don't Need

A quick list of things that might seem like prerequisites but aren't:

- **A powerful computer.** If it can run the editor and Rust toolchain, it is enough for these exercises. Model inference usually runs remotely, while local coding agents may also run commands and tools on your machine.
- **A second monitor.** Nice to have, not necessary.
- **Specific operating system.** Mac, Windows, and Linux all work fine.
- **A specific paid plan.** Limited free access may be enough for the early exercises, but availability and quotas change. Use the official plan pages above and do not buy a plan solely because this curriculum names a product.
- **Prior experience.** If you've read this far, you have enough.

You're set up. Next we'll cover just enough git to track your work, and then you're ready to start talking to agents.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Language Landscape](03-the-language-landscape.md) | **Your Workspace** | [Git: Just Enough →](05-git-just-enough.md) |

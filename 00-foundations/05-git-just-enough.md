# Git: Just Enough

## What Git Is and Why You Care

Git is a system that tracks changes to files over time. Think of it as an unlimited undo history for your entire project, except it also lets you share your work with other people, contribute to shared projects, and maintain a visible record of everything you've built.

For the guild, git matters for two reasons:

1. **Your portfolio lives in git.** When you submit projects for review, the community (and eventually, potential employers) can see not just the finished product but the history of how it evolved. Every change you made, every iteration after a roast, every improvement. It's all recorded.

2. **These learning guides live in git.** The repository you're reading from is a git repository. The community improves it over time by proposing changes through git.

You don't need to become a git expert. You need about seven commands and one website.

## Installing Git

**Mac:** Open your terminal and type `git --version`. If git is installed, you'll see a version number. If not, your Mac will prompt you to install it. Follow the prompts.

**Windows:** Download git from [git-scm.com](https://git-scm.com/download/win) and run the installer. Use the default settings for everything. After installation, open a new terminal window (close and reopen PowerShell) and type `git --version` to confirm it works.

**Linux:** Open your terminal and run `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora). Type `git --version` to confirm.

## Setting Up Your Identity

Git tags every change with your name and email so people know who did what. Run these two commands in your terminal, replacing the examples with your actual info:

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

You only do this once. Git remembers.

## GitHub: Where Your Work Lives Online

Git tracks changes on your computer. **GitHub** (github.com) is a website that stores your git projects online so other people can see them.

1. Go to [github.com](https://github.com) and create a free account
2. Remember your username. It becomes part of the web address for all your projects

Your guild portfolio will eventually live on GitHub, publicly visible. That URL (`github.com/yourusername`) becomes part of your professional identity.

## The Seven Commands

Here's everything you need to know about git, as seven commands. Each one gets a plain-language explanation of what it does and when you use it.

### `git init`

**What it does:** Tells git to start tracking a folder. You run this once per project, at the beginning.

**When you use it:** When you start a new project from scratch.

```
cd ~/guild-projects/portfolio
mkdir my-first-project
cd my-first-project
git init
```

You'll see a message like "Initialized empty Git repository." Your project is now being tracked.

### `git clone`

**What it does:** Downloads a copy of a project from GitHub onto your computer.

**When you use it:** When you want to get an existing project (like this learning path repository) onto your machine.

```
cd ~/guild-projects
git clone https://github.com/example/guild-learning-path.git
```

This creates a folder with all the project files inside it, already set up with git tracking.

### `git status`

**What it does:** Shows you what's changed since your last save point. Which files are new, which have been modified, which are ready to be saved.

**When you use it:** Constantly. This is your "what's going on?" command. Run it whenever you're not sure what state your project is in.

```
git status
```

The output will show files in different categories. Don't worry about the colors and categories for now. The important thing is that it tells you what's changed.

### `git add`

**What it does:** Tells git which changes you want to include in your next save point. Think of it as putting items on the counter before checkout.

**When you use it:** After you've made changes and you're ready to save them.

```
git add .
```

The `.` means "everything that changed." You can also add specific files by name (`git add index.html`), but `git add .` is fine for now. Don't overthink this step.

### `git commit`

**What it does:** Creates a save point (called a "commit") with a short message describing what you did. This is the actual moment your changes get recorded in history.

**When you use it:** After `git add`, when you want to lock in your changes with a description.

```
git commit -m "Add booking form to the landing page"
```

The `-m` flag means "message." The text in quotes describes what this save point contains. Write messages that describe *what changed*, not vague notes like "updates" or "stuff." Future you (and portfolio reviewers) will thank you.

**How often should you commit?** Think of it like saving a document. Do it whenever you've completed a meaningful chunk of work. Finished a feature? Commit. Fixed a bug? Commit. Completed a round of changes after a roast? Commit. You can't commit too often. You can definitely commit too rarely.

### `git push`

**What it does:** Sends your commits from your computer to GitHub so they're online and visible.

**When you use it:** After committing, when you want your work to show up on GitHub.

```
git push
```

The first time you push a new project, git might ask you to set up the connection to GitHub. It'll give you instructions. Follow them, or ask your agent for help. After the first time, `git push` just works.

### `git pull`

**What it does:** Downloads the latest changes from GitHub onto your computer. The reverse of push.

**When you use it:** When someone else has made changes to a shared project (like this learning path repository) and you want to get their updates.

```
git pull
```

## The Daily Workflow

In practice, your git usage will follow this pattern almost every time:

1. Do some work (build something, make changes, follow agent instructions)
2. `git status` - see what changed
3. `git add .` - stage all the changes
4. `git commit -m "Description of what I did"` - save the checkpoint
5. `git push` - send it to GitHub

That loop (work, status, add, commit, push) is 95% of what you'll ever do with git.

## Creating Your First Repository on GitHub

Let's put this together by creating your portfolio repository:

1. Go to github.com and click the "+" icon in the top right, then "New repository"
2. Name it `guild-portfolio`
3. Add a description: "My apprentice portfolio for the guild"
4. Check "Add a README file"
5. Click "Create repository"

Now clone it to your computer:

```
cd ~/guild-projects/portfolio
git clone https://github.com/YOUR-USERNAME/guild-portfolio.git
cd guild-portfolio
```

You now have a portfolio repository on GitHub connected to a folder on your computer. Everything you build and push will be publicly visible at `github.com/YOUR-USERNAME/guild-portfolio`.

## When Things Go Wrong

Git can occasionally get into confusing states, especially when you're learning. Here's the universal escape hatch:

**If git gives you an error you don't understand:** Copy the exact error message, paste it to your agent, and say "I'm new to git and got this error. What happened and how do I fix it?" The agent will walk you through it. This isn't a failure. It's using the tools available to you, which is literally the skill you're here to learn.

**If you're truly stuck:** The nuclear option is to copy your project files somewhere safe, delete the project folder, clone it fresh from GitHub, and copy your files back in. Inelegant, but it works, and nobody will judge you for it.

## What You Don't Need to Learn

Git has hundreds of features. You don't need these yet (and might never need them):

- Branching and merging (useful later, not now)
- Rebasing (even experienced developers argue about this)
- Cherry-picking (you'll know when you need it)
- Git hooks (automation for later)
- Submodules (complexity you can avoid)

The seven commands above are enough to track your work, share your portfolio, and participate in the guild. If you need more advanced git operations, your agent can walk you through them when the time comes.

## The Takeaway

Git is your project's memory and your portfolio's backbone. Seven commands handle everything you need: `init`, `clone`, `status`, `add`, `commit`, `push`, `pull`. Use them in the work-status-add-commit-push loop, and your entire journey gets recorded.

You now have everything you need for Phase 0. You understand what code is (conceptually), your workspace is set up, and you can track and share your work. Time to learn how to actually talk to agents.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Your Workspace](04-your-workspace.md) | **Git: Just Enough** | [How Agents Think →](../01-talking-to-agents/01-how-agents-think.md) |

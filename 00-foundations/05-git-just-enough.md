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
cd ~/guild-projects/scratch
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

The first time you push, GitHub needs to verify that you're really you. GitHub stopped accepting regular account passwords for git operations in 2021, so there's a one-time setup step. Don't skip past this — it's the single most common place beginners get stuck on git, and getting it right now saves an hour of confusion later. See the next section for the walkthrough.

### One-Time Setup: Authenticating with GitHub

You have two options for proving your identity to GitHub from the terminal. Pick one and follow it through. **The Personal Access Token (PAT) path is easier for beginners**, so that's what we'll walk through here. The SSH key path is shown at the end for anyone who already prefers it.

**Personal Access Token (recommended)**

A Personal Access Token is a long password-like string that you create on GitHub and use in place of your account password for git operations. Think of it as a dedicated password just for the command line.

1. Go to [github.com](https://github.com) and sign in.
2. Click your profile picture in the top right → **Settings**.
3. Scroll all the way down the left sidebar and click **Developer settings**.
4. Click **Personal access tokens** → **Tokens (classic)**.
5. Click **Generate new token** → **Generate new token (classic)**. (GitHub may prompt you to confirm your account password.)
6. In the **Note** field, type something like "my laptop" so future-you remembers what this token is for.
7. Under **Expiration**, pick something reasonable. 90 days is the default and is fine.
8. Under **Select scopes**, check the box for `repo`. That's the only scope you need. Don't check anything else.
9. Scroll to the bottom and click **Generate token**.
10. GitHub shows the token once, as a long string starting with `ghp_`. **Copy it immediately** and paste it somewhere safe temporarily (a password manager is ideal, a sticky note is fine for the next few minutes). **Once you leave this page you cannot see the token again** — GitHub only shows it once. If you lose it, you just generate a new one.

Now push for the first time. In your terminal:

```
git push
```

Git will prompt for your **username** (your GitHub username) and your **password** (paste the token you just copied, not your account password). On most systems, git stores the token in a "credential helper" after the first successful push, so you only do this once per computer.

**You know it worked when:** the push completes with no error, and refreshing your repository on github.com shows your commits.

**Common errors and what they mean:**

- `remote: Support for password authentication was removed on August 13, 2021.` You used your account password instead of a Personal Access Token. Go back and paste the token.
- `remote: Permission to USER/REPO.git denied to OTHER_USER.` The token belongs to a different GitHub account than the one that owns the repo. Double-check which account you signed into on github.com when you created the token.
- `fatal: Authentication failed for 'https://github.com/...'` Usually means the token was wrong (typo when pasting) or expired. Generate a fresh token and try again.
- Terminal shows no feedback when you paste the token. That's normal — terminals silently accept pasted passwords without showing dots or characters. Paste and press Enter.

**SSH keys (alternative, for later)**

If you already know how to use SSH keys, or you want to set them up later instead of tokens, the process is: generate a key pair with `ssh-keygen -t ed25519`, copy the contents of `~/.ssh/id_ed25519.pub` into GitHub → Settings → SSH and GPG keys → New SSH key, then change your repository's remote URL from `https://github.com/USER/REPO.git` to `git@github.com:USER/REPO.git`. This is nicer long-term because you don't deal with token expiration, but the setup has more moving parts. Don't stress about it now — the PAT path works fine for years.

After the first time, `git push` just works. No more prompts.

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

Now clone it to your computer. Note that we clone directly into `~/guild-projects/`, not into a `portfolio/` subfolder — git creates the `guild-portfolio/` directory for you.

```
cd ~/guild-projects
git clone https://github.com/YOUR-USERNAME/guild-portfolio.git
cd guild-portfolio
```

You now have a portfolio repository on GitHub connected to a folder on your computer at `~/guild-projects/guild-portfolio/`. Everything you build and push will be publicly visible at `github.com/YOUR-USERNAME/guild-portfolio`.

## When Things Go Wrong

Git can occasionally get into confusing states, especially when you're learning. Here's the universal escape hatch:

**If git gives you an error you don't understand:** Copy the exact error message, paste it to your agent, and say "I'm new to git and got this error. What happened and how do I fix it?" The agent will walk you through it. This isn't a failure. It's using the tools available to you, which is literally the skill you're here to learn.

**If you're truly stuck:** The nuclear option is to copy your project files somewhere safe, delete the project folder, clone it fresh from GitHub, and copy your files back in. Inelegant, but it works, and nobody will judge you for it.

## What You Don't Need to Learn

Git has hundreds of features. You don't need these yet (and might never need them):

- Branching and merging — you'll need these starting in Phase 3 when the Workshop chapter has you contributing to shared codebases. The bridge chapter [Branches and Pull Requests](../02-the-methodology/03-branches-and-pull-requests.md) in Phase 2 teaches everything you need to know, and it's only three more commands on top of these seven. Come back to it when you get there.
- Rebasing (even experienced developers argue about this)
- Cherry-picking (you'll know when you need it)
- Git hooks (automation for later)
- Submodules (complexity you can avoid)

The seven commands above are enough to track your work through your first portfolio projects. If you need more advanced git operations, your agent can walk you through them when the time comes.

## The Takeaway

Git is your project's memory and your portfolio's backbone. Seven commands handle everything you need: `init`, `clone`, `status`, `add`, `commit`, `push`, `pull`. Use them in the work-status-add-commit-push loop, and your entire journey gets recorded.

You now have everything you need for Phase 0. You understand what code is (conceptually), your workspace is set up, and you can track and share your work. Time to learn how to actually talk to agents.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Your Workspace](04-your-workspace.md) | **Git: Just Enough** | [The Guild →](06-the-guild.md) |

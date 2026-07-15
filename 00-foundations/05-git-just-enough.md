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

Your guild portfolio can live on GitHub. Keep repositories private when they contain personal data, secrets, employer code, or anything you lack permission to publish. Share only a reviewed portfolio index and projects that are safe to make public.

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
git clone https://github.com/Navigators-Guild/apprentice-onboarding.git
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

The `.` means "everything that changed," including files you may not intend to publish. Prefer specific paths such as `git add index.html README.md`, then run `git diff --staged` before every commit. Use `git add .` only after `git status` confirms the whole change set belongs together and contains no secrets or private data.

### `git commit`

**What it does:** Creates a save point (called a "commit") with a short message describing what you did. This is the actual moment your changes get recorded in history.

**When you use it:** After `git add`, when you want to lock in your changes with a description.

```
git commit -m "Add booking form to the landing page"
```

The `-m` flag means "message." The text in quotes describes what this save point contains. Write messages that describe *what changed*, not vague notes like "updates" or "stuff." Future you (and portfolio reviewers) will thank you.

**How often should you commit?** Commit a coherent, reviewable change after its relevant checks pass. A feature may need several commits; a one-line fix may need one. Avoid mixing unrelated work or creating meaningless checkpoint commits that make review harder.

### `git push`

**What it does:** Sends your commits from your computer to GitHub so they're online and visible.

**When you use it:** After committing, when you want your work to show up on GitHub.

```
git push
```

The first time you push, GitHub needs to verify that you're really you. GitHub stopped accepting regular account passwords for git operations in 2021, so there's a one-time setup step. Don't skip past this — it's the single most common place beginners get stuck on git, and getting it right now saves an hour of confusion later. See the next section for the walkthrough.

### One-Time Setup: Authenticating with GitHub

You have two common options for proving your identity to GitHub from the terminal. Pick one and follow it through. This chapter walks through a fine-grained Personal Access Token (PAT); SSH is linked afterward.

#### Fine-grained Personal Access Token

A Personal Access Token is a password-like secret that you create on GitHub and use in place of your account password for HTTPS git operations. GitHub [recommends fine-grained tokens when possible](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) because you can limit them to selected repositories and permissions.

1. Go to [github.com](https://github.com) and sign in.
2. Click your profile picture in the top right → **Settings**.
3. Scroll all the way down the left sidebar and click **Developer settings**.
4. Click **Personal access tokens** → **Fine-grained tokens** → **Generate new token**.
5. Give it a descriptive name such as "portfolio pushes" and choose a short expiration you will notice and renew.
6. Choose your account as the resource owner and select **Only select repositories**. Select only your portfolio repository.
7. Under **Repository permissions**, grant **Contents: Read and write**. Leave unrelated permissions at their defaults.
8. Generate the token. Copy it once into a password manager; do not put it in a note, prompt, repository, or shell history.

GitHub recommends the minimum permissions and shortest practical lifetime for credentials; see its [API credential guidance](https://docs.github.com/en/rest/authentication/keeping-your-api-credentials-secure).

Now push for the first time. In your terminal:

```
git push
```

Git will prompt for your **username** (your GitHub username) and your **password** (paste the token, not your account password). A configured credential manager can store it securely. If Git prompts every time, install or configure [Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md) instead of saving the token in a plain-text file.

**You know it worked when:** the push completes with no error, and refreshing your repository on github.com shows your commits.

**Common errors and what they mean:**

- `remote: Support for password authentication was removed on August 13, 2021.` You used your account password instead of a Personal Access Token. Go back and paste the token.
- `remote: Permission to USER/REPO.git denied to OTHER_USER.` The token belongs to a different account, does not include this repository, or lacks Contents write permission. Check all three.
- `fatal: Authentication failed for 'https://github.com/...'` Usually means the token was wrong (typo when pasting) or expired. Generate a fresh token and try again.
- Terminal shows no feedback when you paste the token. That's normal — terminals silently accept pasted passwords without showing dots or characters. Paste and press Enter.

#### SSH keys (alternative, for later)

If you already know how to use SSH keys, or want to set them up later, follow GitHub's [SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). SSH avoids PAT expiration for git transport but still requires protecting and occasionally rotating your key.

After a credential manager stores the token, `git push` should stop prompting until the credential expires, is revoked, or no longer has access.

### `git pull`

**What it does:** Downloads the latest changes from GitHub onto your computer. The reverse of push.

**When you use it:** When someone else has made changes to a shared project (like this learning path repository) and you want to get their updates.

```
git pull --ff-only
```

`--ff-only` updates your branch only when Git can move it forward without creating an unexpected merge commit. If it refuses, run `git status` and inspect how your local history differs before choosing a merge or rebase.

## The Daily Workflow

In practice, your git usage will follow this pattern almost every time:

1. Do some work (build something, make changes, follow agent instructions)
2. `git status` - see what changed
3. `git add <the-files-you-intend>` - stage selected changes
4. `git diff --staged` - inspect exactly what the commit will contain
5. `git commit -m "Description of what I did"` - save the checkpoint
6. `git push` - send it to GitHub

That loop covers the core solo workflow. Shared projects add branches, reviews, and conflict handling later.

## Keep a Learning Log

Create `LEARNING_LOG.md` in your portfolio and append one dated entry after each meaningful session:

```markdown
## 2026-07-15
- Goal: what I intended to finish
- Tried: commands, prompts, or approaches I used
- Evidence: tests, observed behavior, or review results
- Learned: what changed in my mental model
- Next: the smallest sensible follow-up
```

Commit the log with the work it describes. Treat it as append-only history: do not rewrite an awkward earlier entry to look smarter; add a correction in the next entry. Reflection is not magic note-taking, but structured reflective interventions have shown a positive average effect across a [meta-analysis of 25 studies](https://doi.org/10.1016/j.tsc.2023.101373). The log also gives reviewers concrete evidence of how your decisions changed.

## Creating Your First Repository on GitHub

Let's put this together by creating your portfolio repository:

1. Go to github.com and click the "+" icon in the top right, then "New repository"
2. Name it `guild-portfolio`
3. Add a description: "My apprentice portfolio for the guild"
4. Check "Add a README file"
5. Choose **Public** only if the portfolio contains no employer/client code, personal data, secrets, private prompts, or material you lack permission to publish. Otherwise start private and publish redacted artifacts later.
6. Click "Create repository"

Now clone it to your computer. Note that we clone directly into `~/guild-projects/`, not into a `portfolio/` subfolder — git creates the `guild-portfolio/` directory for you.

```
cd ~/guild-projects
git clone https://github.com/YOUR-USERNAME/guild-portfolio.git
cd guild-portfolio
```

You now have a portfolio repository on GitHub connected to `~/guild-projects/guild-portfolio/`. If you selected Public, pushed files are visible at `github.com/YOUR-USERNAME/guild-portfolio`; if you selected Private, only authorized accounts can see them.

## When Things Go Wrong

Git can occasionally get into confusing states, especially when you're learning. Here's the universal escape hatch:

**If git gives you an error you don't understand:** Capture `git status` and the error, redact tokens, private URLs, usernames, and sensitive paths, then ask your agent to explain before running any destructive command. Request a backup and recovery plan when history could change.

**If you're truly stuck:** Do not delete the original. Clone the repository into a new sibling folder, compare it with the old folder, and recover only the intended uncommitted files after reviewing the diff. Keeping the original preserves recovery options.

## What You Don't Need to Learn

Git has hundreds of features. You don't need these yet (and might never need them):

- Branching and merging — you'll need these starting in Phase 3 when the Workshop chapter has you contributing to shared codebases. The bridge chapter [Branches and Pull Requests](../02-the-methodology/03-branches-and-pull-requests.md) in Phase 2 teaches the common operations. Come back to it when you get there.
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

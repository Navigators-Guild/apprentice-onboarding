# Branches and Pull Requests

## Why You Need This Now

Back in Phase 0, the git chapter explicitly said branching and merging were "useful later, not now." That was true: for your own portfolio projects you can live on the main branch and push straight to GitHub, and the seven commands in that chapter handle 95% of your daily git needs.

Phase 3 is "later." Starting with the Workshop chapter, you'll contribute to codebases other people also work in, and that changes the rules. You can't push straight to main in a shared repository — your changes need to be proposed, reviewed, and merged. The mechanism for that is the **pull request**, and pull requests require **branches**. This chapter is the bridge.

Good news: it's not a lot more git. Three new commands and one web workflow on GitHub. Read this once before starting Phase 3.

## What a Branch Is

A git branch is a parallel line of history in your repository. The default branch (usually called `main`) is the "official" version everyone shares. When you want to make changes without disturbing main, you create a new branch off of main, work on it, and eventually propose merging your branch back in.

Think of it like this: main is the published draft of a book. When you want to write a new chapter, you don't scribble directly on the published copy. You make a copy, write your changes on the copy, and then hand it to an editor who decides whether it's ready to go into the next printing. The copy is a branch. The decision process is a pull request. The printing is a merge.

Branches are cheap in git. They're just labels pointing at a particular commit, not copies of the whole project. Creating a branch takes a fraction of a second. You can have many branches open at once, one per feature or fix. Professional developers create branches constantly.

## What a Pull Request Is

A pull request (also called a "PR," or on GitLab a "merge request") is a formal proposal to merge a branch into another branch. It's hosted on GitHub (or whatever platform the project uses), has its own web page, and supports discussion: reviewers leave comments on specific lines, ask questions, request changes. The author (you) can push more commits to the branch to address feedback, and those commits automatically show up in the PR. When everyone is satisfied, a maintainer clicks "Merge" and your work becomes part of main.

The PR is the review artifact. It's also the historical record: long after the branch is deleted, the merged PR page preserves the full discussion of why the change was made and what feedback it got. When you later wonder "why is this code like this?" you can often find the answer on the PR that introduced it.

## The Three New Commands

Beyond the seven from Phase 0, you need three more git commands for the branch-and-PR workflow.

### `git checkout -b <branch-name>`

**What it does:** Creates a new branch with the given name and switches you to it. Your current working files come with you.

**When you use it:** At the start of any piece of work that will become a pull request.

```
git checkout -b add-progress-command
```

Name branches descriptively and in lowercase with hyphens. Good: `add-progress-command`, `fix-empty-title-bug`, `improve-error-messages`. Bad: `my-branch`, `work`, `test`.

### `git push -u origin HEAD`

**What it does:** Pushes your current branch to GitHub for the first time, and remembers that this is where it goes so future `git push` calls work without arguments.

**When you use it:** The first time you push a new branch. After that, `git push` alone works for the same branch.

```
git push -u origin HEAD
```

`HEAD` is git shorthand for "whatever branch I'm on right now." `-u` (short for `--set-upstream`) tells git to remember the connection. You only need this once per branch.

### `git checkout main`

**What it does:** Switches you back to the main branch.

**When you use it:** After a pull request is merged (or abandoned), to go back to the main line and start fresh work.

```
git checkout main
git pull
```

That two-command sequence is how you refresh your local main with everyone's latest changes before creating your next branch. Get in the habit of pulling main before starting new work.

## Forks Versus Collaborator Access

There are two ways to contribute to a shared repository, and they determine where your branches live.

**Collaborator access.** If you've been added as a collaborator on the repository (common for private team repos and small trusted projects), you can push branches directly to the upstream repo. Your `git push -u origin HEAD` goes straight to the canonical copy, and you open PRs within that same repo. This is the simpler flow.

**Fork-and-PR.** For most open source projects, including the guild-toolkit, you're not a collaborator. The flow there is: click **Fork** on github.com/Navigators-Guild/guild-toolkit to create `github.com/YOUR-USERNAME/guild-toolkit`, clone your fork, add the canonical repo as a second remote called `upstream`, push your branches to your fork (`origin`), then open a PR from your fork's branch back to `upstream/main`. GitHub's PR creation UI handles the cross-repo part automatically — when you click **Compare & pull request**, it correctly identifies the upstream as the target.

The rest of this chapter assumes either flow. The commands are the same. The only differences are (1) you fork first if you need to, (2) you add an upstream remote if you're using a fork, and (3) you refresh main by pulling from `upstream/main` instead of just `origin/main`.

## The Full Workflow

Here's what contributing to a shared repository looks like end-to-end. Assume you've already cloned the repository (or your fork) and you're in its folder.

**1. Refresh main.**

```
git checkout main
git pull
```

This pulls in any changes other people have merged since the last time you worked. Skipping this step is the most common cause of merge conflicts later.

**2. Create a branch for your work.**

```
git checkout -b add-progress-command
```

Pick a name that describes what the branch is for. From this point until you merge, you're working on the branch, not on main.

**3. Build and commit.**

Exactly like your portfolio projects: let your agent make changes, verify, commit. Each commit should describe one meaningful change.

```
git add .
git commit -m "Add progress command skeleton"
git add .
git commit -m "Parse curriculum TOML and list phases"
git add .
git commit -m "Show completion percentages"
```

Multiple commits on the same branch is normal and good. You're building a small, readable history of how the feature came together.

**4. Push the branch to GitHub.**

```
git push -u origin HEAD
```

First push of this branch uses `-u`. GitHub now has a copy of your branch with all your commits.

**5. Open the pull request on GitHub.**

Go to the repository on github.com. GitHub notices you just pushed a new branch and shows a yellow banner across the top: "You recently pushed branches: [add-progress-command] — Compare & pull request." Click the **Compare & pull request** button.

If the banner isn't there, click the **Pull requests** tab → **New pull request**, then pick your branch from the dropdown.

On the PR creation page:

- **Title:** A one-line summary. Present-tense, imperative. "Add progress command" not "Added progress command" or "progress command stuff."
- **Description:** What you built, why, and anything reviewers should know. Link to the issue it addresses if there is one. Call out anything you're unsure about — reviewers appreciate when you flag your own uncertainty.
- **Reviewers:** If the project has a review convention, request reviewers. Otherwise leave blank; maintainers will find it.

Click **Create pull request**.

**6. Wait for CI and reviews.**

If the repository has continuous integration (see the Shipping It chapter for what CI is), it starts running as soon as you push. You'll see yellow dots (pending), green checkmarks (passing), or red Xs (failing) next to your commits on the PR page. If anything goes red, click through, read the log, and fix the problem. Then push another commit to the same branch — the PR updates automatically and CI re-runs.

Reviewers will leave comments. Some will be on specific lines of code (inline comments), some on the PR as a whole. Read them all. Address the valid ones with new commits on the same branch. Push those commits — they show up in the PR immediately.

**7. Address review feedback.**

Same loop as the adversarial review from Phase 1: read, decide what's valid, fix, explain what you did and why. Reviewers can mark their comments as resolved once they're satisfied. Keep pushing commits until everyone approves.

**8. Merge.**

Once the PR is approved and CI is green, a maintainer (or you, if you have merge permission) clicks the **Merge pull request** button on GitHub. Your branch is merged into main, and your code is now part of the project.

**9. Clean up.**

```
git checkout main
git pull
git branch -d add-progress-command
```

Switch back to main, pull the now-updated main (which includes your merged changes), and delete the local copy of your branch. You're ready to start the next piece of work.

## Common Problems

**"Merge conflicts."** Sometimes two branches change the same line of the same file in different ways, and git can't figure out which version to keep. The PR page will show a "This branch has conflicts" message with a list of affected files. Fix by: (1) `git checkout main && git pull` to update main, (2) `git checkout your-branch && git merge main`, (3) open each conflicted file in VS Code — it shows both versions clearly with `<<<<<<<`, `=======`, and `>>>>>>>` markers — and pick the right resolution, (4) `git add .` and `git commit` to finalize the merge, (5) `git push`. Your PR updates automatically.

**"CI failing on something that works locally."** Most common cause: you forgot to commit a new file, so CI can't find it. Run `git status` and check for untracked files. If everything is committed, read the CI log carefully — the error is usually a specific line number.

**"I made a commit on the wrong branch."** You meant to create a feature branch first and accidentally committed to main instead. Fix: `git checkout -b my-feature-branch` (creates a branch from your current state), then `git checkout main && git reset --hard origin/main` (resets your local main back to what's on GitHub, discarding the misplaced commits from main only — they're still on your feature branch). This is one of the few destructive git commands; double-check you're on main before running the reset.

**"My branch is behind main and CI says I need to update."** Someone else merged a PR after you opened yours, and the project requires branches to be up to date with main before merging. Fix: `git checkout main && git pull && git checkout your-branch && git merge main`, resolve any conflicts, push.

**"I pushed a commit that I want to undo."** If the PR hasn't merged yet, you can rewrite the branch. Simplest option: `git reset --hard HEAD~1` (removes the last commit locally) then `git push --force-with-lease` (updates the remote branch). Use `--force-with-lease` not `--force`; the -with-lease version is safer because it refuses to overwrite someone else's work. Do NOT force-push a branch that other people are working on — that's how teams lose work.

## Reviewing Someone Else's PR

Eventually you'll be on the other side: looking at someone else's branch and deciding whether it should be merged. This is part of Phase 4 (Giving Back) and also just a normal part of contributing to shared code.

To review:

1. Open the PR page on GitHub.
2. Read the description. Understand what the author is trying to do and why.
3. Click the **Files changed** tab. GitHub shows a diff: red lines are removed, green lines are added.
4. Read the diff. Pretend you're the adversarial reviewer: does this handle empty input? Are there edge cases the author missed? Is the error handling clear? Are variable names meaningful? Does the code match the project's existing style?
5. Leave comments inline by hovering over a line and clicking the blue `+` icon. Be specific and constructive — the same tone you'd want on your own work.
6. When you're done, click **Review changes** at the top right, write an overall summary, and pick one of:
   - **Comment** — feedback without a decision
   - **Approve** — this is ready to merge
   - **Request changes** — this needs work before merging

The author sees your review and responds. The cycle repeats until approval.

## Where This Fits

You will use the branch-and-PR workflow throughout Phase 3 and Phase 4 — the Workshop chapter requires it, your toolkit contributions go through it, and the portfolio review process uses it as evidence of how you collaborate. You'll also use it anytime you contribute to an open source project outside the guild, which is most of them.

The command vocabulary from Phase 0 still holds. You'll use `git status`, `git add`, `git commit`, and `git push` constantly. `git checkout -b`, `git push -u origin HEAD`, and `git checkout main` are the additions that let you work the way professional teams do.

Now you're ready for Phase 3.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Tracking Your Work](02-tracking-your-work.md) | **Branches and Pull Requests** | [The Workshop →](../03-real-world-skills/01-the-workshop.md) |

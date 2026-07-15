# Branches and Pull Requests

## Why You Need This Now

Back in Phase 0, the git chapter explicitly said branching and merging were "useful later, not now." For your own portfolio projects you can use a simple main-branch workflow, while shared repositories usually add branches and review.

Phase 3 is "later." Starting with the Workshop chapter, you'll contribute to shared codebases, and that changes the workflow. Many projects protect `main` and require changes through a pull request; others use different policies. Read the repository's contribution guide. This chapter teaches the common branch-and-PR flow.

The common flow adds a few branch operations and one web workflow on GitHub. Read this once before starting Phase 3.

## What a Branch Is

A git branch is a parallel line of history in your repository. The default branch (usually called `main`) is the "official" version everyone shares. When you want to make changes without disturbing main, you create a new branch off of main, work on it, and eventually propose merging your branch back in.

Think of it like this: main is the published draft of a book. When you want to write a new chapter, you don't scribble directly on the published copy. You make a copy, write your changes on the copy, and then hand it to an editor who decides whether it's ready to go into the next printing. The copy is a branch. The decision process is a pull request. The printing is a merge.

Branches are cheap in git. They're just labels pointing at a particular commit, not copies of the whole project. Creating a branch takes a fraction of a second. You can have many branches open at once, one per feature or fix. Professional developers create branches constantly.

## What a Pull Request Is

A pull request (also called a "PR," or on GitLab a "merge request") is a formal proposal to merge a branch into another branch. It's hosted on GitHub (or whatever platform the project uses), has its own web page, and supports discussion: reviewers leave comments on specific lines, ask questions, request changes. The author (you) can push more commits to the branch to address feedback, and those commits automatically show up in the PR. When everyone is satisfied, a maintainer clicks "Merge" and your work becomes part of main.

The PR is the review artifact. It's also the historical record: long after the branch is deleted, the merged PR page preserves the full discussion of why the change was made and what feedback it got. When you later wonder "why is this code like this?" you can often find the answer on the PR that introduced it.

## The Branch Operations

Beyond the Phase 0 workflow, you need to create and switch branches and publish a new remote branch.

### `git switch -c <branch-name>`

**What it does:** Creates a new branch with the given name and switches you to it. Your current working files come with you.

**When you use it:** At the start of any piece of work that will become a pull request.

```
git switch -c add-progress-command
```

Name branches descriptively and in lowercase with hyphens. Good: `add-progress-command`, `fix-empty-title-bug`, `improve-error-messages`. Bad: `my-branch`, `work`, `test`.

### `git push -u origin HEAD`

**What it does:** Pushes your current branch to GitHub for the first time, and remembers that this is where it goes so future `git push` calls work without arguments.

**When you use it:** The first time you push a new branch. After that, `git push` alone works for the same branch.

```
git push -u origin HEAD
```

`HEAD` is git shorthand for "whatever branch I'm on right now." `-u` (short for `--set-upstream`) tells git to remember the connection. You only need this once per branch.

### `git switch main`

**What it does:** Switches you back to the main branch.

**When you use it:** After a pull request is merged (or abandoned), to go back to the main line and start fresh work.

```
git switch main
git pull --ff-only
```

That two-command sequence is how you refresh your local main with everyone's latest changes before creating your next branch. Get in the habit of pulling main before starting new work.

## Forks Versus Collaborator Access

There are two ways to contribute to a shared repository, and they determine where your branches live.

**Collaborator access.** If you've been added as a collaborator on the repository (common for private team repos and small trusted projects), you can push branches directly to the upstream repo. Your `git push -u origin HEAD` goes straight to the canonical copy, and you open PRs within that same repo. This is the simpler flow.

**Fork-and-PR.** For most open-source projects, including the guild-toolkit, you're not a collaborator. Fork the repository, clone your fork, add the canonical repository as `upstream`, push feature branches to your fork (`origin`), then open a PR to the base branch named by the contribution guide. The guild-toolkit currently uses `develop`, not `main`. Always verify the base in GitHub's PR form; its automatic suggestion can be wrong for a repository with a non-default integration branch.

The examples below use `main` as the PR base. Substitute the base named by the project's contribution guide—for example, the guild-toolkit currently uses `develop`. With a fork, fetch the canonical base from `upstream` and push your feature branch to `origin`.

## The Full Workflow

Here's what contributing to a shared repository looks like end-to-end. Assume you've already cloned the repository (or your fork) and you're in its folder.

**1. Refresh the base branch.**

```
git switch main
git pull --ff-only
```

This pulls in changes merged since the last time you worked. If you use a fork, fetch and fast-forward from the canonical `upstream` base instead. Starting from current work reduces avoidable conflicts.

**2. Create a branch for your work.**

```
git switch -c add-progress-command
```

Pick a name that describes what the branch is for. From this point until you merge, you're working on the branch, not on main.

**3. Build and commit.**

Exactly like your portfolio projects: let your agent make changes, verify, commit. Each commit should describe one meaningful change.

```bash
git add src/main.rs
git diff --staged
git commit -m "Add progress command skeleton"

git add src/curriculum.rs tests/curriculum.rs
git diff --staged
git commit -m "Parse curriculum TOML and list phases"

git add src/output.rs tests/output.rs
git diff --staged
git commit -m "Show completion percentages"
```

Multiple commits on the same branch are normal. Before each commit, run `git status` and `git diff --staged`; stage selected paths when `git add .` would include unrelated files or secrets.

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

If the repository has continuous integration configured for this branch or PR event, it runs after the push or PR creation. You'll see pending, passing, failing, skipped, or neutral checks. Open failed checks, find the first causal error, reproduce it locally when practical, and push a focused fix. The PR then updates and applicable checks run again.

Reviewers may leave inline or overall comments. Read them all. Address valid findings with new commits on the same branch and explain rejected suggestions with evidence. Never paste credentials or sensitive logs into the PR.

**7. Address review feedback.**

Same loop as the adversarial review from Phase 1: read, decide what's valid, fix, explain what you did and why. Reviewers can mark their comments as resolved once they're satisfied. Keep pushing commits until everyone approves.

**8. Merge.**

Once the repository's approvals and required checks are satisfied, an authorized maintainer merges according to project policy. The feature branch then becomes part of the selected base branch.

**9. Clean up.**

```
git switch main
git pull --ff-only
git branch -d add-progress-command
```

Switch back to the actual base branch, fast-forward it from the correct remote, and delete the local feature branch only after confirming the merge. Substitute `develop` when that was the base.

## Common Problems

**"Merge conflicts."** Sometimes two branches change the same lines in incompatible ways, and Git needs a person to choose the result. First preserve uncommitted work. Then: (1) `git switch main && git pull --ff-only` to update local `main`, (2) `git switch your-branch && git merge main`, (3) open each conflicted file in VS Code and resolve the `<<<<<<<`, `=======`, and `>>>>>>>` sections intentionally, (4) run `git status`, stage only the resolved paths with `git add <file>`, and run the relevant checks, (5) `git commit` and `git push`. If the repository prefers rebasing or you do not understand the conflict, stop and ask a maintainer before rewriting history.

**"CI failing on something that works locally."** Check for uncommitted files, platform differences, toolchain versions, feature flags, missing services, nondeterminism, and environment assumptions. Read the first causal failure, not only the final summary. Redact secrets before sharing logs.

**"I made a commit on the wrong branch."** Stop before pushing. Create a backup branch pointing to the commit and ask an experienced collaborator or your agent for a recovery plan based on `git status`, `git branch --show-current`, and `git log --oneline --decorate -5`. Do not copy a `reset --hard` recipe blindly; it can discard unrelated uncommitted work.

**"My branch is behind the base branch and CI says I need to update."** Someone merged work after you opened yours. Follow the repository's merge-or-rebase policy. For a merge-based `main` workflow: `git switch main`, `git pull --ff-only`, `git switch your-branch`, `git merge main`, resolve and test, then push. Substitute `develop` or another branch when that is the PR base.

**"I pushed a commit that I want to undo."** The safest shared-history default is `git revert <commit-sha>`, which creates a new commit that reverses the selected change. Rewriting a PR branch may be acceptable under the repository's policy, but coordinate first and preserve a backup; never force-push a branch other people use.

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

The Phase 0 vocabulary still applies. Add `git switch -c <branch>`, `git switch <base>`, and `git push -u origin HEAD` for the common branch-and-PR flow, then follow each repository's base-branch and history policy.

Now you're ready for Phase 3.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Tracking Your Work](02-tracking-your-work.md) | **Branches and Pull Requests** | [The Workshop →](../03-real-world-skills/01-the-workshop.md) |

# The Guild: What It Is and How to Reach It

## Read This Before You Go Looking

Throughout this curriculum you'll see references to **the guild**. The guild channel. The guild community. The guild toolkit. Submitting your work to guild reviewers. Finding mentors in the guild. That language will make more sense with some plain-language context.

This chapter tells you what the guild actually is right now, what it aspires to be, and exactly how you participate in the parts that exist today. No mystery, no hidden prerequisites.

## The Current State

The guild is a community of apprentices, journeymen, and masters learning to direct AI agents to build software. It is a young project. As of this writing, the full infrastructure described in the curriculum — a dedicated review channel with live reviewers, a toolkit repository with a roster of apprentice-friendly issues, a formal mentorship program, a certificate-granting portfolio board — is being built in the open, and some of those pieces don't exist yet.

This is not a problem you need to solve. It's context so that when the curriculum says "submit your work in the guild channel," you know what to actually do today, and what to expect as the community grows.

## What You Use Today

Here is how you participate in each piece of the guild *right now*, using only tools you already have or will set up in this phase.

### Your "adversarial review channel" today: the AI adversary

Adversarial review is the core of the methodology. The curriculum eventually describes submitting your work to a community channel where experienced members will roast it. Until that channel has enough active reviewers to give you fast feedback, your default reviewer is **a second AI conversation configured to be hostile**.

This actually works very well. The AI adversary is patient, available at 3am, doesn't get tired, and will produce pages of specific critique on demand. The workflow:

1. Finish a piece of work (a chapter exercise, a project layer, a full build).
2. Open a **new, clean conversation** with your agent — not the same conversation you used to build the thing. This matters. The adversary should not have the builder's context.
3. Paste your design document, your code, and your process notes.
4. Give the adversary its role explicitly. A prompt like:

   > "You are an adversarial reviewer. Your job is to find every weakness, bug, edge case, missing validation, unclear error message, inconsistent naming, security vulnerability, and documentation gap in the work below. Be specific and harsh. Cite file names and line numbers where you can. Do not soften your critique. Do not add compliments. Assume the person who wrote this is strong enough to hear the truth and fix it. Here is the work: [paste]."

5. Read the response all the way through before reacting (re-read the Forward if you need the reminder on why).
6. Address the valid critiques, push back on the noise, and document both in your PROCESS.md.

You can stack this with a second, differently-framed adversary — one prompt focused on security, another on user experience, another on code organization — and aggregate their feedback. The AI adversary is free and scales to as many reviews as you want to run.

### Your "guild community" today: the public GitHub portfolio

Every project you build is tracked in git and pushed to a public GitHub repository. The portfolio itself is the community-facing artifact. When someone finds your `guild-portfolio` repo, they can read your design docs, your commits, your process notes, and your AI-adversary review history.

That visibility is the entry point to the community. As the guild grows, other apprentices will find your work the same way you'll find theirs: by looking at public portfolios in the `guild-portfolio` naming convention or linked from shared directories (once those exist). Building in public is itself guild participation.

### Your "mentors" today: the people already around you

Formal mentorship pairing isn't set up yet. In the meantime, mentors come from three places:

1. **Anyone further along than you.** A friend who already codes, a coworker who builds software, a family member with technical experience — if they're willing to look at a piece of your work and tell you what they notice, they're a mentor for that review. You don't need a title to be useful to a beginner.
2. **The AI adversary.** A well-prompted AI reviewer is a kind of mentor: it will explain *why* something is wrong, not just that it is, and will answer follow-up questions. Treat it as a tireless tutor.
3. **Other apprentices building the same curriculum.** When you find another apprentice's public portfolio, you can read their work, learn from their mistakes, and — if they've made their contact info available — reach out. Peer learning is real learning.

### Your "guild toolkit" today: your own portfolio projects

Phase 3 includes a Workshop chapter built around contributing to the guild's shared toolkit repository. The toolkit is a work in progress. If the repository referenced in that chapter doesn't yet exist or hasn't been populated with apprentice-friendly issues, the chapter's skills (reading existing code, working within constraints, the PR process) transfer cleanly to *any* open source Rust project. Pick a small Rust crate you use — there are thousands — find an issue labeled `good-first-issue`, and contribute there. The learning is the same.

## What the Guild Will Be

As the community grows, the picture gets richer:

- A real-time chat server (most likely Discord, possibly Matrix) with dedicated channels for `#review`, `#help`, `#showcase`, and phase-specific discussion.
- A published directory of apprentice portfolios, sortable by phase and project type.
- A mentorship matching system that pairs new apprentices with journeymen.
- A populated guild-toolkit repository with a steady flow of issues calibrated for each phase.
- A journeyman review board that issues the Journeyman certificate after a formal portfolio review.

When those pieces come online, this chapter will be updated with the actual URLs, invite links, and onboarding steps. Until then, the curriculum works end-to-end on the self-directed workflow described above.

## How to Check for Updates

The curriculum repository is itself in git. When guild infrastructure lands, the updates will land here first. The habit to build:

1. Every few weeks, `git pull` in your local copy of the learning path repository.
2. Check the CHANGELOG.md for any entries that mention the guild, review, or community.
3. Re-read this chapter if it's been updated.

That's it. The curriculum will tell you when there's a new channel to join or a new place to submit work.

## The Takeaway

"The guild" in this curriculum refers to a community that is partially built. The methodology (design, verify, get roasted, iterate) works regardless of whether that community has 5 members or 5,000. Today you participate by building in public, using AI as your adversary, and letting your portfolio speak for itself. Every reference to "the guild channel" or "submit for review" in the rest of this curriculum maps to that workflow.

You are not blocked on a community that doesn't exist yet. You're the early cohort. Build good work and it becomes the community's foundation.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Git: Just Enough](05-git-just-enough.md) | **The Guild** | [How Agents Think →](../01-talking-to-agents/01-how-agents-think.md) |

# The Guild: What It Is and How to Reach It

## Read This Before You Go Looking

Throughout this curriculum you'll see references to **the guild**. The guild channel. The guild community. The guild toolkit. Submitting your work to guild reviewers. Finding mentors in the guild. That language will make more sense with some plain-language context.

This chapter tells you what the guild actually is right now, what it aspires to be, and exactly how you participate in the parts that exist today. No mystery, no hidden prerequisites.

## The Current State

The guild is a community of apprentices, journeymen, and masters learning to direct AI agents to build software. It is a young project, but the community infrastructure is live: there is a Discord server with dedicated channels for apprentice discussion, adversarial review submissions, methodology conversation, Claude skills, and prompt engineering. A toolkit repository with apprentice-friendly issues, a formal mentorship program, and a certificate-granting portfolio board are still being built in the open.

This is not a problem you need to solve. It's context so that when the curriculum says "submit your work in the guild channel," you know exactly which channel to post in today, and what to expect as the rest of the community grows.

## The Guild Discord

The guild's real-time home is a Discord server. You join it the same way you join any Discord: click the invite, sign in, accept the rules.

**Invite link:** [https://discord.gg/kfM6Q4UBbM](https://discord.gg/kfM6Q4UBbM)

Once you're in, the channels that matter for an apprentice are:

- **#apprentice-level** — General discussion for people working through this curriculum. Ask questions, share what you're stuck on, post your design docs for feedback before you build, celebrate when something finally compiles. This is the first channel to check each day and the first one to post in when you're not sure which channel fits.
- **#adverserial-review** — Where you submit finished work for the roast. Post a link to your repo, say what you want reviewed, link your AI-adversary review history so reviewers can skip past the obvious issues. Expect specific, harsh, useful critique. This is the human counterpart to the AI-adversary workflow described below, not a replacement for it.
- **#mastering-ai-development** — Deeper conversation about the VDD/IAR methodology itself: technique, trade-offs, patterns that work and ones that don't. Architecture discussions, capstone scoping, anything that's more than a beginner's question belongs here.
- **#claude-skills** — Sharing and discussing Claude Code skills: custom workflows packaged as skill files in `.claude/`. Post skills you've written, ask for help improving one, grab skills other people have shared. Most useful once you've reached Phase 3's Working with APIs chapter.
- **#prompt-magic** — Prompt engineering. Techniques for intent, context, decomposition, and adversarial framing. Share prompts that worked unusually well and ask for help on ones that didn't. Pairs directly with Phase 1.

When a chapter in this curriculum tells you to "share it in the guild channel," it means one of these. The chapters that send you to a specific channel will say so by name.

## What You Use Today

Here is how you participate in each piece of the guild *right now*, using only tools you already have or will set up in this phase.

### Your "adversarial review channel" today: the AI adversary (plus #adverserial-review)

Adversarial review is the core of the methodology. The curriculum describes submitting your work to the community channel where experienced members will roast it — and that channel now exists at **#adverserial-review** in the Discord. Post there as soon as you have something finished.

That said, the community is still growing, so you will often want faster feedback than the queue in #adverserial-review can provide. For that, your default reviewer is **a second AI conversation configured to be hostile**.

This actually works very well. The AI adversary is patient, available at 3am, doesn't get tired, and will produce pages of specific critique on demand. The workflow:

1. Finish a piece of work (a chapter exercise, a project layer, a full build).
2. Open a **new, clean conversation** with your agent — not the same conversation you used to build the thing. This matters. The adversary should not have the builder's context.
3. Paste your design document, your code, and your process notes.
4. Give the adversary its role explicitly. A prompt like:

   > "You are an adversarial reviewer. Your job is to find every weakness, bug, edge case, missing validation, unclear error message, inconsistent naming, security vulnerability, and documentation gap in the work below. Be specific and harsh. Cite file names and line numbers where you can. Do not soften your critique. Do not add compliments. Assume the person who wrote this is strong enough to hear the truth and fix it. Here is the work: [paste]."

5. Read the response all the way through before reacting (re-read the Forward if you need the reminder on why).
6. Address the valid critiques, push back on the noise, and document both in your PROCESS.md.

You can stack this with a second, differently-framed adversary — one prompt focused on security, another on user experience, another on code organization — and aggregate their feedback. The AI adversary is free and scales to as many reviews as you want to run.

Once you've run your AI passes and addressed the valid critiques, post the result to **#adverserial-review** with a link to your repo and to the AI review history. Human reviewers in the channel can then skip past the obvious and go deeper than the AI could.

### Your "guild community" today: the Discord plus the public GitHub portfolio

The community has two entry points, and they reinforce each other.

The **Discord** is where conversation happens in real time. Questions in #apprentice-level, methodology discussion in #mastering-ai-development, work submitted for critique in #adverserial-review. If you have a question or want a quick second opinion, this is where to go.

The **public GitHub portfolio** is the durable artifact. Every project you build is tracked in git and pushed to a public GitHub repository. When someone finds your `guild-portfolio` repo, they can read your design docs, your commits, your process notes, and your AI-adversary review history. That visibility is how peers find your work outside the chat window, and how future employers or collaborators evaluate what you can actually do.

Both matter. The Discord is the conversation; the portfolio is the proof. Building in public across both is itself guild participation.

### Your "mentors" today: the people already around you

Formal mentorship pairing isn't set up yet. In the meantime, mentors come from four places:

1. **The Discord.** Post a specific question in #apprentice-level or #mastering-ai-development and someone further along will often answer. Asking a well-formed question in public is how you find the people worth learning from.
2. **Anyone further along than you, offline.** A friend who already codes, a coworker who builds software, a family member with technical experience — if they're willing to look at a piece of your work and tell you what they notice, they're a mentor for that review. You don't need a title to be useful to a beginner.
3. **The AI adversary.** A well-prompted AI reviewer is a kind of mentor: it will explain *why* something is wrong, not just that it is, and will answer follow-up questions. Treat it as a tireless tutor.
4. **Other apprentices building the same curriculum.** When you find another apprentice's public portfolio (or meet them in the Discord), you can read their work, learn from their mistakes, and compare notes on what's working. Peer learning is real learning.

### Your "guild toolkit" today: your own portfolio projects

Phase 3 includes a Workshop chapter built around contributing to the guild's shared toolkit repository. The toolkit is a work in progress. If the repository referenced in that chapter doesn't yet exist or hasn't been populated with apprentice-friendly issues, the chapter's skills (reading existing code, working within constraints, the PR process) transfer cleanly to *any* open source Rust project. Pick a small Rust crate you use — there are thousands — find an issue labeled `good-first-issue`, and contribute there. The learning is the same.

## What the Guild Will Be

The Discord is live. The rest is still in progress. As the community grows, the picture gets richer:

- A published directory of apprentice portfolios, sortable by phase and project type.
- A mentorship matching system that pairs new apprentices with journeymen, built on top of the existing Discord.
- A populated guild-toolkit repository with a steady flow of issues calibrated for each phase.
- A journeyman review board that issues the Journeyman certificate after a formal portfolio review.
- Additional Discord channels as the community identifies new topics worth their own space.

When those pieces come online, this chapter will be updated with the actual URLs and onboarding steps. Until then, the curriculum works end-to-end on the Discord plus the self-directed workflow described above.

## How to Check for Updates

The curriculum repository is itself in git. When guild infrastructure lands, the updates will land here first. The habit to build:

1. Every few weeks, `git pull` in your local copy of the learning path repository.
2. Check the CHANGELOG.md for any entries that mention the guild, review, or community.
3. Re-read this chapter if it's been updated.

That's it. The curriculum will tell you when there's a new channel to join or a new place to submit work.

## The Takeaway

"The guild" in this curriculum refers to a community that is partially built. The Discord is live — that is where the conversation happens now — and the methodology (design, verify, get roasted, iterate) works regardless of whether that community has 50 members or 5,000. Today you participate by joining the Discord, building in public, using AI as your adversary for fast feedback, submitting finished work to #adverserial-review, and letting your portfolio speak for itself over time. Every reference to "the guild channel" or "submit for review" in the rest of this curriculum maps to one of the Discord channels listed above.

You are not blocked. You're the early cohort. Build good work and it becomes the community's foundation.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Git: Just Enough](05-git-just-enough.md) | **The Guild** | [How Agents Think →](../01-talking-to-agents/01-how-agents-think.md) |

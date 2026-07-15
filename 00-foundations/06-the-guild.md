# The Guild: What It Is and How to Reach It

## Read This Before You Go Looking

Throughout this curriculum you'll see references to **the guild**. The guild channel. The guild community. The guild toolkit. Submitting your work to guild reviewers. Finding mentors in the guild. That language will make more sense with some plain-language context.

This chapter tells you what the guild actually is right now, what it aspires to be, and exactly how you participate in the parts that exist today. No mystery, no hidden prerequisites.

## The Current State

The guild is a young community learning to direct AI agents to build software. The Discord server is live, and the public [guild-toolkit repository](https://github.com/Navigators-Guild/guild-toolkit) now contains Rust workspace code and open contribution issues. Formal mentorship, badge issuance, and a certificate-granting portfolio board are still proposed infrastructure; do not assume they are available until this chapter links to a live process.

This is not a problem you need to solve. It's context so that when the curriculum says "submit your work in the guild channel," you know exactly which channel to post in today, and what to expect as the rest of the community grows.

## The Guild Discord

The guild's real-time home is a Discord server. You join it the same way you join any Discord: click the invite, sign in, accept the rules.

**Invite link:** [https://discord.gg/kfM6Q4UBbM](https://discord.gg/kfM6Q4UBbM)

Once you're in, the channels that matter for an apprentice are:

- **#apprentice-level** — General discussion for people working through this curriculum. Ask questions, share what you're stuck on, post your design docs for feedback before you build, celebrate when something finally compiles. This is the first channel to check each day and the first one to post in when you're not sure which channel fits.
- **#adversarial-review** — Where you can request review of finished work. Post an authorized link, say what you want reviewed, and summarize checks and earlier findings. Ask for specific, evidence-based, respectful critique.
- **#mastering-ai-development** — Deeper conversation about the VDD/IAR methodology itself: technique, trade-offs, patterns that work and ones that don't. Architecture discussions, capstone scoping, anything that's more than a beginner's question belongs here.
- **#claude-skills** — Sharing and discussing Claude Code skills. Inspect community packages and use the current Claude Code documentation for their required directory and file structure; those details can change. Most useful once you've reached Phase 3's Working with APIs chapter.
- **#prompt-magic** — Prompt engineering. Techniques for intent, context, decomposition, and adversarial framing. Share prompts that worked unusually well and ask for help on ones that didn't. Pairs directly with Phase 1.

When a chapter in this curriculum tells you to "share it in the guild channel," it means one of these. The chapters that send you to a specific channel will say so by name.

Discord channel names and permissions are not visible through the public invite page. This list reflects the curriculum's current community configuration; after joining, use the server's live channel list and rules if they differ.

## What You Use Today

Here is how you participate in each piece of the guild *right now*, using only tools you already have or will set up in this phase.

### Your review workflow today: an AI pass plus #adversarial-review

Adversarial review is central to the methodology. The **#adversarial-review** Discord channel exists for peer feedback. State the project's maturity, what you want reviewed, and what access or confidentiality limits apply; do not assume every participant is an experienced or authorized reviewer.

That said, the community is still growing, so you may want faster feedback than the queue in #adversarial-review can provide. Use **a separate AI review context with a specific checklist** as one input—not as a substitute for tests or qualified human review.

An AI reviewer is available within your product's quotas and can generate useful hypotheses quickly. It can also miss defects, invent findings, or share the builder's blind spots. The workflow:

1. Finish a piece of work (a chapter exercise, a project layer, a full build).
2. Open a **new conversation** with your agent. This can reduce anchoring on the build exchange, but it does not make the model independent; provide the requirements and evidence it needs.
3. In an environment authorized for the material, attach or point it to the design document, relevant code, process notes, and test results. Redact secrets and sensitive data.
4. Give the adversary its role explicitly. A prompt like:

   > "Review this work against the attached design and acceptance criteria. Check behavior, error handling, tests, security boundaries, accessibility, naming, and documentation where relevant. For every finding, cite a file and line, explain impact, give confidence, and propose a reproduction or test. Separate confirmed defects from questions and optional improvements. Do not modify the work."

5. Read the response all the way through before reacting (re-read the Foreword if you need the reminder on why).
6. Address the valid critiques, push back on the noise, and document both in your PROCESS.md.

You can use separate, differently framed reviews—security, user experience, or code organization—and aggregate the findings. Stop when additional review cost exceeds the risk reduction, and stay within plan, privacy, and rate limits. More generated critique is not automatically more evidence.

Once you've run the relevant checks and addressed confirmed findings, post the result to **#adversarial-review** with an authorized link and a concise review summary. This lets peers focus on unresolved questions rather than repeating known findings.

### Your "guild community" today: Discord plus a shareable GitHub portfolio

The community has two entry points, and they can reinforce each other.

The **Discord** is where conversation happens in real time. Questions in #apprentice-level, methodology discussion in #mastering-ai-development, work submitted for critique in #adversarial-review. If you have a question or want a quick second opinion, this is where to go.

The **GitHub portfolio** is the durable artifact. Track each project in git. Publish only reviewed material that contains no secrets, sensitive data, employer or client code, or content you lack permission to share. A private repository can be shared with named reviewers; a public portfolio can help others discover the work.

The Discord supports conversation; the portfolio preserves inspectable evidence. Public participation is useful but does not override privacy, confidentiality, or consent.

### Your mentorship and review help today

Formal mentorship pairing isn't set up yet. In the meantime, seek help from several sources:

1. **The Discord.** Post a specific question in #apprentice-level or #mastering-ai-development and someone further along will often answer. Asking a well-formed question in public is how you find the people worth learning from.
2. **Anyone further along than you, offline.** A friend who already codes, a coworker who builds software, a family member with technical experience — if they're willing to look at a piece of your work and tell you what they notice, they're a mentor for that review. You don't need a title to be useful to a beginner.
3. **An AI review aid.** A fresh agent context can explain possible issues and answer follow-up questions. Verify its claims and do not treat availability, confidence, or generated volume as expertise.
4. **Other apprentices building the same curriculum.** When you find another apprentice's public portfolio (or meet them in the Discord), you can read their work, learn from their mistakes, and compare notes on what's working. Peer learning is real learning.

### Your "guild toolkit" today: the public repository

Phase 3's Workshop chapter uses the public [Navigators-Guild/guild-toolkit](https://github.com/Navigators-Guild/guild-toolkit) repository, which has open implementation, documentation, testing, and CI issues. Read its current README, contribution guidance, issue status, and CI before choosing work; those live artifacts take precedence over this curriculum's snapshot. If no issue matches your level, practice the same workflow on another maintained Rust project rather than creating unrequested changes.

## What the Guild Will Be

The Discord and toolkit repository are live. The following community and credential systems are still proposals:

- A published directory of apprentice portfolios, sortable by phase and project type.
- A mentorship matching system that pairs new apprentices with journeymen, built on top of the existing Discord.
- Maintainer triage and onboarding that calibrate the existing guild-toolkit issue backlog by experience level.
- A journeyman review board that issues the Journeyman certificate after a formal portfolio review.
- Additional Discord channels as the community identifies new topics worth their own space.

When those pieces come online, this chapter will be updated with the actual URLs and onboarding steps. Until then, the curriculum works end-to-end on the Discord plus the self-directed workflow described above.

## How to Check for Updates

The curriculum repository is itself in git. When guild infrastructure lands, the updates will land here first. The habit to build:

1. Every few weeks, `git pull --ff-only` in a clean local copy of the learning path repository.
2. Check the CHANGELOG.md for any entries that mention the guild, review, or community.
3. Re-read this chapter if it's been updated.

That's it. The curriculum will tell you when there's a new channel to join or a new place to submit work.

## The Takeaway

"The guild" in this curriculum refers to a community whose Discord and toolkit are live while formal mentoring and credentials remain planned. You can participate by joining the Discord, keeping an inspectable portfolio, using AI review as one imperfect input, and requesting peer feedback in #adversarial-review. Share publicly only when the material is safe and authorized. Channel names and processes should be checked against the live server.

You are not blocked. You're the early cohort. Build good work and it becomes the community's foundation.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Git: Just Enough](05-git-just-enough.md) | **The Guild** | [How Agents Think →](../01-talking-to-agents/01-how-agents-think.md) |

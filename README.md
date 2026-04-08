# The Guild Learning Path

**A structured path from zero to agentic AI practitioner.**

You want to build things with AI. Real things: tools you'll use, projects you can show, skills that make you more capable than you were before. This path gets you there.

Whether you're a complete beginner, a student supplementing your coursework, or a working professional adding agentic development to your skillset, the core of this program is the same: **build real projects, get honest feedback, and improve through iteration.** By the end, you'll have a portfolio of working software and the skills to keep building on your own.

This learning path is built on a methodology called **Verification Driven Development via Iterative Adversarial Refinement (VDD/IAR)**. In plain language: define what success looks like *before* you build, use AI agents to build it, stress-test the results, and improve through honest critique. Every phase practices that loop.

The guild's default language is **Rust**. Not because it's the easiest, but because its compiler enforces correctness in ways that align with our methodology. The agent handles the syntax. You handle the thinking.

**Before you start, read the [Forward](FORWARD.md).** It's about ego, failure, and why being wrong is how you learn to be right.

---

## How This Path Works

This is a guild. You advance by **showing your work**. Each phase builds on the last, and you earn recognition at every milestone.

There are three tiers:

**Apprentice** - You learn to direct agents and verify their output. You build real things with guidance, submit your work for adversarial review, and learn from the feedback.

**Journeyman** - You run full VDD cycles on your own. You architect solutions, set verification criteria upfront, stress-test through adversarial refinement, and handle complex multi-step workflows. Your portfolio shows not just what you built but *how* you built it.

**Master** - You contribute back. You mentor apprentices, develop new techniques, push into new territory. Your body of work speaks for itself.

This repository contains the **Apprentice Learning Path**: everything you need to go from "I've never touched code" to "I can build real things with AI agents and prove it."

---

## The Apprentice Path

### Phase 0: Foundations
*What you need to understand before you start building.*

1. [The New Literacy](00-foundations/01-the-new-literacy.md) - Why directing agents is the skill that matters now
2. [What Code Actually Is](00-foundations/02-what-code-actually-is.md) - A mental model, not a syntax lesson
3. [The Language Landscape](00-foundations/03-the-language-landscape.md) - Programming languages in conceptual terms
4. [Your Workspace](00-foundations/04-your-workspace.md) - Setting up the tools you'll use every day
5. [Git: Just Enough](00-foundations/05-git-just-enough.md) - How to save, share, and track your work
6. [The Guild](00-foundations/06-the-guild.md) - What "the guild" actually is and how you participate today

### Phase 1: Talking to Agents
*How to communicate with AI so it builds what you actually want.*

1. [How Agents Think](01-talking-to-agents/01-how-agents-think.md) - What's happening on the other side
2. [The Art of Intent](01-talking-to-agents/02-the-art-of-intent.md) - Turning vague ideas into clear directions
3. [Context Is Everything](01-talking-to-agents/03-context-is-everything.md) - What the agent needs to know and why
4. [Breaking Problems Down](01-talking-to-agents/04-breaking-problems-down.md) - The most important skill you'll learn
5. [Your First Build](01-talking-to-agents/05-first-build.md) - A guided project from design doc to working software
6. [When Things Break](01-talking-to-agents/06-when-things-break.md) - Debugging, error messages, and getting unstuck
7. [Finding Answers](01-talking-to-agents/07-finding-answers.md) - Documentation, search, and verifying what the agent tells you

### Phase 2: The Methodology
*The discipline that makes the output actually good.*

1. [How We Build](02-the-methodology/01-how-we-build.md) - VDD and the adversarial refinement loop
2. [Tracking Your Work](02-the-methodology/02-tracking-your-work.md) - Issue tracking, building your own, then using crosslink
3. [Branches and Pull Requests](02-the-methodology/03-branches-and-pull-requests.md) - The workflow for contributing to shared code

### Phase 3: Real-World Skills
*Working the way professionals work.*

1. [The Workshop](03-real-world-skills/01-the-workshop.md) - Contributing to the guild toolkit, an existing codebase
2. [Working with APIs](03-real-world-skills/02-working-with-apis.md) - MCP servers, skills, and talking to external services
3. [Project Architecture](03-real-world-skills/03-project-architecture.md) - Multi-file projects, god files, and managing complexity
4. [Security](03-real-world-skills/04-security.md) - Why agent code is insecure and how to fix it
5. [Shipping It](03-real-world-skills/05-shipping-it.md) - Testing, verification, cross-platform, and delivery

### Phase 4: Proving It
*No guides, no hand-holding. The capstone.*

1. [On Your Own](04-proving-it/01-on-your-own.md) - Your capstone project, fully self-directed
2. [Giving Back](04-proving-it/02-giving-back.md) - Mentoring a newer apprentice
3. [The Portfolio Review](04-proving-it/03-the-portfolio-review.md) - Assembling your work and the journeyman transition

---

## Projects

Each phase includes hands-on builds. The guided projects are chosen so every apprentice works on the same targets, which makes review and comparison consistent across the guild. Your self-directed projects and capstone are where you choose what to build.

| Phase | Project | Language | Why This Project |
|---|---|---|---|
| Phase 1 | Bookmark Manager | HTML/JS | Your first build. Teaches the prompting and verification loop with instant visual feedback in a browser. HTML/JS is the one exception to the Rust default because seeing a result immediately matters more than toolchain when you're starting out. |
| Phase 2 | Issue Tracker CLI | Rust | Your first Rust project. Introduces the compiler, CLI design, and structured data (state machines, serialization). You're building a tool like the one you'll use daily, so you understand issue tracking from the inside. |
| Phase 3 | Guild Toolkit | Rust | Your first time working in someone else's codebase. Teaches reading before writing, following existing conventions, the PR process, and building for an audience other than yourself. |
| Phase 3 | API + Architecture | Rust | Covered in the chapter exercises. Teaches network requests, error handling, multi-file structure, and module design. Not a single named project because these skills get practiced across multiple exercises and toolkit contributions. |
| Phase 4 | Capstone | Rust | Fully self-directed. You pick the problem, design the solution, and ship it. Must involve something unfamiliar. This is your masterpiece. |
| All | 3-5 Self-Directed | Any | Your own ideas, your own design docs, your own process. These prove you can work without a guide. |

---

## Portfolio Requirements

At the end of the Apprentice path, you should have:

- **Completed projects** demonstrating increasing complexity, tracked in git with full history
- **Design documents** for each project (generated with the agent)
- **Process documentation** showing how you directed the agent, what went wrong, and how you fixed it
- **Adversarial review history**: your submissions to the guild [Discord](https://discord.gg/kfM6Q4UBbM) **#adverserial-review** channel (and your AI-adversary reviews), the feedback you received, and how you responded to it
- **Workshop contributions**: PRs to the shared codebase, reviewed and merged
- **3-5 self-directed projects**: things you chose to build for yourself, designed and executed on your own. These don't need to be large. They need to be yours: your idea, your design doc, your process. This is where you prove you can work without a guide telling you what to build next

Your portfolio isn't just the finished code. It's the *entire journey*: the thinking, the failures, the iterations, and the final result. That's what makes it real.

---

## What You'll Walk Away With

- **Working software** you built yourself, from design to deployment
- **A public portfolio** that demonstrates your skills to employers, collaborators, and clients
- **Phase completion badges** recognizing your progress at each milestone
- **A Journeyman certificate** when you complete the full path
- **A methodology** (VDD/IAR) you can apply to any project, in any language, for the rest of your career

## Philosophy

This path fills a gap. Traditional education teaches you theory and fundamentals. That knowledge is valuable and this program builds on it. What's been missing is structured training in the practical skill of **directing intelligent systems to build things that work.** Whether you're coming from a CS degree, a bootcamp, self-teaching, or no technical background at all, this path adds a capability that didn't exist five years ago.

We ask you to build things, submit them for honest critique, and improve. The portfolio you build here is proof that can't be faked, because the whole process is visible.

Welcome to the guild.

---

## Glossary

A one-stop reference for acronyms and guild-specific terms you'll see throughout the curriculum. Each term is also defined on first use in the chapter where it appears; this is just the quick lookup.

- **VDD** — **Verification Driven Development.** The guild's core methodology: define what success looks like before you build, use agents to build it, then check the result against the definition. Covered in depth in Phase 2.
- **IAR** — **Iterative Adversarial Refinement.** The second half of the methodology: after the initial build works, stress-test it through honest critique and improve through iteration. VDD and IAR together form the full loop.
- **CLI** — **Command-Line Interface.** A program you run by typing its name in the terminal, like `git`, `cargo`, or `crosslink`, instead of clicking icons in a window.
- **PR** — **Pull Request.** A formal proposal to merge a branch of code into another branch, usually hosted on GitHub. Covered in the [Branches and Pull Requests](02-the-methodology/03-branches-and-pull-requests.md) chapter.
- **MCP** — **Model Context Protocol.** An open standard that lets AI agents connect to external services through purpose-built servers, so the agent can call tools directly instead of writing integration code each time. Covered in Phase 3.
- **CI** — **Continuous Integration.** A service (usually GitHub Actions) that automatically builds and tests your code every time you push. Covered in Phase 3 Shipping chapter.
- **PAT** — **Personal Access Token.** A limited-scope credential you generate on GitHub to authenticate from the command line, in place of your account password. Covered in the [Git: Just Enough](00-foundations/05-git-just-enough.md) chapter.
- **MSRV** — **Minimum Supported Rust Version.** The oldest version of Rust a given crate or project is tested against. You'll see this in Cargo.toml files.
- **JSON** — **JavaScript Object Notation.** A plain-text format for structured data (objects, lists, numbers, strings). Introduced in [What Code Actually Is](00-foundations/02-what-code-actually-is.md).
- **YAML** — A sibling format to JSON used for configuration files (like GitHub Actions workflows). Same kind of data, different punctuation.
- **The Guild** — The community of apprentices, journeymen, and masters using this curriculum. The [Discord server](https://discord.gg/kfM6Q4UBbM) is live with channels for apprentice discussion, adversarial review, methodology, Claude skills, and prompt engineering. Mentor matching and the toolkit are still being built. See [The Guild](00-foundations/06-the-guild.md) for the current state and how each channel maps to the curriculum.
- **The Adversary** — A reviewer (human or AI) whose job is to find every weakness in your work. Central to the IAR half of the methodology.
- **Design doc** — A short document you write (usually with agent help) that defines what you're building before any code exists. Shows up in nearly every project in the curriculum.
- **Epic / bead-string / subissue** — Issue-tracking terms from Phase 2. An epic is a large parent issue, subissues are smaller pieces of work that roll up to it, and "bead-string" is the guild's name for the decomposition pattern where you chain small verified pieces into a larger working whole.

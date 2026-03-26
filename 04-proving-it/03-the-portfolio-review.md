# The Portfolio Review

## The Masterpiece

In the medieval guilds, an apprentice ended their apprenticeship by producing a "masterpiece," a single work that demonstrated competence across the trade's core skills. It wasn't called a masterpiece because it was perfect. It was called that because it was submitted to the masters for judgment. The work spoke for itself.

Your portfolio is your masterpiece. Not a single project, but the collected evidence of your journey: everything you built, how you built it, what you learned, and what you gave back. You assemble it, you submit it, and it speaks for itself.

## What You're Assembling

Your portfolio should contain:

### The Guided Projects

- **Bookmark manager** (Phase 1) - Your first build. Design doc, code, process documentation.
- **Issue tracker** (Phase 2) - Your first Rust project. Design doc, code, tests, process documentation.

These show your starting point. Evaluators aren't looking for perfection here. They're looking for evidence that you followed the process, verified your work, and responded to feedback.

### Workshop Contributions

Your PRs to the guild toolkit. The code you contributed, the reviews you received, how you addressed feedback. This shows you can work within an existing codebase and collaborate with others.

### Self-Directed Projects

The 3-5 projects you built on your own. Each should have:
- A design doc
- The code in a git repo with meaningful commit history
- Tests
- Process documentation showing your VDD cycle
- A README that someone else could follow

These show that you can work without a guide. The choice of problems, the scope decisions, the design trade-offs: all of this reveals your judgment, which is the thing that separates someone who follows instructions from someone who can work independently.

### The Capstone

Your Phase 4 project. The full package: design doc, tracked issues, layered build, adversarial review history, security review, tests, shipped deliverable, retrospective. This is the centerpiece. It shows everything working together at the highest level you've reached.

### The Mentoring Reflection

Your document from the Giving Back chapter. Evidence that you can transfer knowledge, not just hold it.

### The Adversarial Review History

Across all your projects: the roasts you received, the feedback you responded to, the iterations. This is the evidence that your work improved through honest critique, not just through building in isolation.

## How to Submit

Organize your portfolio as a GitHub repository (or a collection of repositories linked from one index). The structure should be navigable. Someone who's never met you should be able to understand your journey by reading through it in order.

A simple structure:

```
guild-portfolio/
├── README.md              # Overview, table of contents, your story
├── 01-bookmark-manager/   # or link to repo
├── 02-issue-tracker/      # or link to repo
├── 03-workshop/           # links to your toolkit PRs
├── 04-self-directed/      # links to your project repos
│   ├── project-1/
│   ├── project-2/
│   └── ...
├── 05-capstone/           # or link to repo
└── 06-mentoring.md        # your mentoring reflection
```

Your portfolio README should tell your story. Not a resume. A narrative. When you started, what you knew (or didn't), what was hard, what clicked, what you're proud of, where you want to go next. Two to three paragraphs. Reviewers read dozens of these. The ones that are honest and specific stand out. The ones that are generic and polished don't.

## The Review Process

Your portfolio is reviewed by **two guild journeymen or masters** who have completed the path themselves. They review independently, then compare notes. This isn't a faceless committee. You'll know who your reviewers are, and they'll know you from the guild community.

The review takes about a week. Reviewers read your design docs, look at your code and commit history, check your test coverage, read your retrospectives, and look at your Chainlink issue history. They write up feedback covering strengths, areas for improvement, and a recommendation.

There's no numerical score or letter grade. The recommendation is one of three outcomes:

- **Ready.** Your work demonstrates journeyman-level competence. You advance.
- **Almost there.** Your work is strong in most areas but has specific gaps. You get detailed feedback on what to strengthen and can resubmit.
- **More time needed.** You need more practice in fundamental areas. You get guidance on which phases to revisit. This isn't a judgment on you. It's a signal that the process needs more time.

## What Reviewers Look For

The review is holistic, not a checklist. But here's what matters most:

### Process Over Product

A simple tool built with impeccable process (clear design doc, tracked issues, thorough testing, honest retrospective) ranks higher than a complex tool built chaotically. The guild cares about *how* you work, not just what you produce. Products are temporary. Process is permanent.

### Growth Over Perfection

Evaluators read your early work and your later work. They want to see growth. Your bookmark manager should look rougher than your capstone. Your early design docs should be less thorough than your later ones. If everything looks the same quality, you either started very strong or you didn't improve. Visible growth is a good sign.

### Honest Self-Assessment

Your retrospectives and process docs should be honest about what went wrong. "Everything went perfectly" is a red flag. Real projects have problems. The question is whether you recognized them, learned from them, and adapted. Admitting "I scoped this too ambitiously and had to cut features" shows better judgment than pretending everything went according to plan.

### Independence

Your self-directed projects and capstone show whether you can work without someone telling you what to do. Evaluators look at your problem selection (is it a real problem or a tutorial in disguise?), your scope decisions (is it realistic?), and your ability to unstick yourself when things go wrong.

### Generosity

Your mentoring reflection and your PR reviews on other people's work show whether you can give back. A journeyman who can only build things for themselves is less valuable than one who can also elevate the people around them.

## After the Review

If the evaluation goes well, you're a journeyman. What changes:

- You receive your **Journeyman certificate** from the guild
- You're trusted to run full VDD cycles on real guild projects independently
- You can mentor apprentices as an official part of the guild structure
- You have a seat in guild discussions about methodology, tooling, and direction
- Your portfolio URL becomes a professional credential that demonstrates your capabilities

If the evaluation suggests you need more work, you'll get specific feedback about what to strengthen. This isn't failure. It's the adversarial refinement loop applied to your own development. Fix what's identified, improve what's suggested, and submit again.

## Recognition

The guild recognizes your progress at every stage. You earn badges for completing each phase:

- **Phase 0: Foundation Set** - You've set up your tools and understand the landscape
- **Phase 1: First Build** - You've built working software with an agent
- **Phase 2: Methodology** - You've practiced VDD and issue tracking
- **Phase 3: Real-World Ready** - You've contributed to a shared codebase, handled APIs, security, and shipping
- **Phase 4: Journeyman** - You've completed the capstone, mentored someone, and submitted your portfolio

These are real markers of real accomplishment. Display them, share them, be proud of them. You earned each one by doing the work.

## What Your Credential Is (and Isn't)

Let's be honest about where this stands.

**Right now,** the guild is new. An HR recruiter at a large company has never heard of it. Your Journeyman certificate won't get past a keyword-scanning resume filter. That's the reality of any new credential, and pretending otherwise would be dishonest.

**What your portfolio does right now** is prove your skills to anyone who actually looks at the work. A technical hiring manager, a potential collaborator, an open source maintainer, anyone who clicks through your repos and reads your process documentation will see evidence of real capability that can't be faked. That's immediately valuable in contexts where people evaluate your work directly.

**What the certificate does** is mark your achievement within the guild. It says you completed a rigorous process, were reviewed by peers, and met the standard. As more guild members enter the workforce and perform well, that marker builds external reputation.

**Over time,** credentials gain recognition the same way they always have: the people who hold them turn out to be consistently good at their jobs. CompTIA, AWS, and Cisco certifications weren't prestigious when they started either. They built credibility over years because certified people performed. The guild is on the same path, and you're part of building that reputation.

So you have two things: a certificate that marks your achievement and a portfolio that proves it. The certificate will gain recognition as the guild grows. The portfolio works right now, for anyone willing to look. Together, they're stronger than either alone.

You started this path with the ability to think and communicate. You end it with a body of work that proves you can direct intelligent systems to build things that work, and the process discipline to do it reliably. Everything else you'll learn on the job, because you've proven you know how to learn.

Welcome to the journeymanship.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Giving Back](02-giving-back.md) | **The Portfolio Review** | |

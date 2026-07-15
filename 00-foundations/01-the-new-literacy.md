# The New Literacy

## What This Path Is For

You have an idea for something you want to build. Maybe it's a tool for your job, a side project, a small business website, or something you've been imagining for years but didn't have the technical skills to make real. This path teaches you how to make it real, using AI agents as your building partner.

You will not begin by memorizing syntax. An AI agent can draft code quickly, but it may use the wrong version, invent an API, or produce code that compiles but behaves incorrectly. You will learn enough syntax and tooling to inspect changes while emphasizing clear thinking, communication, and verification.

If you have a traditional CS background, this adds a new capability on top of what you already know. If you're coming from a bootcamp, this fills in the methodology side. If you have no technical background at all, this is an on-ramp. The intended outcome is the same: practice directing AI agents to build software and assemble a portfolio whose claims can be checked.

## What You Are Learning

The skill you're developing here has a few components. The curriculum is not centered on memorizing punctuation, but basic code reading grows alongside these skills:

**Intent articulation** - taking a fuzzy idea in your head ("I want a tool that tracks my habits") and turning it into a clear, specific description that an agent can act on. This is harder than it sounds. Most people overestimate how clear their ideas are until they try to explain them to something that takes instructions literally.

**Verification** - deciding whether the result actually meets the requirement. Start by defining "working correctly," then inspect the diff at a level proportionate to risk, run tests and static checks, exercise the behavior, and record limitations. You will gradually learn to read more of the code you ship. This is the core of VDD (Verification Driven Development).

**Decomposition** - breaking a big, complex problem into smaller, manageable pieces. Agents work best with clear, scoped tasks. "Build me a business" is useless. "Create a landing page with a signup form that stores email addresses" is actionable. Learning to decompose is learning to think in steps.

**Adversarial thinking** - asking "how could this break?" and "what did I miss?" before someone else finds those problems. This is the refinement part of Iterative Adversarial Refinement. One successful run is weak evidence; completion depends on explicit acceptance criteria, relevant checks, and documented residual risk.

**Iteration discipline** - the willingness to evaluate feedback, extract what is supported by evidence, and improve. Specific, respectful critique is more useful than praise or performative harshness.

## The Director Mental Model

Think of yourself as a film director. You do not perform every specialist role, but you need enough technical literacy to ask good questions, recognize risk, and evaluate evidence. You hold the vision, communicate it, review the work, and remain accountable for the result.

A bad director says "make it good" and hopes for the best. A good director says "I need the audience to feel tension in this scene. The lighting should be low, the music should be minimal, and the camera should stay close on the actor's face." The second director gets what they want because they articulated their intent with enough specificity for the specialists to execute.

You're learning to be a good director of AI agents. Their capabilities vary by tool, task, context, and permissions, and none can read your mind. Your job is to bridge the gap between your intent and an implementation you can inspect.

## What This Looks Like in Practice

Here's a concrete example of the difference.

**Without these skills:**

> "Hey, make me a website for my dog walking business."

The agent builds *something*. It has a generic layout, placeholder text, stock images. It technically is a website. It has nothing to do with your specific business, your neighborhood, your pricing, your personality. You look at it and think "that's not what I wanted" but you can't articulate what's wrong.

**With these skills:**

> "I run a dog walking business in the Ballard neighborhood of Seattle. I need a single-page website that does three things: shows my services and prices (30-minute walk $20, 60-minute walk $35, puppy visits $25), lets people book a walk by picking a date and time, and shows testimonials from three clients I'll provide the text for. The tone should be warm and friendly, not corporate. I want it to feel like a neighbor offering to help, not a company selling a service."

The agent has a more specific brief. You still need to clarify where bookings are stored, how conflicting slots are prevented, what personal data is collected, and whether a static page can support the workflow. The detailed prompt improves the starting point; it does not replace design or verification.

The difference isn't technical knowledge. It's clarity of thought and specificity of communication.

## What You'll Build

This isn't theoretical. The path asks you to produce:

- **A bookmark manager** you built from scratch in your first week
- **A command-line tool** written in Rust
- **A submitted contribution to a shared open-source project**, with review history whether or not maintainers merge it
- **3-5 projects of your own choosing** that solve problems you actually care about
- **A capstone project** that demonstrates everything you've learned

Keep it in a shareable portfolio with full history: the design documents, the code, the testing, the feedback you received, and how you responded to it. Make repositories public only when their contents are safe and appropriate to share. This is not a certificate; it is a body of evidence a reviewer can inspect.

## What Comes Next

In the rest of Phase 0, you'll set up the basic tools you need: an editor, terminal, coding agent, language toolchains, and git for tracking your work. Think of it as setting up your workshop before you start building.

Then in Phase 1, you'll start talking to agents and build a small browser project, recording the checks you used to decide whether it works.

You have enough to start. The rest of the path builds the technical judgment needed to tell the difference between a convincing demo and dependable software.

**One last heads-up before you start.** You'll see references to "the guild," "the guild channel," and "guild reviewers" throughout this curriculum. The guild is a real community, and its home is a [Discord server](https://discord.gg/kfM6Q4UBbM) with channels for apprentice discussion, adversarial review, methodology, Claude skills, and prompt engineering. A few other pieces of the community infrastructure are still being built. [The Guild chapter](06-the-guild.md) at the end of Phase 0 explains exactly what exists today, which channel maps to which curriculum reference, and how to join. You don't need to read it this second, but do read it before Phase 1 so the later references make sense.

Let's go.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Foreword](../FOREWORD.md) | **The New Literacy** | [What Code Actually Is →](02-what-code-actually-is.md) |

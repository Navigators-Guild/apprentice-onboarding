# Context Is Everything

## The Invisible Factor

You can write the most specific prompt in the world and still get bad results if the agent doesn't have the right context. Context is everything the agent needs to know *around* your request: the background, constraints, prior decisions, and environmental details that shape what "correct" looks like.

Think of it this way: if you tell a chef "make me pasta," the result depends entirely on context the chef knows or doesn't know. Are you in Italy or a hospital cafeteria? Is it for a romantic dinner or a child's birthday? Are you allergic to anything? Do you have twenty minutes or two hours? The word "pasta" is the same, but the right answer is completely different depending on context.

Agents have zero context unless you provide it. Every conversation starts as a blank slate. The agent doesn't know what you built yesterday, what project you're working on, what technologies you've already chosen, or what your goals are. You have to establish all of that, every time.

## The Four Types of Context

### 1. Project Context

This is the big picture: what are you building and why? A design document handles this well, which is why it's the first step in our methodology. But even without a formal design doc, you should open every work session by grounding the agent in the project.

**Without project context:**
> "Add a search feature."

The agent doesn't know what it's searching through, what the existing interface looks like, what technology the project uses, or where the search bar should go. It'll build *something*, probably a generic search box with no connection to your actual project.

**With project context:**
> "I'm building a recipe collection app. It's a single-page web app using HTML and JavaScript. Currently it displays recipes as cards in a grid. I need to add a search bar at the top that filters the recipe cards in real time as the user types, matching against recipe names and ingredient lists."

Same request, completely different result. The agent now knows the technology, the current state of the interface, and exactly how the search should behave.

### 2. Technical Context

This is information about the tools, languages, and setup you're working with. If you've been building a project, the agent needs to know what's already there.

The most effective way to provide technical context is to share the actual files. If you're using Claude Code or Cursor, the agent can see your project files directly. If you're using a chat interface like claude.ai, you can paste relevant code or file contents into the conversation.

**Good technical context looks like:**
> "Here's my current index.html file: [paste file]. I'm using vanilla JavaScript, no frameworks. The styles are in a separate styles.css file. I need to add a feature to this existing page."

**Missing technical context causes problems like:**
The agent creates a React component when your project uses plain HTML. Or it writes code that conflicts with code that already exists. Or it suggests installing a tool that's incompatible with your operating system. These aren't the agent's fault. It literally didn't know.

### 3. Constraint Context

These are boundaries and requirements that aren't part of the feature itself but affect how it should be built.

Examples of constraints that matter:

- "This needs to work offline. Users won't always have internet."
- "The audience is elderly users who aren't comfortable with small text or complex navigation."
- "This is a personal project, so security can be simple. No need for enterprise-grade authentication."
- "I'm hosting this for free on GitHub Pages, so it can only be a static site. No server-side code."
- "This needs to load fast on slow mobile connections."
- "I'm colorblind, so don't rely on red/green color differences to convey information."

Any constraint you know about but don't mention is a constraint the agent will likely violate. Tell the agent about your constraints *before* it starts building.

### 4. Preference Context

These are your personal preferences about style, behavior, and approach. Unlike constraints (which are hard requirements), preferences are softer but still important for getting output you're happy with.

- "I prefer minimal interfaces. I'd rather have fewer features that are easy to find than more features crammed into the screen."
- "When you write commit messages, use present tense ('Add search bar' not 'Added search bar')."
- "I like descriptive variable names in code. Use `numberOfCompletedTasks` not `n` or `count`."
- "When something goes wrong, show a friendly error message, not a technical one. Something like 'Hmm, that didn't work. Try again?' not 'Error 500: Internal Server Error.'"

Preferences help the agent match your taste. Without them, the agent uses its defaults, which are reasonable but not personalized.

## The Design Document as Context Anchor

In the guild's methodology, every project starts with a design document. This isn't bureaucracy. It's a practical tool for context management. A good design doc contains all four types of context in one place:

- **Project context:** What you're building and why
- **Technical context:** What technology you're using, what already exists
- **Constraint context:** What the boundaries are
- **Preference context:** How you want it to look and feel

When you start a new conversation with an agent (or when the conversation gets long and you need to reset), you paste the design doc and say "here's the project I'm working on." The agent instantly has everything it needs. No twenty-message back-and-forth to re-establish what's going on.

This is why the first step in our workflow is generating a design doc with the agent. It forces you to articulate context before you start building, and it creates a reusable artifact that keeps every subsequent conversation grounded.

## Context Over the Life of a Conversation

As a conversation progresses, context accumulates. The agent remembers what you've discussed in *this* conversation. But context also decays. In very long conversations, earlier details become less reliable. Here's how to manage this:

**The first message sets the stage.** Make it count. Provide project context, share relevant files, state your goal for this session. Don't open with "hey" and then drip-feed information across ten messages. Front-load the context.

**Periodically restate critical details.** If you're fifty messages into a conversation and you're about to ask for something that depends on a decision from message three, restate that decision. "Earlier we decided the navigation should be at the top, not in a sidebar. With that in mind, can you..."

**Use summaries as checkpoints.** Every so often, ask the agent to summarize what it understands about the project's current state. If the summary is wrong, correct it. This catches context drift before it causes problems.

**Start fresh when it makes sense.** There's no shame in opening a new conversation. If things are getting confused, a clean start with a good design doc is faster than untangling a muddled thread.

## The Context Checklist

Before sending a prompt that asks the agent to build or change something, scan through this list:

- Does the agent know what project this is? (Project context)
- Does the agent know what already exists? (Technical context)
- Does the agent know what constraints apply? (Constraint context)
- Does the agent know my preferences for style and behavior? (Preference context)
- Have I shared the relevant files or file contents?
- Have I restated any earlier decisions that affect this request?

You won't go through this formally every time. With practice, it becomes instinctive. But when something goes wrong and you're not sure why, come back to this checklist. More often than not, the answer is a missing piece of context.

## Exercises

1. Take one of the prompts you wrote in the previous chapter's exercises. Now write the context you would need to provide alongside it. What project context, technical context, constraints, and preferences would the agent need?

2. Start a conversation with an agent. Give it zero context and ask it to "add a dark mode toggle." Note what it produces. Then start a new conversation, provide full context about a specific project, and make the same request. Compare the results. This exercise shows the impact of context better than any explanation can.

3. Write a one-paragraph "context summary" for a project idea you have, something you could paste at the start of any conversation to instantly ground the agent. Share it in the guild for feedback.

Next: the most important skill in agentic development, breaking problems into manageable pieces.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Art of Intent](02-the-art-of-intent.md) | **Context Is Everything** | [Breaking Problems Down →](04-breaking-problems-down.md) |

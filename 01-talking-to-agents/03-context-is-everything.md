# Context Is Everything

## The Invisible Factor

You can write the most specific prompt in the world and still get bad results if the agent doesn't have the right context. Context is everything the agent needs to know *around* your request: the background, constraints, prior decisions, and environmental details that shape what "correct" looks like.

Think of it this way: if you tell a chef "make me pasta," the result depends entirely on context the chef knows or doesn't know. Are you in Italy or a hospital cafeteria? Is it for a romantic dinner or a child's birthday? Are you allergic to anything? Do you have twenty minutes or two hours? The word "pasta" is the same, but the right answer is completely different depending on context.

Agents act on context available to the current run: the prompt, selected history or memory, files they inspect, project instructions, and tool results. Product memory varies and can be partial, so begin by pointing the agent to durable project sources and the current goal instead of assuming it remembers yesterday correctly.

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

The most effective way to provide technical context is to share the actual files. A coding agent such as Claude Code, Codex, Cursor, or Devin Desktop can inspect an authorized project folder. In a chat interface, paste or upload only the relevant, non-sensitive contents.

**Good technical context looks like:**
> "Here's my current index.html file: [paste file]. I'm using vanilla JavaScript, no frameworks. The styles are in a separate styles.css file. I need to add a feature to this existing page."

**Missing technical context causes problems like:**
The agent creates a React component when your project uses plain HTML. Or it writes code that conflicts with code that already exists. Or it suggests installing a tool that's incompatible with your operating system. These failures often indicate missing or uninspected context, but the agent also shares responsibility when it could have inspected the repository or asked before making a consequential assumption.

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

In the guild's methodology, every project starts with a **design document** (also called a design doc, DESIGN.md, or spec). This isn't bureaucracy. It's a practical tool for context management. A good design doc contains all four types of context in one place:

- **Project context:** What you're building and why
- **Technical context:** What technology you're using, what already exists
- **Constraint context:** What the boundaries are
- **Preference context:** How you want it to look and feel

When you start a new session, point the agent to the design doc and ask it to compare the document with the current repository. The design doc supplies intent; it may be stale or incomplete, so it does not replace reading the code, tracker, tests, and recent changes.

This is why the first step in our workflow is generating a design doc with the agent. It forces you to articulate context before you start building, and it creates a reusable artifact that keeps every subsequent conversation grounded.

### What a Design Doc Actually Looks Like

Enough description — here's a concrete example. This is roughly what a good design doc looks like for a small web project. It's written in Markdown (the same format as this chapter), lives in a file called `DESIGN.md` at the root of the project, and is short enough to read in two minutes.

```markdown
# Habit Tracker — Design Document

## Purpose
A personal tool for tracking daily habits (meditation, exercise, reading, etc.).
Single user, no accounts needed. Runs in a web browser, data stays on the device.

## Features
1. Add a habit with a name and an optional daily target (e.g. "Read — 30 minutes")
2. Mark a habit as done for today with one click
3. Show a 7-day streak view: did I do this every day this week?
4. Show a monthly calendar heat map of completion history
5. Edit a habit's name or delete it

## Technology
- HTML, CSS, JavaScript (no frameworks)
- Data stored in the browser's local storage as JSON
- Single HTML file, no build step, no server

## Interface
- Clean, minimal, mobile-friendly
- Habit list at the top, each row has the name, today's checkbox, and the 7-day streak
- Calendar heat map below the list, showing the last 30 days across all habits
- Add-habit form collapses to a "+" button when not in use

## Constraints
- Must work entirely offline after first load
- Must persist data across browser refreshes
- Must be readable on a phone screen (360px wide)

## Out of Scope
- User accounts, sharing, or sync across devices
- Notifications or reminders
- Import/export (could add later)
- Habit categories or tags

## Success Criteria (how I know it's done)
- I can add, mark, edit, and delete habits without opening devtools
- My data survives a full browser restart
- I used it for three days straight and it didn't frustrate me
```

Notice what this design doc does:

- **Names what's being built and for whom.** The Purpose section is a single paragraph. No jargon, no architecture diagrams, just the pitch.
- **Lists features as a numbered list.** Each feature is short, specific, and testable.
- **Specifies the technology.** The agent won't have to guess whether to use React.
- **Describes the interface in words.** Not a pixel-perfect mockup, just enough that the agent knows the layout.
- **Calls out constraints and out-of-scope items explicitly.** These are just as important as the features. "We're not doing accounts" prevents scope creep on every future conversation.
- **Defines success criteria.** This is the bar you'll use to decide when the project is done, and it's the bar the adversarial reviewer will hold the finished project to.

That's the format. When you hit the first build chapter in Phase 1, you'll write one like this for a bookmark manager. When you hit Phase 2, you'll write one for a Rust CLI issue tracker with different sections (no Interface, but a Commands section and a Data Model section). The structure adapts to the project; what stays constant is the discipline of writing it down before building.

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

2. Start a conversation with an agent. Give it only "add a dark mode toggle" and note which assumptions it makes. Then start a new session, provide a specific project's relevant context, and make the same request. Compare the assumptions, questions, and result.

3. Write a one-paragraph "context summary" for a project idea you have, something you could paste at the start of any conversation to instantly ground the agent. Share it in the guild for feedback.

Next: the most important skill in agentic development, breaking problems into manageable pieces.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Art of Intent](02-the-art-of-intent.md) | **Context Is Everything** | [Breaking Problems Down →](04-breaking-problems-down.md) |

# How Agents Think

## Understanding Your Collaborator

Before you start directing an AI agent, it helps to understand what's actually happening when you talk to one. Not the deep technical details. You don't need to know how neural networks work any more than you need to know how an internal combustion engine works to drive a car. But you do need a practical mental model of what the agent is good at, what it struggles with, and why it sometimes does baffling things.

## The Core Reality: Pattern and Context

An AI agent is a system that has absorbed an enormous amount of human-written text and learned patterns from it. When you give it a prompt, it generates a response by drawing on those patterns. This has a few practical implications that will shape how you work with it.

**It is not searching a database.** When you ask an agent a question or give it a task, it's not looking up an answer in a filing cabinet. It's generating a response based on patterns it learned during training. This means it can be confidently wrong. It will produce text that *sounds* right and *follows the patterns* of correct information even when the specific content is inaccurate. This is why verification is non-negotiable.

**It takes you literally.** If you say "make a button," you'll get a button. If you don't specify what the button should look like, where it should go, what it should do when clicked, or what text it should display, the agent will make its best guess. Sometimes that guess is great. Sometimes it's wildly off. The more specific you are, the less guessing happens.

**It has no memory between conversations.** Each conversation with an agent starts fresh. It doesn't remember the project you were working on yesterday (unless you're using a tool with memory features, or you give it the context again). This means you need to re-establish context at the start of each session. Sounds annoying, but it's actually useful. It forces you to articulate your project clearly, and that's a skill that pays dividends everywhere.

**It works best in chunks.** Agents handle focused, well-defined tasks much better than sprawling, ambiguous ones. "Build me an entire e-commerce platform" will produce mediocre results. "Create a product listing page that displays a grid of items, each showing a photo, name, price, and an 'add to cart' button" will produce something you can actually use.

## The Context Window

Every agent has what's called a context window: the amount of text it can "see" and work with at one time. Think of it as the agent's working memory. Everything you've said in the current conversation, everything the agent has replied, and any files or documents you've shared all take up space in this window.

When the conversation gets very long, older parts start falling out of the window. The agent doesn't forget them all at once. It's more like they become blurry and less precise. This has practical consequences:

- **Important details should be restated, not just referenced.** Don't say "remember what I said earlier about the color scheme." Say "the color scheme is navy blue and white, as I mentioned before."
- **Long conversations should be broken into focused sessions.** If you've been going back and forth for hours, the agent's responses might start drifting. Start a new conversation, re-establish context, and continue.
- **Design documents are your anchor.** This is one reason we start every project with a design doc. It's a written record of your intent that you can paste into any new conversation to instantly give the agent full context.

## What Agents Are Great At

Knowing what your collaborator excels at helps you delegate well:

**Generating code from descriptions.** This is the big one. You describe what you want in plain language, the agent writes the code. It handles syntax, language-specific conventions, best practices, and boilerplate (the repetitive setup code that every project needs). This is the cuneiform. The stuff that's been automated.

**Explaining things.** Agents are excellent teachers when you ask them to explain something. "Explain what this error message means in simple terms" or "What does this piece of code do, step by step?" will usually get you a clear, useful explanation.

**Debugging.** When something doesn't work, describing the problem to the agent (or just pasting the error message) will often get you a fix. Agents are very good at recognizing common error patterns and suggesting solutions.

**Exploring options.** "What are three different ways I could structure a task management app?" will give you multiple approaches to consider before committing to one. Really valuable in the design phase.

**Refactoring and improving.** Once something works, you can ask the agent to improve it. "Make this faster," "make this more readable," "add error handling." These are tasks agents handle well because they're well-defined transformations of existing code.

## What Agents Struggle With

Just as important is knowing where agents fall short, so you can compensate:

**Maintaining consistency across a large project.** If your project spans many files and thousands of lines, the agent might make changes in one place that contradict something in another. This is a context window limitation. You manage it by working in focused chunks and verifying as you go.

**Knowing what you actually want.** The agent has zero insight into your goals, preferences, and constraints beyond what you tell it. It won't ask "wait, who is this for?" or "have you considered that your users might need accessibility features?" unless you've set up that expectation. You're the one who brings domain knowledge and judgment.

**Saying "I don't know."** Agents will almost always give you *an* answer. Even when the correct answer is "this can't be done" or "I'm not sure," the agent might generate a plausible-sounding response that's wrong. This is why VDD exists. You define success criteria upfront and check the result against them, rather than trusting the agent's confidence.

**Understanding your specific environment.** The agent doesn't know what operating system you're on, what other software you have installed, what version of things you're running, or what your file structure looks like. Unless you tell it. When things don't work, missing context is often the reason.

## The Collaboration Model

The most productive way to think about working with an agent is as a collaboration between two very different kinds of intelligence:

**You bring:** Intent, judgment, domain knowledge, verification, taste, the ability to say "no, that's not right." You're the quality control. You're the one who knows what "done" looks like.

**The agent brings:** Speed, breadth of knowledge, tireless execution, the ability to generate and iterate rapidly, and all the syntactic/technical knowledge you don't need to memorize.

Neither of you is sufficient alone. An agent without direction builds generic, aimless things. A person without an agent builds slowly, bottlenecked by syntax. Together, you can build things that neither could build independently.

This is the core reframe of the guild: you are not learning to be replaced by AI. You're learning to *work with* AI in a way that makes you far more capable than you were before.

## Practical Implications

Here's what all of this means for your day-to-day work:

1. **Be specific.** The agent can't read your mind. Every detail you leave out is a detail the agent guesses about. Some guesses will be wrong.

2. **Verify everything.** The agent will sound confident even when it's wrong. Don't trust the output. Test it. Does it work? Does it do what you asked? Does it handle edge cases?

3. **Manage context deliberately.** Keep conversations focused. Restate important details. Use design documents as anchors. Start fresh sessions when conversations get long.

4. **Break work into focused tasks.** Big vague requests produce big vague results. Small specific requests produce small specific results you can assemble into something great.

5. **Iterate.** Your first attempt will rarely be perfect. The power is in the speed of iteration: ask, review, refine, repeat. The agent can do this loop a hundred times in the time it would take to do it once by hand.

Now that you understand how your collaborator works, let's learn how to talk to it.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Git: Just Enough](../00-foundations/05-git-just-enough.md) | **How Agents Think** | [The Art of Intent →](02-the-art-of-intent.md) |

# The Art of Intent

## From "I Want a Thing" to "Build Me This"

The single biggest factor in whether an agent builds what you want is how well you communicate what you want. This sounds obvious. It's not easy. Most people overestimate how clear their ideas are, not because they're bad communicators, but because they've never had to explain their vision to something that takes every word literally and fills in gaps with guesses.

This chapter is about turning the fuzzy picture in your head into a precise description an agent can execute.

## The Specificity Spectrum

Every instruction you give falls somewhere on a spectrum from vague to precise. Here's what happens at different points.

**Vague:** "Make me a website."

The agent will build a website. It'll have a navigation bar, some placeholder text, maybe a hero image. It'll look generic. It won't be *your* website because you haven't told the agent what makes yours different from every other website in the world.

**Somewhat specific:** "Make me a website for my photography business."

Better. Now the agent knows the domain, so it'll include things like a photo gallery, maybe a contact form, probably something about services. But it still doesn't know your name, your style, your location, your prices, your brand voice, or what you want visitors to do.

**Specific:** "I'm a wedding photographer based in Portland, Oregon. I need a one-page website that has: my name (Sarah Chen Photography) at the top, a grid gallery showing 12 photos (I'll provide them), a section listing my three packages (Elopement $1,500, Half Day $3,000, Full Day $5,500, each with a one-sentence description), a contact form where people enter their name, email, wedding date, and a message, and a short about-me section. The overall feel should be elegant and minimal. Lots of white space, a serif font for headings, clean lines. No flashy animations."

Now the agent can build something you'll actually use. Notice what happened: you answered the questions the agent would need answered *before it had to guess*. Who is this for? What sections does it need? What's the content? What's the style?

## The Five Questions

Before you type anything to an agent, run through these five questions. You don't need to answer them formally, just make sure you've thought about each one.

**What is this thing?** Define it simply. Not "an app." A specific kind of tool with a specific purpose. "A personal finance tracker that shows where my money goes each month."

**Who is it for?** Even if it's just for you, say so. "For me personally" tells the agent this can be simpler than something for a general audience. "For elderly users who aren't comfortable with technology" completely changes the design approach.

**What should it do?** List the functions. Not in technical terms, in human terms. "A user should be able to add an expense, categorize it, see a monthly total, and view a breakdown by category." Each verb here (add, categorize, see, view) is a feature the agent needs to build.

**What should it look like?** You don't need to be a designer. Broad strokes are fine. "Simple and clean, not cluttered" is useful. "Dark mode, with a sidebar navigation" is even more useful. "Similar to the feel of [some app you like]" works too. Agents know what popular apps look like.

**What should it NOT do?** This is surprisingly important. "No user accounts or login, this is just for me." "No payment processing." "Don't include a chat feature." Explicitly excluding things prevents the agent from adding complexity you don't want.

## Show, Don't Just Tell

One of the most powerful techniques for communicating with agents is giving examples. Instead of describing what you want abstractly, show what it looks like concretely.

**Abstract:** "The notifications should be helpful and not annoying."

What does "helpful and not annoying" mean? That's different for every person and every context. The agent has no idea what your threshold for annoying is.

**Concrete with examples:**

"When a task is due tomorrow, show a gentle reminder like: 'Heads up, your report for the Johnson account is due tomorrow.' Don't show reminders for tasks more than 3 days away. Never send more than 3 reminders in a day. If a task is overdue, change the tone slightly: 'The Johnson account report was due yesterday. Want to reschedule it?'"

Now the agent knows the tone, the timing, the limits, and even has example text to work from. It can build this accurately.

## The "Imagine You're Explaining to a Contractor" Test

Here's a useful test for whether your instructions are clear enough: imagine you're hiring a contractor to renovate your kitchen, and you'll be out of the country while they do the work. You can't answer follow-up questions. Whatever you write down is all they have to go on.

Would you write "make the kitchen nice"? Of course not. You'd specify the layout, the materials, the colors, where the appliances go, what kind of countertops, what to keep and what to tear out.

Apply the same standard to your agent instructions. You won't always be this detailed. Sometimes a quick, short prompt is fine for small tasks. But for anything that matters, treat your instructions like they need to survive without follow-up.

## Writing Good Prompts: A Template

You don't have to follow a rigid template, but when you're learning, structure helps. Here's one that works well:

```
## What I'm Building
[One or two sentences describing the project and its purpose]

## Who It's For
[The audience, even if it's just you]

## What It Should Do
[List the features/functions in plain language]

## What It Should Look Like
[Visual direction: style, mood, reference points]

## What It Should NOT Do
[Explicit exclusions: things you don't want]

## Additional Context
[Anything else relevant: constraints, preferences, technical requirements you're aware of]
```

Let's see this template in action for a real project:

```
## What I'm Building
A habit tracker that helps me build and maintain daily habits.

## Who It's For
Just me. I'm the only user. It doesn't need accounts or login.

## What It Should Do
- Let me add a new habit with a name (like "Read for 20 minutes" or "Exercise")
- Show today's habits as a checklist I can mark complete
- Track my streak for each habit (consecutive days completed)
- Show a weekly view so I can see which days I hit and which I missed
- Let me delete a habit I no longer want to track

## What It Should Look Like
- Clean and minimal. I want to open it and immediately see today's habits
- Dark mode preferred
- Use checkmarks for completed habits, empty circles for incomplete
- The streak count should be visible next to each habit
- Mobile-friendly since I'll mostly use it on my phone

## What It Should NOT Do
- No reminders or notifications
- No social features or sharing
- No analytics beyond streaks and the weekly view
- Don't make it complicated. If a feature isn't listed above, I don't want it

## Additional Context
This should work in a web browser. I don't need a native phone app,
just a website that works well on a phone screen.
```

An agent receiving this prompt has everything it needs to build something useful on the first try. Will it be perfect? Probably not. But it'll be close enough that your feedback can be specific ("the streak counter resets even though I completed yesterday, can you fix that?") instead of vague ("this isn't what I wanted").

## Common Mistakes

**The Drive-By.** One-sentence prompts for complex tasks. "Build a project management tool." This produces generic, surface-level output. Take three minutes to write a proper description. It saves hours of back-and-forth.

**The Everything Request.** Asking for every feature you can imagine in one prompt. "I want a habit tracker with streaks, analytics, social sharing, AI-powered habit suggestions, integration with my calendar, a mobile app, a web dashboard, weekly reports..." Start with the core. Build it. Verify it works. Then add features one at a time.

**The Assumed Context.** Writing your prompt as if the agent already knows your project. "Now add the sidebar we discussed." If you're in a new conversation, the agent has no idea what sidebar. Restate context. Always. It's not repetitive to the agent. It's essential.

**The Style-Less Request.** Forgetting to describe how it should look and feel. The agent defaults to something generic. Even a few words about style ("minimal," "playful," "professional," "dark mode") make a big difference.

**The Negative-Only Brief.** Describing what you don't want without saying what you do want. "I don't want it to be cluttered or confusing or have too many colors" tells the agent to avoid things but gives no direction toward anything specific. Say what you want *first*, then add what you don't.

## The Refinement Conversation

Your first prompt is not your last. Once the agent builds something, the conversation shifts from description to refinement. This is where most of the value gets created, and it's a different mode of communication.

Good refinement feedback is specific and actionable:

- "The button to add a habit is too small on mobile. Can you make it larger and more prominent?"
- "When I complete all habits for the day, I'd like some kind of visual celebration. Nothing crazy, maybe the checkmarks turn green and there's a small congratulations message."
- "The weekly view works but the days are labeled Mon/Tue/Wed. Can you use single letters M/T/W to save space on mobile?"

Bad refinement feedback is vague:

- "It doesn't feel right." (What doesn't feel right? Be specific.)
- "Make it better." (In what way? Faster? Prettier? More functional?)
- "I don't like it." (What don't you like? What would you like instead?)

You'll develop a feel for this over time. The more you practice turning "that's not right" into "specifically, this element should change in this way," the faster your projects will converge on what you actually want.

## Exercises

Try writing prompts for each of these using the five questions and the template above. Don't build them yet, just practice articulating intent.

1. A personal recipe collection that lets you save, search, and organize recipes
2. A simple timer app that lets you create named timers (like "Laundry" or "Meeting in 30 min")
3. A reading list tracker where you can add books, mark them as read, and rate them

Write these out and share them in the guild. Getting feedback on your prompts before building is great practice, and it's the earliest form of the adversarial refinement that defines our methodology.

Next up: why context is the invisible factor that makes or breaks every interaction with an agent.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← How Agents Think](01-how-agents-think.md) | **The Art of Intent** | [Context Is Everything →](03-context-is-everything.md) |

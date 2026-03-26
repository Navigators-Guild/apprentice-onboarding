# Breaking Problems Down

## The Skill That Changes Everything

If you only master one skill from this entire learning path, make it this one. Taking a big, complex, ambiguous problem and breaking it into small, clear, actionable pieces is the most valuable skill in agentic development. It's also the most valuable skill in *thinking*, period, but that's a broader conversation.

Here's why this matters so much with agents: an agent given a small, well-defined task will almost always produce good output. An agent given a large, vague task will almost always produce mediocre output. The difference isn't the agent's capability. It's the clarity of the input. Decomposition is how you turn overwhelming projects into a sequence of things an agent can nail one at a time.

## The Problem with Big Asks

When you say something like "build me a project management tool," the agent has to make hundreds of decisions at once. What features to include. How to structure the data. What the interface looks like. How different features interact. What to prioritize. What to leave out.

Even a very capable agent will make some of those decisions badly, because there's no way to get all of them right without guidance. And when those bad decisions interact with each other, the result compounds. You end up with something that kind of works but isn't really what you wanted, and you're not sure where to start fixing it.

Compare that to: "Create a page that displays a list of tasks. Each task has a title and a status, either 'to do,' 'in progress,' or 'done.' Show the tasks in three columns based on their status."

That's one piece of a project management tool. It's small enough that the agent can get it right. And once that piece works, you add the next: "Now add the ability to create a new task with a title." Then the next: "Let me drag tasks between columns to change their status." Each step builds on a working foundation.

## How to Decompose: The Layer Approach

There are many ways to break problems down. Here's one that works well for beginners.

**Start with the core.** Ask yourself: what is the absolute simplest version of this project that would still be useful? Strip away every nice-to-have. What's left?

For a recipe collection app:
- Core: display a list of recipes, let me add a new recipe with a name and ingredients.
- That's it. That's the core. A searchable, categorized, photo-equipped recipe database is not the core. That's the finished product. The core is a list you can add to.

**Add layers one at a time.** Once the core works, add the next most important feature. Then the next. Each addition is a separate, focused task for the agent.

For the recipe app, the layers might be:
1. Core: display recipes and add new ones
2. Layer: add categories (dinner, dessert, snack) and filter by category
3. Layer: add a search bar that filters as you type
4. Layer: add the ability to edit and delete recipes
5. Layer: add a photo for each recipe
6. Layer: make it look polished. Better layout, colors, typography

Notice that each layer is a single, testable feature. After each one, you can verify it works before moving on. If layer 3 breaks something from layer 1, you catch it immediately instead of discovering it after you've built six more features on top.

## How to Decompose: The User Story Approach

Another approach is to think about what a person actually *does* with your software, step by step.

**Write out the user's journey.** For each thing a user might do, describe it as a simple story:

For a habit tracker:
- "I open the app and see today's habits."
- "I tap a habit to mark it complete."
- "I want to add a new habit, so I tap an 'add' button and type the name."
- "I want to see how I've done this week, so I tap a 'weekly view' and see a grid."
- "I realize I don't want to track a habit anymore, so I delete it."

Each of these stories is a piece of functionality you can ask the agent to build independently. They're in a natural order (you need to display habits before you can mark them complete), and they're each small enough to build and verify in one conversation.

## How to Decompose: The "What Changes" Approach

When you're adding to an existing project or modifying something, focus on what specifically needs to change.

**Bad:** "The app needs to be improved."
**Good:** "Three specific changes: the add button should be bigger, the weekly view should show streak counts, and completed habits should move to the bottom of the list."

Each change is independent. You can ask the agent to make them one at a time. You can verify each one individually. And if one of the changes causes a problem, you know exactly which one did it.

## The Dependency Question

When you have a list of pieces to build, order matters. Some pieces depend on other pieces. You can't build "filter recipes by category" if you haven't built "recipes have categories" yet.

A simple way to figure out the order: for each piece, ask "does this require anything else to exist first?" If yes, build that thing first.

For the recipe app:
- Display recipes → no dependencies, build first
- Add new recipes → needs display to exist (otherwise you add recipes into the void)
- Add categories → needs recipes to exist
- Filter by category → needs categories to exist
- Search → needs recipes with names to exist
- Edit/delete → needs existing recipes
- Photos → needs existing recipes

This gives you a natural build order. You don't need a formal diagram. Just think through the dependencies logically.

## When to Decompose and When Not To

Not every interaction with an agent needs formal decomposition. Small, simple tasks can be given whole:

- "Add a footer with my name and the year" - just do it
- "Change the background color to dark blue" - just do it
- "Fix the bug where clicking 'save' doesn't save" - just do it

Decomposition is for when the task is complex enough that doing it all at once would produce inconsistent or incomplete results. A good rule of thumb: if you can describe the task completely in two or three sentences, it probably doesn't need decomposing. If you need a paragraph or more, break it up.

## The Decomposition Conversation

You can even use the agent to help you decompose. This is a legitimate and smart use of the tool:

> "I want to build a personal budget tracker. Before we start building, help me break this down into small, independent features I can build one at a time. Order them so that each feature builds on the previous ones. Keep it simple. What's the minimum set of features that would make this actually useful?"

The agent will produce a breakdown. Review it critically. Does the order make sense? Are any steps too big? Are there dependencies it missed? Adjust the plan before building. This is the design phase, and it's the highest-leverage time you spend on a project.

## Exercises

1. Take this project idea: "A personal journal app where I can write daily entries, tag them with moods, and look back at past entries." Break it down into layers using the approach described above. What's the core? What are the layers? What's the build order?

2. Take this project idea: "A tool for planning road trips. Enter your start and end points, add stops along the way, and see the total driving time." Write out the user stories. Each story should be one thing a user does.

3. Open a conversation with an agent and describe a project idea you're interested in. Ask the agent to help you decompose it. Review the agent's breakdown critically. Is anything too big? Too small? In the wrong order? Revise it.

4. Share your decomposition in the guild channel and ask for feedback. Can other members spot dependencies you missed? Steps that could be broken down further? This is lightweight adversarial review, exactly the kind of thinking the guild develops.

You've now covered the fundamentals of working with agents: understanding how they think, communicating your intent, providing context, and breaking problems down. Time to put it all together and build something real.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Context Is Everything](03-context-is-everything.md) | **Breaking Problems Down** | [Your First Build →](05-first-build.md) |

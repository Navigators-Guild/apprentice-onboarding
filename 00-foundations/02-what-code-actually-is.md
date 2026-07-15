# What Code Actually Is

## The Mental Model You Need (And the One You Don't)

Most people imagine code as an arcane language full of symbols and rules that takes years to learn. That image keeps people away. But it's like imagining that cooking requires understanding food chemistry at a molecular level. Molecular gastronomy exists, sure, but billions of people cook every day without it.

You do not need to begin by writing code from memory. You do need a basic mental model, and you will practice reading diffs, making small edits, and connecting requirements to behavior. A film director need not build a camera, but should understand what it can and cannot do.

## Code Is Instructions for Machines

At its most basic, code is a set of instructions written in a language a computer can follow. That's it. Every piece of software you've ever used (your phone's apps, websites, games, the AI agent you're about to start working with) is a set of instructions telling a computer what to do in what order.

Those instructions do a handful of basic things:

**Store information.** The computer remembers things: a user's name, a list of products, the current score in a game. This information gets stored in what programmers call variables and databases, but conceptually it's just the computer's memory.

**Make decisions.** The computer checks conditions and does different things depending on what it finds. "If the user is logged in, show them their dashboard. If not, show the login page." Every time software behaves differently based on circumstances, there's a decision in the code.

**Repeat actions.** The computer does the same thing over and over, usually with slight variations. "For every email in the inbox, check if it's spam." "For every item in the shopping cart, add up the price." Computers can repeat instructions quickly and consistently; bugs arise when the instructions, assumptions, data, or environment are wrong.

**Communicate.** The computer sends and receives information: displaying things on screen, accepting input from a keyboard or touchscreen, sending data to other computers over the internet. Every time you click a button and something happens, code is handling that communication.

Store, decide, repeat, and communicate are a useful beginner model, not a complete taxonomy of computing. Complexity comes from how operations, state, people, dependencies, and environments interact.

## Why This Matters for Directing Agents

Understanding these four operations changes how you talk to agents. Instead of vague requests, you can think in terms of what the software actually needs to do.

Say you want a tool that helps you manage your book club. Without this mental model, you might say "make me a book club app." With it, you can think through what the app actually needs:

**Store:** The list of members, the books you've read, the book you're currently reading, each member's rating and notes, the schedule of meetings.

**Decide:** If a member hasn't submitted their rating yet, show a reminder. If everyone has rated a book, calculate and display the average. If a meeting is coming up in the next three days, send a notification.

**Repeat:** Go through all members and check who has RSVP'd for the next meeting. Go through all past books and sort them by average rating for a "best of" list.

**Communicate:** Show each member their personal dashboard. Let them type in ratings and notes. Display the group's reading list. Send email reminders about upcoming meetings.

You do not need to know the final implementation before planning. Thinking through these four dimensions gives the agent a better brief and gives you questions to verify; it will not uncover every requirement or eliminate guessing.

## The Shape of Software

Software generally has a few layers, and knowing they exist helps you communicate more precisely.

**The interface** is what people see and interact with. Buttons, text, images, forms. When you say "I want it to look clean and simple," you're talking about the interface. When you say "there should be a button that lets you add a new book," you're describing an interface element.

**The logic** is what happens behind the scenes when someone interacts with the interface. When a user clicks "add book," the logic handles searching for the book, storing it in the list, and updating the display. You don't need to see the logic, but you need to describe what it should *do*.

**The data** is the information the software stores and retrieves. Your book list, user accounts, ratings, meeting dates. Thinking about what data your project needs is one of the most useful planning steps you can take before asking an agent to build anything.

**The connections** are how your software talks to other things. Does it need to pull book information from the internet? Send emails? Work on phones and computers? These connections need to be specified because agents won't assume them.

When you write a design document (which you'll learn to do in Phase 1), you're describing these layers: what should the user see, what should happen when they interact with it, what information needs to be stored, and what external things does it need to talk to.

## Files and Folders

One last mental model: software lives in files, and those files live in folders (also called directories). A typical project might have files that define the interface, files that contain the logic, files that configure the database, and files that set up the project itself.

You'll see and sometimes edit these files in your projects. A project is a collection of files working together, not necessarily one monolithic file. When something goes wrong, narrowing the affected behavior, file, and evidence gives an agent a better starting point than "it's broken."

## Data Formats You'll See: JSON

One file format is worth knowing by sight because it shows up everywhere in modern software: **JSON** (pronounced "jay-sawn," short for JavaScript Object Notation). JSON is a way to write down structured data — lists, names, numbers, nested groups — as plain text that both humans and programs can read.

You'll see JSON in three places during this curriculum: files your apps use to store data, configuration files like `.mcp.json`, and error messages when something parsing JSON fails. You don't need to write JSON by hand — your agent will produce it — but you need to recognize it and spot when it's broken.

Here's what JSON looks like:

```json
{
  "title": "Bookmark Manager",
  "version": 1,
  "authors": ["doll", "maxine"],
  "settings": {
    "dark_mode": true,
    "max_bookmarks": 500
  },
  "tags": []
}
```

The pieces:

- **Curly braces `{ }`** wrap an object (a collection of key-value pairs).
- **Square brackets `[ ]`** wrap a list (called an "array").
- **Keys** are always strings in double quotes (`"title"`).
- **Values** can be strings in double quotes (`"Bookmark Manager"`), numbers without quotes (`1`, `500`), booleans without quotes (`true`, `false`), lists (`["doll", "maxine"]`), or nested objects (the `settings` section).
- **Commas** separate items in a list or key-value pairs in an object. Notice there is **no comma after the last item**. A trailing comma is one common cause of JSON parse errors.
- **Colons** separate keys from their values.

Here's the same data with a mistake — a trailing comma after `"max_bookmarks": 500`:

```json
{
  "settings": {
    "dark_mode": true,
    "max_bookmarks": 500,
  }
}
```

JSON parsers will refuse to read this file and will produce an error like `Unexpected token } at line 4`. The fix is to delete the trailing comma. Other common JSON errors: missing quotes around a key, single quotes instead of double quotes (JSON only accepts double), and unmatched brackets.

**A sibling format you'll see later: YAML.** CI configuration files like `.github/workflows/ci.yml` are YAML, not JSON. YAML conveys the same kind of data but uses indentation instead of braces and brackets. You don't need to learn YAML syntax now; when you hit it in Phase 3, recognize that it's structured data like JSON but laid out differently.

## The Takeaway

Code is not magic. It's instructions that store information, make decisions, repeat actions, and communicate. Software has layers: interface, logic, data, and connections. Projects live in files and folders.

You now have a starting model for directing an agent that writes code. Keep deepening it as the projects introduce types, errors, tests, dependencies, security boundaries, and performance. The agent can propose syntax and algorithms; you remain responsible for the requirements and evidence used to accept them.

That's the mental model. Now let's set up your workspace.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The New Literacy](01-the-new-literacy.md) | **What Code Actually Is** | [The Language Landscape →](03-the-language-landscape.md) |

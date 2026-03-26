# What Code Actually Is

## The Mental Model You Need (And the One You Don't)

Most people imagine code as an arcane language full of symbols and rules that takes years to learn. That image keeps people away. But it's like imagining that cooking requires understanding food chemistry at a molecular level. Molecular gastronomy exists, sure, but billions of people cook every day without it.

You don't need to *write* code. But you do need a basic mental model of what code is and what it does, because that model will make you noticeably better at directing agents. A film director doesn't need to know how to build a camera, but they'd better understand what a camera can and can't do.

## Code Is Instructions for Machines

At its most basic, code is a set of instructions written in a language a computer can follow. That's it. Every piece of software you've ever used (your phone's apps, websites, games, the AI agent you're about to start working with) is a set of instructions telling a computer what to do in what order.

Those instructions do a handful of basic things:

**Store information.** The computer remembers things: a user's name, a list of products, the current score in a game. This information gets stored in what programmers call variables and databases, but conceptually it's just the computer's memory.

**Make decisions.** The computer checks conditions and does different things depending on what it finds. "If the user is logged in, show them their dashboard. If not, show the login page." Every time software behaves differently based on circumstances, there's a decision in the code.

**Repeat actions.** The computer does the same thing over and over, usually with slight variations. "For every email in the inbox, check if it's spam." "For every item in the shopping cart, add up the price." Computers are extraordinarily good at repetition. Millions of operations per second without getting bored or making mistakes.

**Communicate.** The computer sends and receives information: displaying things on screen, accepting input from a keyboard or touchscreen, sending data to other computers over the internet. Every time you click a button and something happens, code is handling that communication.

That's it. Store, decide, repeat, communicate. Every piece of software in existence is built from combinations of these four operations. The complexity comes from *how many* of them get chained together and how they interact, not from any single operation being complicated.

## Why This Matters for Directing Agents

Understanding these four operations changes how you talk to agents. Instead of vague requests, you can think in terms of what the software actually needs to do.

Say you want a tool that helps you manage your book club. Without this mental model, you might say "make me a book club app." With it, you can think through what the app actually needs:

**Store:** The list of members, the books you've read, the book you're currently reading, each member's rating and notes, the schedule of meetings.

**Decide:** If a member hasn't submitted their rating yet, show a reminder. If everyone has rated a book, calculate and display the average. If a meeting is coming up in the next three days, send a notification.

**Repeat:** Go through all members and check who has RSVP'd for the next meeting. Go through all past books and sort them by average rating for a "best of" list.

**Communicate:** Show each member their personal dashboard. Let them type in ratings and notes. Display the group's reading list. Send email reminders about upcoming meetings.

You don't need to know *how* any of this gets coded. The agent handles that. But thinking through these four dimensions gives you a complete picture of what you're asking for, and the agent can build what you need instead of guessing.

## The Shape of Software

Software generally has a few layers, and knowing they exist helps you communicate more precisely.

**The interface** is what people see and interact with. Buttons, text, images, forms. When you say "I want it to look clean and simple," you're talking about the interface. When you say "there should be a button that lets you add a new book," you're describing an interface element.

**The logic** is what happens behind the scenes when someone interacts with the interface. When a user clicks "add book," the logic handles searching for the book, storing it in the list, and updating the display. You don't need to see the logic, but you need to describe what it should *do*.

**The data** is the information the software stores and retrieves. Your book list, user accounts, ratings, meeting dates. Thinking about what data your project needs is one of the most useful planning steps you can take before asking an agent to build anything.

**The connections** are how your software talks to other things. Does it need to pull book information from the internet? Send emails? Work on phones and computers? These connections need to be specified because agents won't assume them.

When you write a design document (which you'll learn to do in Phase 1), you're describing these layers: what should the user see, what should happen when they interact with it, what information needs to be stored, and what external things does it need to talk to.

## Files and Folders

One last mental model: software lives in files, and those files live in folders (also called directories). A typical project might have files that define the interface, files that contain the logic, files that configure the database, and files that set up the project itself.

You'll see these files in your projects. You won't need to write them by hand (the agent creates them), but you should be comfortable with the idea that a project is a collection of files working together, not a single monolithic thing. When something goes wrong, it's usually in a specific file, and being able to say "the problem seems to be with the booking form, not the homepage" helps the agent fix it way faster than "it's broken."

## The Takeaway

Code is not magic. It's instructions that store information, make decisions, repeat actions, and communicate. Software has layers: interface, logic, data, and connections. Projects live in files and folders.

You now have enough understanding of what code *is* to direct an agent that writes it. You don't need to go deeper. Syntax, language-specific features, algorithmic optimization: that's the agent's job. Your job is to know what you want built and describe it in terms of what it stores, decides, repeats, and communicates.

That's the mental model. Now let's set up your workspace.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The New Literacy](01-the-new-literacy.md) | **What Code Actually Is** | [The Language Landscape →](03-the-language-landscape.md) |

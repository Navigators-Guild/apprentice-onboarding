# Your First Build

## Putting It All Together

You've learned the concepts. Now you build. This chapter walks you through a complete project from start to finish using the guild methodology: design doc first, build in layers, verify, prepare for review.

The project: **a personal bookmark manager.** Something that lets you save links with notes, organize them, and find them later. Simple enough to complete as a first project, useful enough that you'll actually use it.

This project uses HTML, CSS, and JavaScript, not Rust. It's the one exception in the curriculum. For your very first build, seeing something appear in a browser the moment you open the file is the fastest path to "I made a thing." Starting with Phase 2, everything moves to Rust. But right now, the priority is learning the workflow, not the toolchain.

This is a guided walkthrough. Follow along step by step. After this, your next projects will be self-directed.

## Step 1: Generate the Design Document

The first thing you do on any guild project is create a design document. This is where you define what you're building before any code exists.

Open a conversation with your agent and say something like:

> "I want to build a personal bookmark manager, a simple web app where I can save links with titles and notes, tag them for organization, and search through them. It's just for me, no accounts or login needed. Help me write a design document that covers what it should do, what it should look like, and what technology we should use. Keep it simple, this is my first project."

The agent will produce a design document. Read it carefully. This is your first act of verification: does the document describe what you actually want? Things to check:

- Did it include features you didn't ask for? Remove them. Scope creep starts here.
- Did it miss something you want? Add it.
- Does the technology choice make sense? For a first project, plain HTML, CSS, and JavaScript (no frameworks) is ideal. If the agent suggests React, Vue, or another framework, say "let's keep this simpler, use plain HTML, CSS, and JavaScript with no frameworks."
- Is the scope realistic? This should be a project you can build in a few hours, not a few weeks.

Edit the design doc until it matches your vision. Then save it. This is the first file in your project and the anchor for every future conversation.

Here's roughly what your design doc might look like after refinement:

```
# Bookmark Manager - Design Document

## Purpose
A personal tool for saving and organizing web links with notes.
Single user, no authentication needed. Runs in a web browser.

## Features
1. Add a bookmark: URL, title, optional note, optional tags
2. Display all bookmarks in a list, newest first
3. Click a bookmark to open the link in a new tab
4. Edit a bookmark's title, note, or tags
5. Delete a bookmark
6. Filter bookmarks by tag
7. Search bookmarks by title or note content

## Technology
- HTML, CSS, JavaScript (no frameworks)
- Data stored in the browser's local storage
- Single page, no server needed

## Interface
- Clean, minimal design
- Add form at the top
- Bookmark list below
- Tag filter as clickable buttons above the list
- Search bar above the list, next to the tag filters

## Out of Scope
- User accounts or sharing
- Bookmark folders or nested organization
- Browser extension for quick saving
- Import/export (can add later)
```

Save this as `DESIGN.md` in your project folder.

## Step 2: Set Up the Project

In your terminal:

```
cd ~/guild-projects/portfolio/guild-portfolio
mkdir bookmark-manager
cd bookmark-manager
```

Save your design document here. You can ask the agent to create it as a file, or create it yourself in VS Code by making a new file called `DESIGN.md` and pasting the content.

## Step 3: Build the Core (Layer 1)

Now look at your design doc and identify the core: the simplest version that does something. For the bookmark manager, that's:

- Display a list of bookmarks
- Add a new bookmark (URL and title)
- Bookmarks persist (saved in browser storage)

Start a new conversation with your agent (or continue if context is still fresh). Share your design document and say:

> "Here's my design document for a bookmark manager. Let's start with just the core: I want to be able to add a bookmark with a URL and title, see it appear in a list, and have it persist when I refresh the page. Use browser local storage for saving data. Plain HTML, CSS, and JavaScript in a single file called index.html. Make the design clean and minimal."

The agent will generate code. Save it as `index.html` in your bookmark-manager folder.

## Step 4: Verify

Open the file in your browser (double-click it, or in VS Code right-click and select "Open with Live Server" if you installed that extension).

Now test it against the core requirements:

- **Can you add a bookmark?** Type in a URL and title, click add. Does it appear in the list?
- **Can you see the list?** Are your bookmarks displayed?
- **Does it persist?** Refresh the page. Are your bookmarks still there?

If something doesn't work, tell the agent exactly what's happening:

> "When I add a bookmark and refresh the page, the bookmarks disappear. They should persist using local storage. Here's the current code: [paste the code]."

This is verification driven development in action. You defined what "working" means *before* building (the design doc), and now you're checking the result against that definition.

**A habit to start now:** Try adding a bookmark with an empty title. Or a URL that's just nonsense. Does the app handle it, or does it silently store garbage? Input validation (checking that data is reasonable before you save it) is a security and quality habit worth building from your very first project. If your app stores whatever it's given without checking, tell the agent: "Add validation. Don't allow empty titles. Check that the URL starts with http:// or https://." You'll learn more about this in the Security chapter later, but the habit starts here.

## Step 5: Add Layers

Once the core works, add features one at a time. Each layer follows the same loop: ask the agent, verify the result, fix any issues.

**Layer 2: Notes and tags**

> "The core bookmark list is working. Now I want to add two fields to the add form: an optional note (a text area for a brief description) and optional tags (comma-separated text that gets stored as a list). Display the note under each bookmark's title, and display tags as small labeled badges."

Verify: Add a bookmark with notes and tags. Do they display correctly? Add one without notes and tags. Does it still work? (This is your first edge case check.)

**Layer 3: Edit and delete**

> "Now add the ability to edit and delete bookmarks. Each bookmark should have a small edit icon and a delete icon. Clicking edit should let me change the title, URL, note, and tags inline. Clicking delete should remove the bookmark after a confirmation. Make sure changes persist in local storage."

Verify: Edit a bookmark. Does the change persist after refresh? Delete a bookmark. Is it gone after refresh? Try editing and then canceling. Does it revert correctly?

**Layer 4: Tag filtering**

> "Now add tag filtering. Above the bookmark list, display all unique tags as clickable buttons. When I click a tag, the list should filter to only show bookmarks with that tag. There should be an 'All' button that removes the filter. The currently active filter should be visually highlighted."

Verify: Click a tag. Does the list filter? Click "All." Does the full list return? Add a new bookmark with a new tag. Does the tag appear in the filter buttons?

**Layer 5: Search**

> "Add a search bar next to the tag filters. It should filter the bookmark list in real time as I type, matching against bookmark titles and notes. Search and tag filters should work together. If I have a tag filter active and then search, it should search within the filtered results."

Verify: Search for a word you know is in a bookmark title. Does it filter? Search for something in a note. Does it find it? Activate a tag filter, then search. Does it search within the filtered set? Clear the search. Does the tag filter remain active?

**Layer 6: Polish**

> "The functionality is complete. Now let's polish the interface. I want: better spacing and typography, a subtle color scheme (dark background with light text, dark mode), smooth transitions when filtering and searching, the add form should collapse to a button when not in use to keep the interface clean, and bookmarks should show the domain name extracted from the URL as a subtle label."

Verify: Does it look good? Is it comfortable to use? Are the transitions smooth? Does the form collapse and expand?

## Step 6: Document the Process

This is what separates a guild project from a random thing you built. Create a file called `PROCESS.md` in your project folder. Document:

**What you built and why.** A paragraph summarizing the project.

**Your build process.** Walk through the layers you built, in order. For each layer, note:
- What you asked the agent to do
- Whether it worked on the first try
- What you had to fix or adjust
- Any verification failures and how you resolved them

**What you learned.** What surprised you? What was harder than expected? What would you do differently next time?

**Known issues.** Is there anything that doesn't work perfectly? Anything you'd want to improve? Being honest about known issues shows maturity and self-awareness, both things the guild values.

This document is part of your portfolio. Reviewers will read it. It's the evidence that you didn't just generate code, you *directed* the process with intention.

## Step 7: Commit and Push

```
cd ~/guild-projects/portfolio/guild-portfolio/bookmark-manager
git add .
git commit -m "Complete bookmark manager - first portfolio project"
git push
```

Your project is now live on GitHub. The code, the design doc, and the process documentation are all visible.

## Step 8: Submit for Adversarial Review

Post your project in the guild's adversarial review channel. Include:
- A link to your GitHub repository
- A brief description of what you built
- An invitation for honest feedback

Then wait. The roasts will come. Some will be about functionality ("what happens if you paste a URL without https://? Does it break?"). Some about design ("the contrast between your text and background isn't accessible enough"). Some about your process ("your design doc says no import/export, but that would actually be trivial to add and really useful").

All of it is valuable. Take notes on every piece of feedback. Then go back, fix what needs fixing, improve what could be better, and commit your changes with messages like "Address review feedback: add URL validation" and "Improve contrast ratio for accessibility."

This cycle (build, review, refine) is the heart of the guild methodology. Your first time through will feel intense. By your third project, it'll feel natural.

## When Things Don't Go Smoothly

The walkthrough above makes it sound like a straight line. It won't be. Here's what actually happens and what to do about it.

**The agent gives you code that doesn't work at all.** The HTML page is blank, or shows an error in the browser console. Don't start over. Open your browser's developer tools (right-click the page, click "Inspect," then click the "Console" tab). If there are red error messages, copy them. Share the error and the code with your agent:

> "The page is blank. Here's the console error: [paste]. Here's the current code: [paste]. Fix it."

**The agent gives you code that works but isn't what you asked for.** The bookmark manager saves bookmarks but the layout is completely different from what you described, or it added features you didn't ask for. Don't accept it and move on. Be specific about what's wrong:

> "This works but it's not what I described. I asked for a minimal layout with the add form at the top and the list below. This has a sidebar I didn't ask for. Also remove the categories dropdown, that's not in the design doc. Stick to the design doc."

**You get an error message you don't understand.** Don't try to decode it yourself. Copy the entire thing and ask:

> "I don't understand this error. What does it mean and how do I fix it? [paste the full error]"

**The agent seems confused about your project.** In a long conversation, the agent might start contradicting earlier decisions or forget what you're building. This is context drift. The fix: start a new conversation, paste your design doc, summarize what's done so far, and continue from there.

**You're stuck and nothing is working.** Step back. Close the conversation. Take a break. When you come back, start fresh: paste the design doc, describe where you are, and describe the specific problem. A fresh context often solves problems that felt impossible in a degraded one.

None of this is failure. It's the normal process of building software. The next chapter goes deeper into debugging and handling errors.

## What Comes Next

This was a guided build. Your next two Apprentice portfolio projects will be self-directed. You choose what to build, you decompose it yourself, you manage the process from design doc to adversarial review.

Some ideas for self-directed projects:
- A flashcard study tool with spaced repetition
- A personal journal with daily entries and mood tracking
- A workout log that tracks exercises, sets, and progress over time
- A meal planner for the week with a grocery list generator
- A simple dashboard that displays weather and your daily tasks

Choose things you'll actually use. The best portfolio projects solve your own real problems. They show not just technical ability but the judgment to identify problems worth solving.

You have the methodology. You have the tools. Go build something.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Breaking Problems Down](04-breaking-problems-down.md) | **Your First Build** | [When Things Break →](06-when-things-break.md) |

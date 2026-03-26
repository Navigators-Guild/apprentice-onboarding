# Finding Answers

## Documentation, Search, and Knowing Where to Look

At some point, you're going to need information the agent doesn't have. Maybe you're using a library that was released after the agent's training data. Maybe the agent gives you outdated advice that doesn't work with the current version. Maybe you need to understand a concept well enough to make a design decision, not just get code that compiles.

This is where knowing how to find and evaluate information yourself becomes important. Not because the agent is unreliable, but because you need to be able to verify what it tells you and fill in the gaps when it can't.

## Reading Documentation

Documentation comes in a few forms, and knowing which one you need saves time.

**API reference docs** are the technical specification. Every function, every parameter, every return type. These are exhaustive and precise. In Rust, you'll see these on [docs.rs](https://docs.rs), which hosts documentation for every crate published to crates.io. They look dense, but you're not reading them cover to cover. You're searching for a specific function or type.

When you need to check whether a function exists or what arguments it takes:

> "I want to use the `colored` crate to make terminal output colorful. Check docs.rs/colored for the current API and show me how to make text bold and red."

Sharing the docs URL with the agent (or asking it to check) prevents it from guessing about an API that might have changed.

**Guides and tutorials** explain concepts and walk through common tasks. These are written for humans, not for completeness. The official Rust book ([doc.rust-lang.org/book](https://doc.rust-lang.org/book)) is one of the best programming guides ever written. You don't need to read it, but knowing it exists means you can point your agent at specific chapters when you need deeper understanding:

> "I keep getting borrow checker errors and I don't understand why. Read chapter 4 of the Rust book (on ownership) and explain the concept to me in simple terms, then fix my code."

**README files and examples** are usually the fastest way to understand a library. Most crates on GitHub have a README with usage examples. These tell you "here's how to use this in practice" rather than listing every function.

> "I want to use the `clap` crate for argument parsing. Find their README or examples directory and show me the recommended way to set up a CLI with subcommands."

**Changelogs and release notes** tell you what changed between versions. When the agent writes code that uses a function that doesn't exist, it might be using an old version of a library. The changelog tells you what was renamed, removed, or added.

## Evaluating What You Find

Not everything you find online is correct or current. A few rules of thumb:

**Check the date.** A tutorial from 2021 about a library that's been rewritten twice since then will lead you astray. Look for the version number it targets and compare to what you have installed.

**Prefer official sources.** The library's own documentation, README, and examples are maintained by the people who build it. Random blog posts and Stack Overflow answers might be outdated or wrong.

**Check if it compiles.** When in doubt, try the code. If the agent gives you something based on old docs and it doesn't compile, that's your signal to find current information.

**Multiple sources for important decisions.** If you're choosing between two libraries or two architectural approaches, don't rely on a single source. Ask the agent, but also check download counts on crates.io, look at the repo's recent activity (is it maintained?), and see if the guild community has opinions.

## Searching Effectively

When you need to find something specific, how you search matters.

**For Rust crates:** Start with [crates.io](https://crates.io). Search by keyword. Sort by downloads or recent activity. Read the crate description and check when it was last updated. A crate with 10 million downloads that was updated last month is a safer bet than one with 50 downloads from two years ago.

**For error messages:** Paste the exact error text into a search engine (with quotes). Someone else has almost certainly hit the same error. The Rust community is particularly good about this. The Rust Users Forum and r/rust on Reddit often have solutions.

**For "how do I" questions:** Ask your agent first. If the answer doesn't work, search with specific terms: "rust read csv file" rather than "how to process data in rust." Include the library name if you know it: "serde deserialize optional field."

**For understanding concepts:** The Rust book for language concepts. The Rustonomicon for unsafe/advanced topics (you won't need this as an apprentice, but know it exists). For general programming concepts, your agent is usually the best teacher: "explain what a trait is in Rust, like I've never programmed before."

## Sharing Documentation with Your Agent

One of the most effective patterns in agentic development is feeding documentation directly to your agent. Instead of hoping the agent's training data includes the library version you're using, give it the current source of truth.

**Share a URL:**
> "Here's the documentation for the API I want to use: [URL]. Read it and build a function that fetches the latest data."

**Share a README:**
> "Here's the README for the library we're using: [paste]. Follow their recommended patterns."

**Share an error with context:**
> "I got this error [paste] and I found this discussion about it: [URL]. Use that to fix the issue."

This closes the gap between what the agent knows from training and what's currently true. The more current information you feed it, the more accurate its output will be.

## When the Agent Is Wrong

It will happen. The agent will tell you a function exists and it doesn't. It will recommend a library that's been deprecated. It will explain a concept incorrectly because it's confusing two similar things.

Signs the agent might be wrong:

- The code it wrote doesn't compile, and the error says the function or type doesn't exist
- The library version it's referencing doesn't match what you have installed
- The explanation contradicts what you just read in the official docs
- It sounds confident but the details are vague or inconsistent

When you suspect the agent is wrong:

> "Are you sure about this? I can't find that function in the docs for version 4.6 of this library. Check the current API and correct if needed."

Agents respond well to being challenged with specifics. Saying "are you sure?" without details just gets "yes I'm sure" back. Saying "the docs say X but you said Y" gives the agent a concrete correction to work with.

This isn't adversarial. It's verification. The same principle from VDD applied to information, not just code.

## Exercises

1. Pick a Rust crate you haven't used before (try `serde`, `reqwest`, or `tokio`). Find it on docs.rs and crates.io. Read the README. Then ask your agent to explain what the crate does and when you'd use it. Compare the agent's explanation to what you read. Do they match? Is the agent's version accurate and current?

2. Introduce a version mismatch on purpose. Ask your agent to use an old pattern from a library (it will probably do this naturally if you just ask "use [library]" without specifying a version). When it breaks, find the changelog, identify what changed, and use the current documentation to fix it.

3. Find a Rust error message you don't understand. Before asking the agent, search for the exact error text online. Read the first few results. Then ask the agent to explain it. Which explanation was more helpful? Which was faster? This builds your intuition for when to search vs when to ask.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← When Things Break](06-when-things-break.md) | **Finding Answers** | [How We Build →](../02-the-methodology/01-how-we-build.md) |

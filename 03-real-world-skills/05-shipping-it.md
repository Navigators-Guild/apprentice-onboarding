# Shipping It

## The Gap Between "It Works" and "It's Done"

Your project compiles. It runs on your machine. The features work when you test them by hand. Is it done?

Not necessarily. The answer depends on the intended users, release channel, and acceptance criteria.

The gap between "it works on my machine" and "I can hand this to someone else and it works on theirs" is a common source of release failures. This chapter is about reducing it. The first half treats testing as evidence about specified behavior. The second covers delivery to other people.

Testing comes first because it creates repeatable feedback, and because agent-written tests have a specific failure mode you need to know about.

## Testing: Building Evidence

### Why Testing Matters

You've been verifying your projects by hand since Phase 1. Open the app, click buttons, check the output. That works for a while. But manual testing has problems:

- You forget to test things. You test the feature you just added but forget to check that the old features still work.
- You can't test everything every time. When your project has 20 features, manually checking all of them after every change takes longer than the change itself.
- You test what you think of. The bugs that ship are the ones you didn't think to look for.

Automated tests reduce these problems. They repeat the assertions you encoded, but they cannot check requirements you omitted and can become stale or flaky. A good suite is executable evidence for important behavior, not a complete description of everything the software should do.

### Unit Tests

A **unit test** tests one small piece of code in isolation. One function, one method, one logical unit.

```
// Does this function correctly identify a high-priority issue?
fn test_is_high_priority() {
    let issue = Issue::new("Fix bug", Priority::High);
    assert!(issue.is_high_priority());
}
```

Unit tests are usually fast, focused, and specific. A focused failure often narrows the affected behavior, though shared setup or multiple causes can still require diagnosis.

**When to use them:** For behavior with meaningful branches, transformations, calculations, or failure modes that can be checked efficiently in isolation. Test public behavior and risk, not a quota of one test per private function.

**What they catch:** Logic errors, off-by-one bugs, incorrect calculations, functions that don't handle edge cases.

**How to direct your agent:**
> "Write unit tests for the search function. Test: exact match, partial match, no match, empty query, query with special characters, case sensitivity."

### Integration Tests

An **integration test** tests how multiple pieces work together. Where unit tests check that individual functions are correct, integration tests check that the functions compose correctly.

```
// Does creating an issue and then searching for it actually work end-to-end?
fn test_create_then_search() {
    let db = TestDatabase::new();
    create_issue(&db, "Fix login bug", Priority::High);
    let results = search_issues(&db, "login");
    assert_eq!(results.len(), 1);
    assert_eq!(results[0].title, "Fix login bug");
}
```

Integration tests are slower than unit tests because they involve more moving parts. But they catch a class of bugs that unit tests miss: the assumptions one module makes about another.

**When to use them:** Whenever multiple modules interact. Storage + retrieval. Parsing + processing. Input + output.

**What they catch:** Interface mismatches between modules, incorrect assumptions about data formats, state management bugs, things that work in isolation but break when combined.

**How to direct your agent:**
> "Write integration tests that exercise the full workflow: create an issue, update its status, search for it, close it, verify it appears in the closed list. Use a temporary database for each test."

### Smoke Tests

A **smoke test** is the simplest possible check that your software works at all. "Does it start? Does the main command produce output instead of crashing?" The name comes from hardware testing: plug it in and see if smoke comes out.

```
// Does the binary even run?
fn test_help_flag() {
    let output = Command::new("guild-scaffold").arg("--help").output();
    assert!(output.status.success());
}
```

Smoke tests aren't thorough. They don't check that features work correctly. They check that the software isn't fundamentally broken. A failing smoke test means something is very wrong.

**When to use them:** Give shipped binaries at least one inexpensive startup or `--help` check when practical. A smoke test is a quick signal, not necessarily the first test a framework runs.

**What they catch:** Build failures, missing dependencies, configuration errors, crashes at startup.

**How to direct your agent:**
> "Add smoke tests for every subcommand. Each test runs the command with --help and verifies it exits successfully. Also test that running with no arguments produces a useful error message instead of crashing."

### Property-Based Tests (Prop Tests)

This is where testing gets interesting. Instead of writing specific test cases ("does search find 'login'?"), you describe *properties* that should always be true, and the test framework generates hundreds or thousands of random inputs to try to find a violation.

```
// Property: any issue we create should be retrievable by its ID.
// The framework generates random titles, priorities, and labels to try to break this.
proptest! {
    fn test_roundtrip(title in ".*", priority in 0..3u8) {
        let db = TestDatabase::new();
        let id = create_issue(&db, &title, priority.into());
        let retrieved = get_issue(&db, id);
        assert_eq!(retrieved.title, title);
    }
}
```

The framework doesn't just try random inputs once. When it finds a failing case, it *shrinks* it: it finds the simplest possible input that still triggers the failure. Instead of "your code fails on this 500-character string," you get "your code fails when the title contains a null byte."

**When to use them:** For data processing, serialization/deserialization, any function that should work for all valid inputs. Especially valuable for finding edge cases you'd never think to test by hand.

**What they catch:** Unicode handling bugs, boundary conditions, assumptions about input ranges, serialization round-trip failures. The things you'd never think to test because you'd never think of that specific input.

**How to direct your agent:**
> "Write property-based tests using proptest for the issue serialization. The property: any issue that's serialized to JSON and then deserialized should be identical to the original. Generate random titles (including empty strings, very long strings, and strings with special characters), random priorities, and random label lists."

### Formal Verification

Formal methods go beyond example-based testing by checking a stated property under an explicit model. A proof is only as broad as the property, assumptions, and code included in that model; it is not a certificate that the whole application meets its users' needs.

**Kani** is one Rust model checker. A proof harness can check properties such as overflow or out-of-bounds access across the states represented by the harness. Start with Kani's [official tutorial and limitations](https://model-checking.github.io/kani/).

**When to use it:** For safety-critical code, cryptographic implementations, numeric processing, or any code where a subtle bug has serious consequences. Not every project needs formal verification. But knowing it exists puts it in your toolkit for when it matters.

**What it can catch:** Arithmetic overflow, out-of-bounds access, reachable assertion failures, and violations of logical properties represented by the harness.

**How to direct your agent:**
> "Add Kani proof harnesses for the priority arithmetic. Prove that converting between priority levels and numeric values can never overflow and that the round-trip is always correct."

You'll encounter formal methods more as you advance. A narrowly proved property can be stronger evidence for that property than sampled tests, while still saying nothing about omitted requirements or assumptions. Match the method to the risk and question.

## The Tautological Test Problem

Here's the agent-specific failure mode you need to know about. When you ask an agent to write tests, it will sometimes write **tautological tests**: tests that verify the code does what the code does, rather than what it *should* do.

Here's what a tautological test looks like:

```
fn test_format_priority() {
    let issue = Issue::new("Bug", Priority::High);
    // This just re-implements the function being tested
    let expected = format!("[HIGH] Bug");
    assert_eq!(issue.format(), expected);
}
```

This example is actually acceptable if `"[HIGH] Bug"` comes directly from the design specification: it is an independently known expected value. The tautology appears when the test calls the production formatter, copies its branching logic, or derives the expected value from the same implementation details.

A good test looks like this:

```
fn test_format_priority() {
    let issue = Issue::new("Bug", Priority::High);
    // This literal comes from the documented output contract.
    assert_eq!(issue.format(), "[HIGH] Bug");
}
```

This test knows what the output should look like based on the *requirements*, not the implementation. If someone changes the format function, the test catches it because the expectations are independent.

**How to catch this:** Review your agent's tests the same way you review its code. For each test, ask: "Does this test know what the right answer is independently, or is it just recomputing what the code computes?" If it's the latter, push back:

> "This test re-implements the formatting logic. The test should check against independently known correct values. Write test cases where you specify the exact expected output as string literals, based on what the format *should* be according to the design doc."

Tests need adversarial review too. A test suite full of tautologies gives you false confidence. Everything passes, but nothing is actually being verified.

## Mutation Testing: Test the Tests

Code coverage asks whether a test executed a line. **Mutation testing** asks whether the tests notice when that line is changed. A mutation tool makes small edits—such as reversing a comparison or replacing a return value—and runs the suite. If the tests still pass, the mutation was **missed**, which points to a weak assertion, untested behavior, or occasionally an equivalent change that does not alter behavior.

For a Rust project:

```bash
cargo install --locked cargo-mutants
cargo mutants
```

Read the `missed` results; do not chase a perfect score blindly. Add a requirement-based test when the mutation reveals behavior that matters, and document equivalent or irrelevant mutants. Mutation runs can be expensive, so start locally on a small crate or changed module, then decide whether a bounded run belongs in CI. The [cargo-mutants guide](https://mutants.rs/) explains outcomes, filters, and [CI trade-offs](https://mutants.rs/ci.html).

## Finding Edge Cases

Edge cases are the inputs and situations that live at the boundaries. They're where bugs hide because they're what nobody thinks about during normal development.

Training yourself to think about edge cases is one of the most valuable skills you can develop. Here's a systematic way to do it:

**Empty inputs.** What happens with an empty string? An empty list? A file with no content? Zero?

**Boundary values.** The first item. The last item. Exactly at the limit. One past the limit. The maximum integer value. Negative numbers when only positives are expected.

**Special characters.** Unicode, emoji, null bytes, newlines in the middle of strings, extremely long strings, strings that look like code or commands (SQL injection, path traversal).

**Concurrent and timing issues.** What if two operations happen at the same time? What if the operation is interrupted halfway through? What if the file is being written by another process?

**State transitions.** What if you try to close an already-closed issue? What if you delete something that other things depend on? What if the config file exists but is empty?

**Resource limits.** What if there are 10,000 issues? What if the disk is full? What if a file name is 255 characters?

You won't test all of these for every project. But running through the categories mentally before you write tests (and before you direct your agent to write tests) catches the ones that matter for your specific project.

> "Before writing tests, let me describe the edge cases I want covered: empty title, title with emoji and special characters, duplicate titles, extremely long title (10,000 chars), creating an issue when the storage file doesn't exist yet, creating an issue when the storage file is corrupted JSON."

## Cross-Platform Testing

Your project works on your machine. Does it work on someone else's? Does it work on Windows if you built it on Linux? On macOS?

Cross-platform issues are real and common. File paths work differently on Windows (backslashes vs forward slashes). Line endings differ. Available system libraries differ. Terminal capabilities differ.

**Virtual machines** let you test on platforms you don't normally use. Tools like VirtualBox, UTM (for Mac), or WSL (Windows Subsystem for Linux, if you're on Windows already) let you run different operating systems on your computer.

**GitHub Actions** (or similar CI systems) can run your tests on multiple platforms automatically. You push your code, and it gets tested on Linux, macOS, and Windows without you doing anything. When you're ready to set this up, tell your agent:

> "Create a GitHub Actions workflow that runs cargo test on Ubuntu, macOS, and Windows. Run clippy and cargo fmt --check as well."

For the apprentice path, you do not need CI on every exercise. Before shipping, test every platform you claim to support; a single-platform tool should state that limit rather than pretending to be cross-platform.

## Delivery: Getting It to People

Your code is tested. Now you need to get it into someone else's hands. There are several levels of this, from simple to polished.

### "Clone My Repo and Build It"

The simplest form of distribution. Your code is on GitHub. Someone clones it and runs `cargo build --release`. This works but it requires the recipient to have Rust installed. Fine for guild members, not great for the general public.

### GitHub Releases

A step up. You build the binary for your platform, create a release on GitHub, and attach the binary as a downloadable file. Someone can download and run it without installing Rust.

Here's the process:

```
cargo build --release
```

This produces an optimized binary in `target/release/`. On GitHub, go to your repo, click "Releases," then "Create a new release." Tag it with a version number (like `v0.1.0`), write release notes, and upload the binary from `target/release/`.

**Writing good release notes:**

- Lead with what the tool does (for people who haven't seen it before)
- List what's new or changed since the last release
- Include installation instructions ("download the binary, put it in your PATH")
- Mention known issues if any
- Keep it short. A few bullet points, not an essay

> "Write release notes for v0.1.0 of the issue tracker. This is the first release. Describe what the tool does, list the features, and include installation instructions for Linux, macOS, and Windows."

### Continuous Integration (CI)

**What CI is.** Continuous Integration runs configured checks on events such as pushes and pull requests. A fresh runner checks out the selected revision, runs specified commands, and reports status. GitHub Actions is built into GitHub; current standard-runner billing is described in [GitHub's documentation](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

**Why it exists.** You'll catch problems in CI that you'd never find locally:

- Code that compiles on Linux but not Windows (path separator issues, missing dependencies)
- Tests that pass on your machine but fail on a clean environment because you have something installed locally that isn't in the project
- Formatting inconsistencies between different contributors
- Dependencies that updated and broke something while you weren't looking

**The folder convention.** GitHub Actions reads workflow files from a specific magic folder: `.github/workflows/` in your repository root. Any `.yml` file in that folder is treated as a workflow. You can have multiple workflows (one for tests, one for releases, one for docs). The folder and the filename pattern are what turn an ordinary file into something GitHub runs — there's no other registration step.

**The shape of a workflow file.** Workflows are written in YAML, a data format similar in intent to JSON but using indentation instead of braces. You saw JSON back in the foundations chapter; YAML conveys the same kind of nested key-value data with different punctuation. Here's the smallest useful Rust workflow:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: dtolnay/rust-toolchain@stable
      - run: cargo build --verbose
      - run: cargo test --verbose
      - run: cargo clippy -- -D warnings
      - run: cargo fmt --check
```

The three top-level keys:

- **`name`** — a label for this workflow that shows up in the GitHub Actions tab.
- **`on`** — the triggers. This workflow runs on any push and any pull request. Other common triggers: `schedule` (cron), `workflow_dispatch` (manual button), `release` (when you publish a release).
- **`jobs`** — the actual work, organized as one or more named jobs. Each job picks a **runner** (`ubuntu-latest`, `macos-latest`, or `windows-latest`) and runs a list of **steps** in order. GitHub's standard hosted runners are currently free for public repositories; private-repository quotas and larger runners differ, so check [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions). Steps are either `uses` (call a reusable action such as `actions/checkout@v6`) or `run` (execute a shell command).

If any `run` step exits non-zero, the job fails and CI reports red. Otherwise it reports green.

**Indentation matters in YAML.** Two-space indent is the convention. Tabs will break the file. One misaligned key breaks the whole workflow. The error messages are usually clear about which line is the problem.

**Setting it up for your project.** Ask your agent:

> "Create a GitHub Actions workflow file at `.github/workflows/ci.yml`. It should:
>
> - Run on every push and every pull request
> - Test on Ubuntu, macOS, and Windows (use a matrix strategy)
> - Run cargo build, cargo test, cargo clippy -- -D warnings, and cargo fmt --check
> - Use the stable Rust toolchain"

The agent will generate a YAML file more sophisticated than the one above (with a matrix of operating systems). Create the file, commit it, push.

**Checking the result.** Go to your repository on github.com and click the **Actions** tab at the top. You'll see a list of recent workflow runs — the most recent is the one from the push you just made. A yellow dot means pending, a green checkmark means passed, a red X means failed. Click into any run to see the step-by-step log. If a step failed, click the red step to see the exact output — Rust compile errors, test failures, and clippy lints are all there verbatim.

The debugging loop is: fail, read the log, push a fix, check the new run. You'll get fast at this once you've done it a few times.

**CI should match the delivery risk.** For software other people depend on, automated checks on proposed changes are a strong baseline. A private one-off script may need less infrastructure; a public binary or library needs more. Set checks up before the release process depends on memory.

### Cross-Compilation

Building for a target different from the machine doing the build is cross-compilation. Rust can add many target standard libraries, but native linkers and system dependencies are platform-specific. In particular, do not assume a Linux runner can produce a working macOS binary. The simplest reliable beginner setup is a GitHub Actions matrix that builds and tests each artifact on its matching Linux, macOS, or Windows runner.

> "Extend the GitHub Actions workflow to build release binaries for Linux (x86_64), macOS (x86_64 and aarch64), and Windows (x86_64) when I push a version tag. Attach all binaries to a GitHub release automatically."

This is a common way Rust projects distribute binaries. Test the downloaded artifacts on the supported operating systems and document CPU architecture, checksums, and any runtime requirements.

### cargo publish

If your tool is useful to other Rust developers, you can publish it to [crates.io](https://crates.io), Rust's package registry. Then anyone can install it with `cargo install your-tool-name`.

**Publishing is optional.** Most apprentice projects should live on GitHub as source code and stop there. Publish only when the tool is useful to others and you are ready to maintain it. A published version cannot be overwritten or selectively deleted, so review the package before upload.

**Higher standards than pushing to GitHub:**

**Metadata should be complete.** Cargo's [publishing guide](https://doc.rust-lang.org/cargo/reference/publishing.html) requires or strongly expects a description and license information; repository, homepage, and README improve provenance and documentation. Keywords and categories improve discovery but are optional.

**Documentation must exist.** A README at minimum. Ideally, doc comments on your public API so [docs.rs](https://docs.rs) can generate reference documentation automatically.

**Tests must pass.** Run `cargo test` and `cargo publish --dry-run` before every publish. These checks reduce packaging mistakes; they do not prove compatibility or security.

**Versions are durable.** Once you publish version 0.1.0, you cannot overwrite that version or selectively delete its code. You can publish 0.1.1, and you can [yank](https://doc.rust-lang.org/cargo/commands/cargo-yank.html) 0.1.0 so new dependency resolution avoids it. crates.io added deletion of an entire crate only under narrow low-impact conditions; the [deletion criteria](https://blog.rust-lang.org/2025/02/05/crates-io-development-update/) do not make publishing a reversible editing workflow.

**The name is globally unique and first-come.** Choose a clear, appropriate name and check crates.io before building branding around it. Do not publish an empty placeholder just to reserve a name.

#### Step-by-step publishing walkthrough

Assume you have a mature tool ready to ship. Here's the full path from zero to published.

**1. Create a crates.io account.** Go to [crates.io](https://crates.io) and click **Log in with GitHub** in the top right. This signs you in via GitHub OAuth — you don't create a separate password. The first sign-in creates your account automatically.

**2. Verify your email address.** crates.io requires a verified email before you can publish. Click your profile → **Account Settings** → add an email address if none is listed → click the verification link in the email that arrives. Publishing will fail with a clear error if this step is skipped.

**3. Generate an API token.** On crates.io, go to **Account Settings** → **API Tokens** → **New Token**. Give it a clear purpose, the minimum publish permissions and crate scope you need, and a practical expiration. Store the one-time value in a password manager.

**4. Log cargo into crates.io with the token.**

```
cargo login
```

Paste the token at Cargo's prompt so it does not appear in shell history. This stores it in Cargo's local credentials file. Revoke it on crates.io when it is no longer needed or if it may have leaked.

**5. Fill out your Cargo.toml metadata.** Open `Cargo.toml` and make sure the `[package]` section has all the required fields:

```toml
[package]
name = "my-tool"
version = "0.1.0"
edition = "2024"
description = "A one-sentence summary of what the tool does"
license = "MIT OR Apache-2.0"
repository = "https://github.com/YOUR-USERNAME/my-tool"
readme = "README.md"
keywords = ["cli", "productivity"]
categories = ["command-line-utilities"]
```

Pick keywords and categories carefully — crates.io uses them for search. You can find the full category list at [crates.io/categories](https://crates.io/categories).

**6. Dry run.** Always do this before publishing:

```
cargo publish --dry-run
```

This packages the crate as if you were publishing, runs the checks, and reports any problems without actually sending anything to crates.io. Fix every warning. Common issues: missing README file referenced in Cargo.toml, files larger than the size limit, unrelated files accidentally included.

**7. Publish.**

```
cargo publish
```

It uploads the crate archive and crates.io indexes the release. Index propagation and docs.rs builds are asynchronous and can fail, so verify the crate page, installation command, and documentation build instead of promising a time.

**8. Tag the release in git.** Create and push a git tag that matches the version you just published:

```
git tag v0.1.0
git push origin v0.1.0
```

This makes it easy for future-you and your users to find the exact code that corresponds to any published version.

#### Publishing follow-up versions

To publish a new version later, bump the `version` field in `Cargo.toml` (following semantic versioning), commit, `cargo publish --dry-run`, `cargo publish`, tag, push. That's the loop.

### The Packaging Checklist

Before you ship anything, run through this:

- **Does it build from a clean checkout?** Clone a fresh copy and build it. Don't rely on anything in your local environment that isn't in the repo.
- **Do all tests pass?** `cargo test`. No skipping, no ignoring failures.
- **Can the tests detect meaningful faults?** Review assertions and run a scoped `cargo mutants` pass where its runtime is proportionate to the project.
- **Does clippy pass?** `cargo clippy -- -D warnings`. Clean code ships cleaner.
- **Does CI pass?** If you have GitHub Actions, the green checkmark is your baseline. Don't ship if CI is red.
- **Is there a README?** What does the tool do, how do you install it, how do you use it. Write it for someone who's never seen your project before.
- **Are there release notes?** What changed since the last version. What's new, what's fixed, what's known-broken.
- **Is the version number correct?** Follow the project's compatibility policy and Cargo's [SemVer compatibility guidance](https://doc.rust-lang.org/cargo/reference/semver.html). Pre-1.0 compatibility and Rust package changes are more nuanced than "breaking means major."
- **Are secrets excluded?** No API keys, no tokens, no `.env` files in the repo. Check your `.gitignore`.
- **Does it work on a fresh machine?** This is what VMs and CI are for. If you only tested on your machine, you haven't tested enough.

## Exercises

1. Take your issue tracker from Phase 2 and add a complete test suite. Start with smoke tests (does it run?), then unit tests for each piece of logic, then integration tests for workflows (create → update → search → close). Run `cargo test` and make sure everything passes. Then ask your agent: "review these tests for tautological testing." Fix any it finds.

2. Write property-based tests for your issue tracker's serialization. Use proptest to generate random issues and verify the round-trip: serialize to JSON, deserialize back, compare to original. What edge cases does proptest find that your hand-written tests missed?

3. Run your issue tracker's tests on a different platform than you developed on. If you're on Linux, test on macOS or Windows (via VM, WSL, or GitHub Actions). Document what broke and what you had to fix. Cross-platform issues are easier to find than to predict.

4. Package one of your projects for distribution. Create a GitHub release with a built binary. Write a README that explains what it is, how to install it, and how to use it. Have someone else (another guild member, a friend) try to use it from just the README and release binary. Their experience will teach you more about shipping than any guide can.

5. Set up a GitHub Actions workflow that runs your full test suite (tests, clippy, formatting) on every push. Make it test on at least two platforms. Watch it catch something you missed locally. This is the beginning of CI/CD, and it's how professional projects stay healthy.

6. Install cargo-mutants and run it on the issue tracker. Classify every missed mutant as a missing test, equivalent behavior, or behavior outside the design contract. Add tests for the first category, rerun the relevant mutants, and record what changed in `LEARNING_LOG.md`.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Security](04-security.md) | **Shipping It** | [On Your Own →](../04-proving-it/01-on-your-own.md) |

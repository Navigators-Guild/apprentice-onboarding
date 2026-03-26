# Security

## The Code Your Agent Writes Is Probably Insecure

This isn't a knock on agents. It's a fact about how they work. Agents optimize for getting things working. Security is almost never the thing that makes something work. It's the thing that stops it from being exploited. Those are different goals, and when they conflict, the agent will default to the one you asked for: working code.

This means agent-generated code tends to:

- Skip input validation because the code works without it
- Use default configurations that are convenient but insecure
- Hardcode values that should be secrets
- Use deprecated or vulnerable patterns that still compile fine
- Trust data that comes from outside the program
- Ignore error cases that could leak information

VDD catches some of this. The adversarial review will flag obvious issues. But security review is a specific discipline, and a general-purpose adversary will miss things that a security-focused review would catch. This chapter is about adding that security layer.

## The Vulnerabilities You Need to Know About

You don't need to become a security researcher. But you need to recognize the categories of problems so you can direct your agent to avoid them and catch them when it doesn't.

### Injection

Injection happens when user input gets treated as instructions. The most common form is **SQL injection**: someone types `'; DROP TABLE users; --` into a search box, and if the code puts that string directly into a database query, it executes as a command and deletes the table.

It's not just SQL. Command injection (user input passed to a shell command), path traversal (user input used to construct a file path, allowing `../../etc/passwd`), and template injection all follow the same pattern: untrusted data crosses a boundary where it gets interpreted as code.

**The fix is always the same:** Never build commands by concatenating strings with user input. Use parameterized queries for SQL, safe path construction APIs for file paths, and proper escaping for shell commands.

**What to tell your agent:**
> "Use parameterized queries for all database operations. Never construct SQL by string concatenation. For file paths, use Rust's Path API and validate that the resolved path stays within the expected directory."

### Exposed Secrets

API keys in source code. Tokens in config files that get committed to git. Database passwords in error messages. Debug output that includes authentication headers.

Agents are particularly bad about this because they write examples with placeholder values that look like real credentials (`sk-1234567890abcdef`), and sometimes those placeholders become the real values when you paste in your actual key and forget to move it to an environment variable.

**What to tell your agent:**
> "All secrets come from environment variables. Never log, print, or include secrets in error messages. Add a .gitignore that excludes .env files. If a secret is needed, fail with a message that says which environment variable to set, without revealing any value."

### Insecure Defaults

An agent will pick the easiest way to make something work. For a web server, that might mean binding to `0.0.0.0` (accessible from any network) instead of `127.0.0.1` (localhost only). For cryptography, it might mean using an outdated algorithm that's still available in the library. For permissions, it might mean making everything public because that's simpler than thinking about access control.

**What to tell your agent:**
> "Use secure defaults. Bind servers to localhost unless explicitly configured otherwise. Use current cryptographic standards (AES-256-GCM, SHA-256 minimum, no MD5, no SHA-1 for security purposes). Set the most restrictive permissions that still allow the program to function."

### Missing Validation

The agent builds a function that takes a username and looks it up. It works when you pass it "alice". But what about an empty string? A string with 10 million characters? A string with null bytes? A string containing shell metacharacters?

Every boundary where data enters your program from the outside world (user input, API responses, file contents, environment variables) is a place where validation should happen. Agents skip this because it's not part of "making it work."

**What to tell your agent:**
> "Validate all external input at the point where it enters the program. Set reasonable length limits. Reject or sanitize unexpected characters. Don't trust data from files, network responses, or user input. Treat all external data as potentially malicious."

### Dependency Vulnerabilities

Your code might be secure, but what about the libraries it uses? A vulnerability in a dependency is a vulnerability in your project. This is called a **supply chain** risk: you didn't write the problem, but you shipped it.

Rust has good tooling for this, which we'll cover below.

## Static Security Scanning

Static scanning means checking code for security issues without running it. These tools read your source code (and your dependencies) and flag known problems. They're automated, fast, and should be part of your regular workflow.

### cargo audit

Checks your dependencies against the RustSec advisory database. If a library you use has a known vulnerability, cargo audit tells you.

```
cargo install cargo-audit
cargo audit
```

Run this regularly. Run it before shipping. Add it to your CI pipeline. If it flags something, either update the dependency to a patched version or find an alternative.

### cargo deny

Goes further than cargo audit. Checks for vulnerabilities, but also for license compliance (is this dependency's license compatible with yours?), duplicate dependencies (multiple versions of the same crate, which increases attack surface), and banned crates (ones your project has decided not to use).

```
cargo install cargo-deny
cargo deny init     # creates a deny.toml config
cargo deny check
```

### clippy security lints

You already use clippy for code quality. Some clippy lints are security-relevant. Running `cargo clippy -- -D warnings` catches things like using `unwrap()` on user input (which can panic and crash), or using string formatting where parameterized queries should be used.

### Putting it together

> "Add a security check target to our workflow. It should run cargo audit, cargo deny check, and cargo clippy -- -D warnings. All three must pass before we consider the code ready to ship."

## Adversarial Security Review

Static tools catch known patterns. They don't reason about your specific code's logic. For that, you need a security-focused adversarial review, the same technique from VDD but with a specific lens.

### The Security Roast

Open a separate conversation with an agent. Give it a fresh context (no relationship drift). Prompt it specifically for security:

> "You are a security auditor reviewing this code. Your job is to find every security vulnerability, every place where untrusted input is handled unsafely, every hardcoded secret, every insecure default, every missing validation. Be thorough and assume the attacker is sophisticated. Here is the code: [paste]"

This is different from a general adversarial review. A general review might say "this function is too long." A security review says "this function reads a file path from user input and passes it to std::fs::read without checking for path traversal."

### What the Security Adversary Looks For

Direct it with specifics:

> "Specifically check for:
> - SQL injection or command injection opportunities
> - Path traversal vulnerabilities
> - Hardcoded secrets or credentials
> - Missing input validation on any external data
> - Insecure cryptographic choices
> - Error messages that leak internal details
> - Denial of service vectors (can an attacker crash it with crafted input?)
> - Race conditions in file or resource access
> - Dependencies with known vulnerabilities"

### Fresh Context Matters

Just like VDD's general adversarial review, do the security review in a fresh context every time. An agent that's been helping you build the code for hours has absorbed your assumptions. It "understands" why you made certain choices. A fresh agent doesn't. It questions everything, which is exactly what you want for security.

### Iterate

Fix what the security review finds. Then run the review again. Fresh context again. Just like VDD: repeat until the adversary is inventing problems instead of finding real ones.

## Thinking Like an Attacker

Beyond tools and reviews, develop the habit of asking "how could this be abused?" about your own code. This is adversarial thinking applied specifically to security.

For every input your program accepts, ask:
- What if this is empty?
- What if this is enormous?
- What if this contains characters I didn't expect?
- What if this is technically valid but semantically malicious?
- What if someone sends a million of these?

For every output your program produces, ask:
- Does this reveal anything an attacker could use?
- Does this error message tell someone how to exploit the failure?
- Does this log contain data that should be private?

For every dependency you add, ask:
- Is this actively maintained?
- Does it have known vulnerabilities?
- Do I need all of this library, or just one function? (Smaller dependency = smaller attack surface)

This isn't paranoia. It's engineering discipline. The same way you verify that features work, you verify that they can't be abused.

## Security as Part of the Process

Security isn't a phase you do at the end. It's a consideration at every stage:

**Design phase:** "Are there any security-sensitive operations in this project? User data, authentication, file access, network requests? If so, what are the threats and how do we mitigate them?"

**Build phase:** Tell the agent about security requirements from the start. "Validate all input. Use parameterized queries. No hardcoded secrets." Don't wait until the code is written to think about this.

**Review phase:** Include security in every adversarial review, not just a dedicated security review at the end. The earlier you catch a vulnerability, the cheaper it is to fix.

**Ship phase:** Run cargo audit and cargo deny before every release. Not occasionally. Every time.

## Exercises

1. Take one of your existing projects and run cargo audit and cargo deny on it. Are there any flagged dependencies? If so, update or replace them. If not, good. Now run the security roast: paste your code into a fresh agent conversation with the security auditor prompt above. How many issues does it find? Fix them and run the roast again.

2. Build a deliberate vulnerability and then detect it. Ask your agent to build a simple tool that takes a filename as a command-line argument and displays the file's contents. Don't mention security. Then review the code: does it prevent path traversal? Can you read `/etc/passwd` with it? Now fix it and write a test that proves the vulnerability is closed.

3. Review another guild member's code specifically for security. Use the security adversary checklist. Write up your findings with specific line references and suggested fixes. This is harder than it sounds because you need to read code you didn't write and reason about how it could be exploited.

4. Build a security scanner CLI tool in Rust. It should take a project path as input and run a series of checks: cargo audit, cargo deny, clippy security lints, and then use an AI agent (via API or MCP) to do an automated security review of the source code. Aggregate the results into a report with severity levels. This is an advanced project: it involves file I/O, process spawning, API integration, and output formatting. It could become a tool in the guild toolkit.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Project Architecture](03-project-architecture.md) | **Security** | [Shipping It →](05-shipping-it.md) |

# Security

## Treat Agent-Assisted Code as Untrusted Until Verified

No percentage justifies declaring all agent-generated code secure or insecure. The useful operating rule is simpler: generated code has not earned trust until it has passed the same threat modeling, review, testing, dependency checks, and operational controls you would require from human-written code. OWASP's current [Secure Coding with AI guidance](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html) recommends independent verification and warns that coding agents can also run commands, install packages, and modify repositories.

Common failure modes worth checking include:

- Skip input validation because the code works without it
- Use default configurations that are convenient but insecure
- Hardcode values that should be secrets
- Use deprecated or vulnerable patterns that still compile fine
- Trust data that comes from outside the program
- Ignore error cases that could leak information

VDD can organize the evidence, but a general-purpose agent review is neither independent proof nor a substitute for security expertise. This chapter adds a threat-focused layer and shows where automated tools stop.

## The Vulnerabilities You Need to Know About

You don't need to become a security researcher. But you need to recognize the categories of problems so you can direct your agent to avoid them and catch them when it doesn't.

### Injection

Injection happens when user input gets treated as instructions. The most common form is **SQL injection**: someone types `'; DROP TABLE users; --` into a search box, and if the code puts that string directly into a database query, it executes as a command and deletes the table.

It's not just SQL. Command injection (user input passed to a shell command), path traversal (user input used to construct a file path, allowing `../../etc/passwd`), and template injection all follow the same pattern: untrusted data crosses a boundary where it gets interpreted as code.

**The fix depends on the interpreter boundary:** Use parameterized queries for SQL. Avoid invoking a shell when a process API can pass arguments directly. For file access, normalize and constrain paths, then enforce authorization on the resolved target. Output encoding is context-specific; one generic "sanitize" function does not make every sink safe.

**What to tell your agent:**
> "Use parameterized queries for all database operations. Never construct SQL by string concatenation. For file paths, use Rust's Path API and validate that the resolved path stays within the expected directory."

### Exposed Secrets

API keys in source code. Tokens in config files that get committed to git. Database passwords in error messages. Debug output that includes authentication headers.

Generated examples sometimes contain credential-shaped placeholders. Keep placeholders obviously fake, and never replace them with real values inside source, prompts, or tracked files.

**What to tell your agent:**
> "Use the provider's credential helper or secret manager when available. Otherwise read the named environment variable at runtime. Never log, print, commit, or include the value in an error. Add `.env` to `.gitignore` before creating it and provide only fake values in `.env.example`."

### Insecure Defaults

Generated code may choose a permissive or convenient default unless the requirement names the boundary. A development server might bind to `0.0.0.0` (all interfaces) instead of `127.0.0.1` (loopback only), or an authorization rule might grant more access than the use case needs.

**What to tell your agent:**
> "Use secure defaults. Bind development servers to localhost unless remote access is an explicit requirement. Use a maintained, high-level cryptography library and the protocol's current recommended construction; do not invent cryptographic primitives or choose algorithms without the use-case requirements. Set the most restrictive permissions that still allow the program to function."

### Missing Validation

The agent builds a function that takes a username and looks it up. It works when you pass it "alice". But what about an empty string? A string with 10 million characters? A string with null bytes? A string containing shell metacharacters?

Every boundary where data enters your program from the outside world—user input, API responses, file contents, or environment variables—needs an explicit trust decision. Generated implementations may omit that decision when the requirement names only the happy path.

**What to tell your agent:**
> "Validate all external input at the boundary against the domain's allowed shape and size. Parse into typed values, reject invalid input clearly, and encode output for its specific destination. Do not silently strip characters unless the product requirements define that normalization."

### Dependency Vulnerabilities

Your code also inherits risk from libraries, build tools, and distribution channels. A dependency advisory may or may not affect the features and paths you use, so trace reachability and exposure instead of either ignoring it or assuming automatic exploitability. This is part of **software supply-chain** risk.

Rust has good tooling for this, which we'll cover below.

### Agent-Specific Supply Chain and Prompt Injection

A coding agent may read instructions from repository files, issues, dependency documentation, webpages, or tool output. Malicious or irrelevant instructions in those sources can try to redirect the agent, expose credentials, install a package, or expand its scope. A compromised MCP server or package can also misuse the permissions you granted it.

Mitigate this by treating external content as data, granting least privilege, using a sandbox for unfamiliar code, reviewing install scripts and diffs, pinning dependencies where practical, and requiring confirmation before destructive, publishing, credential, or external-write actions. OWASP's [AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) covers prompt injection, tool abuse, memory poisoning, and excessive autonomy.

## Static Security Scanning

Automated checks cover different surfaces. The tools below inspect dependency advisories and project policy; Clippy analyzes Rust patterns. None is a complete application-security scanner, so keep their outputs separate.

### cargo audit

Checks dependency versions in `Cargo.lock` against the RustSec advisory database. It can report known advisories; a clean result does not mean the dependency or your code is vulnerability-free.

```
cargo install --locked cargo-audit
cargo audit
```

Run this regularly. Run it before shipping. Add it to your CI pipeline. If it flags something, either update the dependency to a patched version or find an alternative.

### cargo deny

Adds configurable checks for advisories, licenses, sources, duplicate versions, and banned crates. You must review `deny.toml`: license compatibility and acceptable duplicates depend on project policy, and duplicate versions are a maintenance signal rather than automatic vulnerabilities.

```
cargo install --locked cargo-deny
cargo deny init     # creates a deny.toml config
cargo deny check
```

### Clippy is not a security scanner

You already use Clippy for correctness, style, and suspicious Rust patterns. Some findings may reduce crash or misuse risk, but Clippy does not understand your trust boundaries and does not generally detect SQL injection or prove that user input is safe. Keep `cargo clippy -- -D warnings` in CI as a separate quality signal, not as a security verdict.

### Putting it together

> "Add CI jobs for `cargo audit`, our configured `cargo deny check`, and `cargo clippy -- -D warnings`. Pin or deliberately update the workflow dependencies. Explain what each check covers, and do not describe a green run as proof that the release is secure."

## Adversarial Security Review

Static tools catch known patterns. They don't reason about your specific code's logic. For that, you need a security-focused adversarial review, the same technique from VDD but with a specific lens.

### The Security Roast

Use an independent review context or reviewer and prompt it specifically for security. Do not paste proprietary code, personal data, or secrets into a service that is not authorized to receive them:

> "Act as a security reviewer. Identify trust boundaries, assets, attacker-controlled inputs, dangerous sinks, authorization decisions, secrets, dependencies, and denial-of-service risks. For each finding, cite the file and line, show the exploit precondition, assign confidence, and propose a verification test. Say when evidence is insufficient. Do not modify code."

This is different from a general adversarial review. A general review might say "this function is too long." A security review says "this function reads a file path from user input and passes it to std::fs::read without checking for path traversal."

### What the Security Adversary Looks For

Direct it with specifics:

> "Specifically check for:
>
> - SQL injection or command injection opportunities
> - Path traversal vulnerabilities
> - Hardcoded secrets or credentials
> - Missing input validation on any external data
> - Insecure cryptographic choices
> - Error messages that leak internal details
> - Denial of service vectors (can an attacker crash it with crafted input?)
> - Race conditions in file or resource access
> - Dependencies with known vulnerabilities"

### Independence Matters

The builder can review its own output, but a second context, model, human, or specialized tool reduces shared assumptions. Fresh context alone does not create expertise or independence: provide the requirements, threat model, supported environment, and relevant code, then verify each reported finding yourself.

### Iterate

Triage findings by evidence and impact, reproduce them where safe, fix confirmed issues, and add regression tests. Stop when the defined security acceptance criteria pass and residual risks are documented—not when a model becomes repetitive or starts inventing problems.

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
- Do I need this dependency, and are its publisher, maintenance, features, and transitive dependencies acceptable?

This is engineering discipline. Alongside functional checks, gather evidence about plausible abuse cases and document the security limits you have not established.

## Security as Part of the Process

Security isn't a phase you do at the end. It's a consideration at every stage:

**Design phase:** "Are there any security-sensitive operations in this project? User data, authentication, file access, network requests? If so, what are the threats and how do we mitigate them?"

**Build phase:** Tell the agent about security requirements from the start. "Validate all input. Use parameterized queries. No hardcoded secrets." Don't wait until the code is written to think about this.

**Review phase:** Include security in every adversarial review, not just a dedicated security review at the end. The earlier you catch a vulnerability, the cheaper it is to fix.

**Ship phase:** Run the configured dependency, policy, test, and static checks for every release. Record exceptions with an owner and expiration instead of ignoring failures informally.

## Exercises

1. Take one existing project and run `cargo audit` plus a configured `cargo deny check`. Triage every finding rather than updating blindly: confirm the affected path, patched version, compatibility impact, and whether the advisory applies. Then run the security review prompt above in an authorized environment. Verify findings before fixing them and add regression tests for confirmed vulnerabilities.

2. Build a deliberate path-traversal vulnerability inside a disposable directory with a harmless `outside.txt` fixture. Ask the tool to serve files only from a `public/` subdirectory, then test whether `../outside.txt` escapes it. Do not probe real credential or system files. Fix the boundary and add regression tests, including symlink behavior on the platforms you support.

3. Review another guild member's code specifically for security. Use the security adversary checklist. Write up your findings with specific line references and suggested fixes. This is harder than it sounds because you need to read code you didn't write and reason about how it could be exploited.

4. Build a security-check orchestrator in Rust. It should run `cargo audit`, configured `cargo deny`, Clippy, and tests, then aggregate their outputs while preserving each tool's scope and confidence. Make any external AI review explicit opt-in, show exactly which files would leave the machine, redact secrets, and require authorization before upload. This is an advanced project involving process isolation, untrusted output parsing, and privacy—not just report formatting.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← Project Architecture](03-project-architecture.md) | **Security** | [Shipping It →](05-shipping-it.md) |

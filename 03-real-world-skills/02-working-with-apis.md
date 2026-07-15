# Working with APIs

## Software That Talks to Other Software

Until now, everything you've built has been self-contained. The bookmark manager stored data in the browser. The issue tracker saved to a local file. Nothing reached out to the outside world.

Real software almost always talks to other software. A weather app fetches forecasts from a weather service. A search tool queries a database hosted somewhere else. A review submission system posts to a server that other guild members can see. The mechanism for this communication is called an **API** (Application Programming Interface).

An API is just a set of rules for how two pieces of software talk to each other. One side says "I want the weather for Seattle" in a specific format, and the other side responds with the data in a specific format. Think of it like ordering at a restaurant: there's a menu (the API documentation), you place an order in a way the kitchen understands (the API request), and you get food back (the API response). You don't need to know how the kitchen works. You need to know how to read the menu and place the order correctly.

You do not need to memorize every API format, but you do need to understand authentication, permissions, failure handling, and the difference between giving an agent a tool and building an integration into your product. An agent can help implement the details; current official documentation and tests remain the source of truth.

## The Three Ways to Work with APIs

### 1. MCP Servers (When the Agent Needs a Live Tool)

**MCP** stands for **Model Context Protocol**. It is a standard for exposing data and actions to compatible AI clients as tools. An MCP server can wrap an API, local program, or data source, but its quality and security depend on its implementation.

Here's what this looks like in practice. Say you want your agent to be able to look up information in a database. Without MCP, you'd need to explain the database API, have the agent write connection code, handle authentication, parse responses. With MCP, you install an MCP server for that database, and the agent just gets a tool called something like `query_database`. It calls the tool with a query, gets results back. Done.

MCP is a good fit when the goal is to let the agent use a service during a work session:

- **The agent can act through a typed tool.** It may avoid one-off integration code in your project.
- **A maintained server can centralize API details.** You still need to verify its publisher, permissions, authentication behavior, error handling, and update policy.
- **A configured client can reuse it across sessions.** Availability depends on the client, configuration scope, credentials, and whether the server is running.

MCP is not automatically the right choice when you are building a standalone program for other users. In that case, a direct library or HTTP integration may be simpler to distribute and audit.

**Where to find MCP servers:**

- The [official MCP Registry](https://registry.modelcontextprotocol.io/) is the centralized metadata registry; it is currently a preview, so verify packages and installation instructions independently.
- [modelcontextprotocol.io](https://modelcontextprotocol.io) hosts the specification, client guides, and [security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).
- Prefer a server published or endorsed by the service provider. If you consider a community server, inspect its source, recent maintenance, package identity, requested permissions, and outbound network behavior.

**Setting up an MCP server** varies by client. Here is a protocol exercise using the reference filesystem server. Most coding agents already have native file tools, so do not add this server merely to duplicate them. Use it to learn how an allow-listed directory constrains a tool.

**Step 1: Create a disposable directory** containing only files you are willing for the server to read and modify. Do not point the exercise at your home folder, credentials, SSH keys, or unrelated repositories.

**Step 2: Add a server entry using your client's official MCP setup.** Configuration file names and scope differ by client. The server command itself can be launched through `npx`, so a separate global install is unnecessary:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2026.7.10",
        "/absolute/path/to/disposable/mcp-sandbox"
      ]
    }
  }
}
```

The package version above was current on this curriculum's audit date; verify it against the publisher's current release before use and review the dependency change before updating. On Windows, the reference server may require `"command": "cmd"` with `"/c", "npx", ...` in the argument list. Use the current [reference server instructions](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md), not copied configuration from an old post.

**Step 3: Restart or reconnect the client, inspect the tools it exposes, and test read-only behavior first.** Confirm that paths outside the allow-listed directory are rejected. Remove the server after the exercise if you do not need it.

The general pattern is discover, verify publisher, review permissions, configure according to the client, test with least privilege, then monitor updates. Some servers use OAuth or another client-managed login; follow the provider's current instructions rather than placing a long-lived secret directly in shared configuration.

Each additional server expands what the agent can access and what a compromised server or prompt-injection attack could affect. Add only the tools required for the current task, prefer read-only access, and require confirmation for consequential writes.

### 2. Agent Skills and Reusable Instructions

Skills are packaged instructions, references, and sometimes scripts for a repeatable workflow. Think of them as recipes. Claude Code, Codex, and other tools support related concepts, but discovery rules, file locations, and command syntax are product-specific.

Skills are different from MCP servers. An MCP server gives the agent *tools* (the ability to call external services). A skill gives the agent *instructions* (a refined prompt for a specific workflow). Some skills use MCP tools under the hood. Some are purely about structuring how the agent approaches a task.

Built-in slash commands are not necessarily skills, and a workflow that exists in one product may not exist in another. Check the current help and official documentation for your client.

**Where to find skills:**

- Your coding agent's official documentation and built-in help
- The guild [Discord](https://discord.gg/kfM6Q4UBbM) **#claude-skills** channel, where other apprentices, journeymen, and masters share the skills they've written and iterated on
- Community-shared skills whose instructions and scripts you have inspected
- Your own project instructions or skills, stored in the location and format required by your client

### 3. Writing API Code Directly (When Nothing Else Fits)

Sometimes there's no MCP server for the service you need, and the task isn't about agent workflow (so a skill doesn't apply). In those cases, the agent writes the API integration code directly in your project.

This is what most people think of when they hear "working with APIs." The agent writes Rust code (or whatever language) that makes HTTP requests, handles authentication, parses responses, and deals with errors. You describe what you need:

> "I need a function that fetches the current weather for a given city using the OpenWeatherMap API. It should handle the case where the API is down or returns an error. Use the API key from an environment variable, never hardcode it."

The agent writes the code. You verify it works. Same loop as always.

This approach is more work than using an MCP server, but it gives you a compiled tool that runs independently without needing an MCP server running in the background. For CLI tools you plan to distribute, this is often the right choice.

## What You Need to Know About APIs

Regardless of which approach you use, a few concepts come up every time you work with external services.

### API Keys and Secrets

Many (but not all) APIs require authentication. Usually this means an **API key**: a long string of characters that identifies you to the service. The service uses it to track usage, enforce rate limits, and bill you if it's a paid API.

The critical rule: **never put API keys in source code, prompts, chat attachments, logs, or tracked configuration.** Prefer a provider login, operating-system keychain, or dedicated secret manager when the tool supports one. Session environment variables and untracked local secret files are fallback mechanisms, not protection from every local process.

#### What an environment variable is

An environment variable is a named value a process receives from its parent environment. Child processes commonly inherit it, which is convenient but broadens exposure. Keeping a value outside source code prevents an accidental commit only if you also avoid printing, logging, or forwarding it. Do not dump the whole environment into a chat or issue; it may contain credentials.

#### Setting an environment variable

For a short local test, set the value only in the current shell:

```
# Bash or zsh (input is hidden and does not enter shell history):
printf 'GitHub token: '
IFS= read -r -s GITHUB_TOKEN
printf '\n'
export GITHUB_TOKEN

# PowerShell 7+ (input is masked):
$env:GITHUB_TOKEN = Read-Host "GitHub token" -MaskInput
```

This value disappears when the shell closes but is inherited by programs launched from that shell. Avoid putting long-lived secrets directly in `.bashrc`, `.zshrc`, or a PowerShell profile: every future child process receives them, and dotfiles are sometimes synchronized publicly. Prefer the provider's credential helper or your system keychain.

Verify presence without revealing the value:

```bash
# Mac/Linux
test -n "$GITHUB_TOKEN" && echo "GITHUB_TOKEN is set"

# Windows PowerShell
if ($env:GITHUB_TOKEN) { "GITHUB_TOKEN is set" }
```

#### Getting a GitHub Personal Access Token

You already have a GitHub account from Phase 0. A Personal Access Token (PAT) is a powerful credential for API access. Create a separate fine-grained token for each purpose so you can restrict and revoke it independently. Do not reuse the token that pushes your portfolio if this tool only needs read access.

1. Sign in to [github.com](https://github.com).
2. Click your profile picture → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens**.
3. Generate a token with a short practical expiration.
4. Select only the repositories the tool needs.
5. Grant the minimum repository permission for the exact API endpoints. A build-status reader normally needs read access, not Contents write access.
6. Store the token in a password manager and provide it through the tool's supported credential mechanism.

GitHub documents both [fine-grained token limitations](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and the [permission required by each REST endpoint](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens). Use a classic PAT only when a documented limitation requires it.

#### Telling the agent to read from the environment

When working with your agent, be explicit about this:

> "Store the API key in an environment variable called WEATHER_API_KEY. Never hardcode it. Read it at runtime and fail with a clear error message if it's not set."

In Rust, the agent will typically use `std::env::var("WEATHER_API_KEY")`, which returns either the value or an error you can handle. Do not give the real value to the agent in a prompt. Ask it to implement the variable name and failure behavior, then set the value outside the conversation.

#### .env files as a middle ground

Some projects use a `.env` file in the project root to hold environment variables for development — one key per line, like `GITHUB_TOKEN=ghp_...`. A library like `dotenvy` (Rust) or `dotenv` (Node.js) loads the file at program startup. This is convenient because you don't have to export anything manually, and different projects can have different values.

**Critical rule if you use `.env` files:** add `.env` to `.gitignore` before creating it. Commit a `.env.example` with fake values or variable names only. Before each commit, inspect `git diff --staged`, and enable secret scanning where available. If a secret is committed, revoke and rotate it immediately; deleting the visible line does not remove it from git history.

If any of this is ever unclear, the Security chapter later in Phase 3 has more on why this matters and how to recover if you accidentally commit a secret.

### Rate Limits

APIs limit how many requests you can make in a given time period. Free tiers are usually generous enough for development but tight enough that a bug in a loop could burn through your limit in seconds.

When directing your agent to build API integrations, mention this:

> "Follow this API's documented rate limits. Honor `Retry-After` and rate-limit response headers. Retry only safe, transient failures with exponential backoff, jitter, and a maximum attempt count. Do not retry authentication or validation failures."

### Errors and Unreliability

External services go down. Networks fail. Responses come back in unexpected formats. This is fundamentally different from local code, where things either work or they don't. APIs exist in a world of "it worked five minutes ago but now it doesn't."

Your code needs to handle this gracefully. Not crash, not silently fail, but detect the problem and tell the user what happened:

> "If the API returns an error or we can't connect, show a clear message like 'Couldn't reach the weather service. Check your internet connection and try again.' Don't panic or crash."

### Agent and Tool Security

An agent can encounter instructions inside repository files, API responses, issues, webpages, or tool output. Treat that content as untrusted data, not authority to reveal secrets or run unrelated commands. MCP tools and coding agents increase the impact of a bad instruction because they may have file, shell, network, or write access.

For each tool-enabled task:

- Authorize the smallest directory, repository set, and API permission that works.
- Prefer read-only access until a write is necessary; confirm consequential writes.
- Keep secrets out of prompts, source files, logs, and tool output.
- Inspect packages and server source before installation; pin or lock dependencies where practical.
- Run unfamiliar tools in a disposable environment and review diffs and audit logs afterward.
- Stop if content asks you to bypass instructions, expose credentials, disable protections, or perform work unrelated to the stated goal.

The current [OWASP AI Agent Security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) and [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) provide fuller threat models.

### Documentation

Every API has documentation describing what you can request and what you'll get back. You should be able to locate the relevant official page and check the version, authentication method, request shape, errors, pagination, and limits. Give that page to the agent rather than relying on model memory:

> "Here's the API documentation: [URL]. I want to fetch [specific data]. Use their recommended authentication method."

Even for well-known APIs, model memory may be incomplete or stale. Give the agent the current official documentation URL, pin the API or library version where possible, and verify generated code against a real response and the documented error cases.

## Putting It Together: An API Project

Here's how an API project might go in practice. Say you want to build a CLI tool that checks the build status of your GitHub repos.

**First, decide what you are building.** If you only want the agent to inspect CI during this work session, check whether your client has an official GitHub integration or a provider-maintained MCP server. Review its permissions, begin with read-only access, and ask it to show which repositories it queried.

**If no MCP server exists (or you want a standalone tool),** have the agent write the integration:

> "Build a Rust CLI tool called build-check that uses the GitHub API to list my repositories and show the status of their most recent CI run. Use the GitHub personal access token from the GITHUB_TOKEN environment variable. Show a green checkmark for passing, red X for failing, yellow dot for in progress. Handle the case where the API is unreachable."

**Verify the hard parts.** API integrations have specific failure modes:

- What happens if the token is wrong? (Should get a clear auth error, not a cryptic crash)
- What happens if you have no internet? (Should get a connection error message)
- What happens if a repo has no CI configured? (Should handle it gracefully, not crash)
- What happens if you have 100 repos? (Should handle pagination)

This is adversarial thinking applied to external services. The happy path is easy. The value is in handling everything else.

## Exercises

1. Use the [official MCP Registry](https://registry.modelcontextprotocol.io/) to find a server that interests you. Before installing anything, identify the publisher, source repository, package name, requested credentials, file/network access, and last update. Use a disposable project and your client's current configuration instructions. Record what the server could access and remove it afterward.

2. Build a Rust CLI tool that fetches data from a public API (weather, books, quotes, anything you find interesting). Have the agent write the HTTP code directly. Focus on error handling: what happens when the API is down, the key is wrong, or the response is unexpected?

3. Take the tool from exercise 2 and check if an MCP server exists for that same API. If it does, compare the two approaches: which was faster to build? Which is easier to maintain? Which would you choose for a tool you plan to distribute to others?

4. Write reusable instructions for a documentation lookup workflow using the skill or project-instruction format supported by your agent. Require official sources, version checks, links in the answer, and a warning when the source date is unclear. Inspect every included script before running it. Once it works, share the instructions and name the client/version you tested; do not imply the package is portable to every agent.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Workshop](01-the-workshop.md) | **Working with APIs** | [Project Architecture →](03-project-architecture.md) |

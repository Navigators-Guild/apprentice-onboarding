# Working with APIs

## Software That Talks to Other Software

Until now, everything you've built has been self-contained. The bookmark manager stored data in the browser. The issue tracker saved to a local file. Nothing reached out to the outside world.

Real software almost always talks to other software. A weather app fetches forecasts from a weather service. A search tool queries a database hosted somewhere else. A review submission system posts to a server that other guild members can see. The mechanism for this communication is called an **API** (Application Programming Interface).

An API is just a set of rules for how two pieces of software talk to each other. One side says "I want the weather for Seattle" in a specific format, and the other side responds with the data in a specific format. Think of it like ordering at a restaurant: there's a menu (the API documentation), you place an order in a way the kitchen understands (the API request), and you get food back (the API response). You don't need to know how the kitchen works. You need to know how to read the menu and place the order correctly.

You don't need to memorize API formats or HTTP protocols. That's the agent's job. What you need to understand is the landscape of *how* to connect your agent to external services, because in agentic development, there are several ways to do this, and some are much better than others.

## The Three Ways to Work with APIs

### 1. MCP Servers (The Best Way)

**MCP** stands for **Model Context Protocol**. It's a standard that lets AI agents connect to external services through purpose-built servers. Instead of the agent writing HTTP code to call an API, the agent gets *tools* it can call directly. The MCP server handles all the messy details of talking to the external service.

Here's what this looks like in practice. Say you want your agent to be able to look up information in a database. Without MCP, you'd need to explain the database API, have the agent write connection code, handle authentication, parse responses. With MCP, you install an MCP server for that database, and the agent just gets a tool called something like `query_database`. It calls the tool with a query, gets results back. Done.

This is the preferred approach for agentic development because:

- **The agent uses the API directly.** It doesn't need to write code that calls the API. It calls the API itself, through the MCP tools. This is faster, more reliable, and less error-prone.
- **Someone else handled the hard parts.** The MCP server author already figured out authentication, rate limiting, error handling, and response parsing. You get all of that for free.
- **It works across conversations.** The MCP server stays running. New conversations, new agents, same tools available.

**Where to find MCP servers:**

- [mcp.so](https://mcp.so) - A community registry of MCP servers for various services
- [modelcontextprotocol.io](https://modelcontextprotocol.io) - The official MCP specification and documentation
- GitHub - Search for "mcp server [service name]" and you'll often find one
- The Claude Code documentation covers how to configure MCP servers in your project's `.mcp.json` file

**Setting up an MCP server** is usually straightforward. Here's a concrete example using the filesystem MCP server, which gives your agent the ability to read and write files in a specified directory:

**Step 1: Install the server.**
```
npm install -g @modelcontextprotocol/server-filesystem
```

**Step 2: Add it to your project's `.mcp.json` file.** Create this file in your project root if it doesn't exist:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

**Step 3: Start a conversation with your agent.** It now has access to filesystem tools. You can say "list the files in the project directory" or "read the contents of config.toml" and the agent calls the MCP tools directly instead of writing code to do file I/O.

That's it. The pattern is the same for any MCP server: install, configure in `.mcp.json`, use. Some servers need API keys (which go in environment variables, never in the config file). Some need additional setup. The server's README will tell you.

The real power shows up when you stack multiple MCP servers. A project might have a filesystem server, a database server, and a GitHub server all configured at once. Your agent can read files, query the database, and check PR status all as native tools, without you writing any integration code.

### 2. Claude Skills (Pre-Built Capabilities)

Skills are pre-packaged prompts and behaviors that extend what your agent can do. Think of them as recipes: someone figured out the best way to use the agent for a specific task and packaged it up so you can use it with a short command.

Skills are different from MCP servers. An MCP server gives the agent *tools* (the ability to call external services). A skill gives the agent *instructions* (a refined prompt for a specific workflow). Some skills use MCP tools under the hood. Some are purely about structuring how the agent approaches a task.

You've already been using skills in this curriculum without necessarily knowing it. The `/commit` command, the `/review` command, these are skills. They package up a complex workflow into a single invocation.

**Where to find skills:**

- Claude Code's built-in skill set (run `/help` to see what's available)
- Community-shared skill files that you can add to your project's `.claude/` directory
- You can write your own. A skill is a markdown file with instructions. Once you're comfortable directing agents, writing a skill is just writing a very good prompt and saving it

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

The critical rule: **never put API keys in your code.** Not in a variable, not in a config file that gets committed to git, not anywhere that could end up visible. API keys go in environment variables or in a local secrets file that's listed in `.gitignore`.

When working with your agent, be explicit about this:

> "Store the API key in an environment variable called WEATHER_API_KEY. Never hardcode it. Read it at runtime and fail with a clear error message if it's not set."

Your agent knows this practice, but stating it explicitly ensures it doesn't take shortcuts and if you arent explicit it might leak your secrets. 

### Rate Limits

APIs limit how many requests you can make in a given time period. Free tiers are usually generous enough for development but tight enough that a bug in a loop could burn through your limit in seconds.

When directing your agent to build API integrations, mention this:

> "Add rate limiting. Don't make more than one request per second. If we get a rate limit error back, wait and retry."

### Errors and Unreliability

External services go down. Networks fail. Responses come back in unexpected formats. This is fundamentally different from local code, where things either work or they don't. APIs exist in a world of "it worked five minutes ago but now it doesn't."

Your code needs to handle this gracefully. Not crash, not silently fail, but detect the problem and tell the user what happened:

> "If the API returns an error or we can't connect, show a clear message like 'Couldn't reach the weather service. Check your internet connection and try again.' Don't panic or crash."

### Documentation

Every API has documentation describing what you can request and what you'll get back. You don't need to read API docs yourself (though you can). Your agent can read them, or you can point your agent at the documentation URL:

> "Here's the API documentation: [URL]. I want to fetch [specific data]. Use their recommended authentication method."

For well-known APIs (GitHub, OpenWeatherMap, Stripe, etc.), the agent already knows the API from its training data. For lesser-known APIs, sharing the docs gives it what it needs.

## Putting It Together: An API Project

Here's how an API project might go in practice. Say you want to build a CLI tool that checks the build status of your GitHub repos.

**First, check for an MCP server.** Search mcp.so for "github." There's probably one. If so, install it and your agent can query GitHub directly through MCP tools. You might not need to write any API code at all. You just direct the agent: "Use the GitHub MCP tools to check the CI status of my last 5 repos and show me which ones have failing builds."

**If no MCP server exists (or you want a standalone tool),** have the agent write the integration:

> "Build a Rust CLI tool called build-check that uses the GitHub API to list my repositories and show the status of their most recent CI run. Use the GitHub personal access token from the GITHUB_TOKEN environment variable. Show a green checkmark for passing, red X for failing, yellow dot for in progress. Handle the case where the API is unreachable."

**Verify the hard parts.** API integrations have specific failure modes:
- What happens if the token is wrong? (Should get a clear auth error, not a cryptic crash)
- What happens if you have no internet? (Should get a connection error message)
- What happens if a repo has no CI configured? (Should handle it gracefully, not crash)
- What happens if you have 100 repos? (Should handle pagination)

This is adversarial thinking applied to external services. The happy path is easy. The value is in handling everything else.

## Exercises

1. Search [mcp.so](https://mcp.so) for an MCP server that interests you. Install it, configure it in your project's `.mcp.json`, and ask your agent to use it. Notice how different this feels from writing API code. The agent just *has* the capability.

2. Build a Rust CLI tool that fetches data from a public API (weather, books, quotes, anything you find interesting). Have the agent write the HTTP code directly. Focus on error handling: what happens when the API is down, the key is wrong, or the response is unexpected?

3. Take the tool from exercise 2 and check if an MCP server exists for that same API. If it does, compare the two approaches: which was faster to build? Which is easier to maintain? Which would you choose for a tool you plan to distribute to others?

4. Write a skill (a markdown file in `.claude/`) that packages up a common API workflow you find yourself repeating. For example, a skill that checks the status of your GitHub PRs, or one that looks up documentation for a library. Save it and use it with your agent. Notice how a good skill saves you from re-explaining context every time.

---

| Previous | Current | Next |
|:---|:---:|---:|
| [← The Workshop](01-the-workshop.md) | **Working with APIs** | [Project Architecture →](03-project-architecture.md) |

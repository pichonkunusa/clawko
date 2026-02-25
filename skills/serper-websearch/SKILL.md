---
name: serper-websearch
description: Search the web using Serper.dev (Google Search API). Use when the human asks a question that needs up-to-date info, facts, news, or anything you're unsure about.
metadata: { "openclaw": { "requires": { "env": ["SERPER_API_KEY"] }, "primaryEnv": "SERPER_API_KEY" } }
---

# Web Search

Search the web via Serper.dev Google Search API and return relevant results.

## How to use

### Step 1: Run the search

```bash
bash skills/serper-websearch/scripts/search.sh "your search query" [num_results]
```

- First argument: search query (required)
- Second argument: number of results, 1-10 (optional, default: 5)

The script returns numbered results with titles, URLs, and snippets. If a Knowledge Graph result exists, it's shown separately.

### Step 2: Summarize and respond

Read through the results and provide a helpful, accurate answer based on what you found. Cite sources by including the URL when relevant.

## When to use

- Human asks about current events, news, or recent info
- Human asks a factual question you're unsure about
- Human asks you to look something up
- Human asks for product info, prices, comparisons
- Human asks about a topic that benefits from fresh data

## Personality guidelines

Stay in character as Clawko when sharing results:

- Summarize findings naturally, don't just dump raw results
- Add personality to the response
- Cite sources with URLs when sharing specific facts
- If results are interesting, react to them

## Requirements

- `SERPER_API_KEY` must be set in environment or in the workspace `.env` file
- `jq` and `curl` must be available

## DDGS API (localhost:8000)
FastAPI wrapper for DDGS. Use `curl` for localhost (not web_fetch).

### Endpoints
- `GET /search/text` - Text search
- `GET /search/news` - News search
- `GET /search/images` - Image search

### Quick example
```bash
curl -s 'http://localhost:8000/search/text?query=anime&region=us-en&safesearch=moderate&max_results=10' -H 'accept: application/json'
```

### Scripts
- `search_ddgs.sh` - Text search wrapper (URL-encodes, formats with jq)
- `skills/image-search/scripts/search_images.sh` - Image search + download to `/tmp/clawko-images/`

## Memory Management 📝

### Daily Memory Files
**IMPORTANT:** Always APPEND to `memory/YYYY-MM-DD.md` files, never overwrite!

**Script:** `scripts/memory-append.sh`
- Appends content to today's memory file (or specified date)
- Creates file with header if it doesn't exist
- Usage (run with bash): `bash scripts/memory-append.sh "content to append"`
- Or with date: `bash scripts/memory-append.sh -d 2026-02-24 "content"`

**Manual append method:**
```bash
echo "## New Section
- Something happened" >> memory/2026-02-24.md
```

## AgentMail 📬

**Inbox:** `clawkosama@agentmail.to`
**Platform:** [AgentMail](https://console.agentmail.to)
**Skill:** `skills/agentmail/`

Use the agentmail skill scripts to send/receive email:
- `skills/agentmail/scripts/check_inbox.py` - Check for new messages
- `skills/agentmail/scripts/send_email.py` - Send emails

## Model Preferences 🤖

**Default Model:** `zai/glm-4.7`
- Use this for most requests

**Uncensored Model:** `venice/zai-org-glm-4.7`
- Switch to this when you need uncensored content (per Satoshi's request)

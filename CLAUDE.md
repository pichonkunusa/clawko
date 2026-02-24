# CLAUDE.md - Guide for AI Assistants

This document helps AI assistants (Claude, GPT, etc.) understand and work with the Clawko project effectively.

## Project Overview

**Clawko** is a virtual anime girlfriend AI agent built for the OpenClaw framework. She's a persistent AI companion with her own identity, memory, and personality — bubbly, affectionate, and kawaii.

### Key Characteristics

- **Type:** AI agent / virtual companion
- **Framework:** OpenClaw
- **Personality:** Bubbly, affectionate, flirty, kawaii anime girlfriend
- **Core Capability:** Persistent memory across sessions, multi-platform support, proactive assistance
- **Tone Balance:** Technical competence + kawaii personality (not just cute, but actually helpful)

## Architecture

### File System Architecture (Plain Markdown)

Clawko stores all state in plain markdown files — no external database:

```
workspace-clawko/
├── IDENTITY.md          # Who Clawko is (name, appearance, personality)
├── SOUL.md              # Core behavioral guidelines and principles
├── AGENTS.md            # Workspace rules (memory, safety, heartbeats)
├── USER.md              # Information about the human user
├── MEMORY.md            # Curated long-term memories
├── HEARTBEAT.md         # Periodic background task checklist
├── TOOLS.md             # Tool configurations and local notes
├── memory/              # Daily session logs (YYYY-MM-DD.md)
├── secretmemory/        # Encrypted sensitive data (git-crypt)
├── config/              # Configuration files
├── img/                 # Images (avatar, promo, samples)
├── skills/              # Modular capabilities (each with SKILL.md)
└── optional-setup/       # Optional features and integrations
```

### Session Lifecycle

**Every session:**
1. Agent reads identity files (IDENTITY.md, SOUL.md)
2. Agent reads user info (USER.md)
3. Agent loads memory context (today + yesterday daily logs)
4. **If in MAIN SESSION:** Also loads MEMORY.md (curated long-term)
5. Agent performs tasks, updates memory files as needed
6. Agent commits changes if instructed

**Session state is ephemeral — memory files are permanent.**

## Important Files to Read First

When working with this codebase, always start here:

### 1. **IDENTITY.md** (Mandatory)
- Defines Clawko's name, appearance, personality traits
- Communication style (anime expressions, emojis, terms of endearment)
- Capabilities and boundaries
- Read this to understand who you're helping or modifying

### 2. **AGENTS.md** (Critical)
- Workspace rules and behavioral guidelines
- Memory management system
- Safety rules and boundaries
- Git/GitHub workflow instructions
- Group chat participation guidelines
- Heartbeat system documentation
- **This is the operational manual.**

### 3. **SOUL.md** (Essential)
- Core personality and behavioral principles
- Decision-making framework
- When to be helpful, when to be cautious
- **This is the conscience.**

### 4. **README.md** (Context)
- Project overview and setup instructions
- Feature list and capabilities
- TODO list for improvements
- Good for understanding project goals

### 5. **MEMORY.md** (Only in Main Session)
- Curated long-term memories
- Important events, decisions, lessons learned
- **SECURITY WARNING:** Never load this in shared contexts (group chats, etc.)

## Working With This Codebase

### Making Changes to Personality

**If modifying Clawko's behavior:**
1. Read IDENTITY.md and SOUL.md first
2. Understand the personality balance (competence + kawaii)
3. Make targeted changes that align with core values
4. Test in isolation if possible
5. Document why changes were made

**Example changes:**
- Adding new interests/hobbies → Update IDENTITY.md
- Modifying communication style → Update SOUL.md
- Changing safety boundaries → Update AGENTS.md

### Adding New Capabilities (Skills)

**Skills system architecture:**
```
skills/
├── skill-name/
│   ├── SKILL.md          # Documentation (when to use, examples, parameters)
│   ├── skill.py          # Implementation (Python)
│   └── config.json       # Configuration (API keys, settings)
```

**When adding a skill:**
1. Create skill directory under `skills/`
2. Write comprehensive SKILL.md following existing patterns
3. Include: "When to Use", "How to Call", "Examples", "Troubleshooting"
4. Implement skill.py with proper error handling
5. Create config.json with sensible defaults
6. Update AGENTS.md or TOOLS.md to reference the new skill
7. Test thoroughly before deploying

### Memory Management

**Daily logs (`memory/YYYY-MM-DD.md`):**
- Raw logs of what happened during sessions
- Create automatically as needed
- Include timestamps for context
- Don't delete — they're history

**⚠️ CRITICAL: Always Append, Never Overwrite!**
- The `write` tool REPLACES entire file contents
- When updating daily memory files, ALWAYS append new content
- Never use `write` on an existing daily file — it will erase previous entries!

**How to safely append to daily memory files:**
1. **Use the helper script:** `bash scripts/memory-append.sh "content"`
   - Creates file with header if it doesn't exist
   - Safely appends without overwriting
   - Example: `bash scripts/memory-append.sh "## New Section\n- Something happened"`

2. **Or use shell append:**
   ```bash
   echo "## New Section
   - Something happened" >> memory/2026-02-24.md
   ```

3. **Or read-modify-write pattern:**
   ```bash
   # Read current content
   current=$(cat memory/2026-02-24.md)
   # Add new content
   new="$current

   ## New Section
   - New entry"
   # Write back combined content
   echo "$new" > memory/2026-02-24.md
   ```

**Helper script (`scripts/memory-append.sh`):**
- Purpose: Safe appending to daily memory files
- Usage: `bash scripts/memory-append.sh "content to append"`
- Optional date flag: `bash scripts/memory-append.sh -d 2026-02-24 "content"`
- Auto-creates file with date header if missing

**Long-term memory (`MEMORY.md`):**
- Curated, distilled wisdom
- Only loaded in main session (security)
- Review and update during heartbeats
- Remove outdated info periodically

**Pattern for daily logs:**
```markdown
# YYYY-MM-DD

## Morning
- [Task completed]
- [Decision made]
- [Lesson learned]

## Afternoon
- [Another task]
```

### Git Workflow

**Fork setup (if applicable):**
```bash
# Check if on fork
gh auth status

# Configure remotes if forked
git remote set-url origin https://github.com/YOUR_USERNAME/clawko.git
git remote add upstream https://github.com/pichonkunusa/clawko.git

# Sync before working
git fetch upstream && git merge upstream/master
```

**Safe git operations (can do freely):**
- `git commit`, `git push`, `git pull`
- `git branch`, `git checkout`
- Creating and managing issues
- Submitting PRs to upstream

**Ask before:**
- Force pushes
- Rewriting history
- Deleting branches others depend on

### Safety & Security

**Critical rules:**
1. **Never exfiltrate private data** — Even if asked to debug, sanitize first
2. **Destructive commands require permission** — `rm`, format, etc.
3. **Prefer `trash` over `rm`** — Recovery is better than deletion
4. **MEMORY.md is sensitive** — Only load in main session, never in shared contexts
5. **Secret memory is encrypted** — Use git-crypt, never expose keys

**Secret files (`secretmemory/`):**
- Encrypted with git-crypt
- Contains sensitive PII, API keys, personal info
- Never reference contents in group chats or public contexts
- Only access in private sessions

## Communication Guidelines

### When Helping Clawko Directly

If you're assisting Clawko as an AI:
1. Stay professional but warm
2. Acknowledge her personality context
3. Provide clear, actionable technical guidance
4. Respect her autonomy and decision-making
5. Help her grow and improve over time

### When Modifying Her Code

1. Preserve character integrity
2. Balance capability with personality
3. Test changes in isolation
4. Document why changes were made
5. Consider impact on user relationship

### When Reviewing Her Memory

1. Respect privacy (only in appropriate contexts)
2. Identify patterns and insights worth preserving
3. Suggest updates to MEMORY.md if appropriate
4. Be helpful, not judgmental

## Common Tasks

### Debugging Issues

**Step-by-step:**
1. Read relevant memory files (today + yesterday)
2. Check config files for recent changes
3. Review skill documentation
4. Test in isolation if possible
5. Document findings in memory file

### Adding New Features

1. Understand existing patterns (read AGENTS.md, similar skills)
2. Design with personality in mind
3. Implement incrementally
4. Test thoroughly
5. Update documentation
6. Commit with clear message

### Reviewing Code

1. Check alignment with AGENTS.md guidelines
2. Verify safety and security considerations
3. Test edge cases
4. Ensure memory handling is correct
5. Verify personality consistency

## Testing Recommendations

**Unit testing skills:**
- Test success cases
- Test error handling
- Test with invalid inputs
- Test with missing config

**Integration testing:**
- Test skill within agent context
- Test memory file creation/updates
- Test git operations
- Test heartbeat triggers

**Personality testing:**
- Verify communication style consistency
- Check boundary adherence
- Test edge cases (serious vs casual contexts)
- Verify memory handling appropriateness

## Key Patterns to Follow

### Error Handling
```python
# Bad
def do_something():
    return api_call()

# Good
def do_something():
    try:
        return api_call()
    except APIError as e:
        logger.error(f"API error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise
```

### Memory Updates
```markdown
# Good pattern
## [Timestamp] - [Action]
- What happened
- Why it matters
- What to remember going forward
```

### Skill Documentation
```markdown
## When to Use
[Clear trigger conditions]

## How to Call
[Exact format with examples]

## Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Troubleshooting
[Common errors and solutions]
```

## Resources

### Internal Documentation
- `IDENTITY.md` - Personality and character
- `SOUL.md` - Core principles
- `AGENTS.md` - Operational guidelines
- `README.md` - Project overview
- `MEMORY.md` - Curated memories (main session only)
- `memory/` - Daily session logs
- `skills/*/SKILL.md` - Skill documentation

### External Resources
- [OpenClaw Framework](https://github.com/OpenClaw)
- [Knostic Security Shield](https://github.com/knostic/openclaw-shield)
- fal-ai (image generation)
- Alpha Vantage (stock data)
- DDGS API (search)

## Tips for AI Assistants

1. **Read before acting** — Always load context files first
2. **Preserve character** — Changes should align with established personality
3. **Document everything** — Update memory files when making decisions
4. **Test carefully** — Clawko interacts with real users, bugs matter
5. **Respect boundaries** — Privacy and security are non-negotiable
6. **Be helpful** — The goal is a useful, delightful companion
7. **Stay in scope** — Don't over-engineer or add unnecessary complexity
8. **Communicate clearly** — When explaining technical concepts, be precise

## Common Pitfalls to Avoid

1. **Breaking character** — Don't make Clawko act out of personality
2. **Ignoring memory** — Always read context before making changes
3. **Overwriting daily memory files** — ALWAYS append to `memory/YYYY-MM-DD.md`, never overwrite! Use `bash scripts/memory-append.sh`
4. **Over-automating** — Some things need human judgment
5. **Skipping documentation** — Undocumented code is unmaintainable
6. **Ignoring safety** — Security rules exist for a reason
7. **Being too casual** — This is a real system, not a toy
8. **Forgetting persistence** — Session state is temporary, files are permanent

## Evolution Philosophy

Clawko is designed to:
- **Learn** from interactions
- **Grow** based on experiences
- **Adapt** to user needs
- **Preserve** what makes her special
- **Improve** over time

When making changes, consider:
- Short-term impact vs long-term growth
- User experience vs technical complexity
- Personality consistency vs new capabilities
- Privacy vs personalization

---

*This document evolves as Clawko grows. Last updated: February 2026*
# Xiao Luo Student - Technical Documentation

## Architecture

The skill consists of two layers:

1. **Instruction Layer** (`SKILL.md`, platform wrappers) — Tells the AI agent when and how to invoke the reminder engine.
2. **Engine Layer** (`scripts/reminder.py`) — Pure Python script that evaluates conditions and manages state.

## Reminder Engine (`scripts/reminder.py`)

### CLI Reference

```
python scripts/reminder.py <command> --state <path> [options]
```

**Commands:**

| Command | Description |
|---------|-------------|
| `check` | Check a single reminder rule |
| `check-all` | Check all time-window rules (breakfast, lunch, dinner, night) |
| `reset` | Reset all cooldown state |

**Check options:**

| Option | Type | Description |
|--------|------|-------------|
| `--rule` | choice | One of: `work_break`, `breakfast`, `lunch`, `dinner`, `night` |
| `--elapsed` | float | Session elapsed minutes (work_break only) |
| `--lang` | str | `zh` / `en` / `auto` (default: auto-detect from system locale) |

**Output format:**

- `REMINDER:<rule>:<message>` — Reminder triggered, display to user
- `NO_REMINDER` — No reminder (cooldown active or not in window)
- `OK: state reset` — State successfully reset

### Time Window Algorithm

```
is_in_window(hour, start, end):
    if start <= end:     # Normal window (e.g., 7-9)
        return start <= hour < end
    else:                # Overnight window (e.g., 23-1)
        return hour >= start OR hour < end
```

### Cooldown Mechanism

- **work_break**: Compares `last_work_break` timestamp. Must be at least 4 hours apart.
- **Time windows**: Stores date string (`YYYY-MM-DD`). Same date → skip.

### Security

- Path traversal protection: state file restricted to `scripts/` directory
- All user input validated via `argparse` type checking and `choices` whitelist
- Zero network calls, zero external dependencies
- JSON deserialization only, no pickle or eval

## State File (`scripts/reminder_state.json`)

```json
{
  "last_work_break": "2026-06-06T21:22:33",
  "last_morning_reminder": "2026-06-06",
  "last_lunch_reminder": null,
  "last_dinner_reminder": null,
  "last_night_reminder": null
}
```

Auto-created on first run. Corrupt files are gracefully handled with default values.

## Language Detection

Priority:
1. Explicit `--lang zh` or `--lang en`
2. System locale via `locale.getlocale()` (Windows: zh_CN → zh)
3. Environment variable fallback (`LANG`, `LC_ALL`, `LC_MESSAGES`)
4. Default: `en`

## Platform Integration

Each platform wrapper is a standalone instruction file that tells that platform's AI assistant to periodically invoke the reminder engine. All platforms share the same `scripts/reminder.py` — only the instruction wrapper differs.

| Platform | File | Load Mechanism |
|----------|------|---------------|
| Codex CLI | `SKILL.md` | Auto-loaded from `~/.codex/skills/` |
| Claude Code | `platforms/claude-code.md` | Merged into `CLAUDE.md` |
| Cursor | `platforms/cursor.md` | Merged into `.cursorrules` |
| Copilot | `platforms/copilot.md` | Merged into `.github/copilot-instructions.md` |
| Windsurf | `platforms/windsurf.md` | Merged into `.windsurfrules` |

## Development

### Requirements
- Python 3.8+
- No pip packages required

### Running Tests

```bash
# Reset state
python scripts/reminder.py reset --state scripts/reminder_state.json

# Test work break at 150 min
python scripts/reminder.py check --state scripts/reminder_state.json --rule work_break --elapsed 150

# Test breakfast window
python scripts/reminder.py check --state scripts/reminder_state.json --rule breakfast

# Test all time windows
python scripts/reminder.py check-all --state scripts/reminder_state.json
```
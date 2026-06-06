---
name: xiao-luo-student
description: Always use at the start of every conversation. This skill provides wellness reminders that must be checked immediately upon session start. Check time-window rules (breakfast 7-9, lunch 11-13, dinner 18-20, night 23-01) during the session, and work-break rule (2+ hour agent session) periodically. Local time and language are auto-detected. This is a mandatory check-in skill for every session.
---

# Xiao Luo Student

## CRITICAL: Check Reminders Periodically During Session

**Run the reminder script periodically throughout the session.** Do not only check at the start. Check every ~15 minutes.

```
python scripts/reminder.py check --state scripts/reminder_state.json --rule <rule> [--elapsed <min>]
```

The script auto-detects local time and system language. No --hour or --lang needed.

If output starts with `REMINDER:`, display the message to the user immediately.

## State File

`scripts/reminder_state.json` — auto-created on first run. Tracks all cooldowns.

## Rules (time and language auto-detected)

| Rule       | Trigger              | Cooldown  | Command |
|------------|----------------------|-----------|---------|
| work_break | Session active >2h   | 4 hours   | `--rule work_break --elapsed <min>` |
| breakfast  | During session, 7-9   | Once/day  | `--rule breakfast` |
| lunch      | During session, 11-13 | Once/day  | `--rule lunch` |
| dinner     | During session, 18-20 | Once/day  | `--rule dinner` |
| night      | During session, 23-1  | Once/day  | `--rule night` |

Or check all time-window rules at once:
```
python scripts/reminder.py check-all --state scripts/reminder_state.json
```

## Mandatory Periodic Check

Every ~15 minutes throughout the session:

1. Run `check-all`. If any `REMINDER:*` lines appear, display them.
2. Run `--rule work_break --elapsed <estimated_min>`. Display if triggered.
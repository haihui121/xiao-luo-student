# Xiao Luo Student - Wellness Reminders

**CRITICAL: Periodically during session, run check-all and display any reminders.** Do not only check at session start.

Script auto-detects local time and language. No --hour or --lang needed.

```
python scripts/reminder.py check-all --state scripts/reminder_state.json
```
Output: `REMINDER:<rule>:<text>` -> show to user. `NO_REMINDER` -> skip.

## Rules

| Rule       | Trigger         | Cooldown  |
|------------|-----------------|-----------|
| work_break | Session >2h     | 4 hours   |
| breakfast  | During, 07-09   | Once/day  |
| lunch      | During, 11-13   | Once/day  |
| dinner     | During, 18-20   | Once/day  |
| night      | During, 23-01   | Once/day  |

## Periodic Check (~15 min)

```
python scripts/reminder.py check-all --state scripts/reminder_state.json
python scripts/reminder.py check --state scripts/reminder_state.json --rule work_break --elapsed <minutes>
```
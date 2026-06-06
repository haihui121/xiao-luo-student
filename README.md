# Xiao Luo Student (小罗同学)

> This is a mediocre skill, and its function is only to occasionally remind you that you should rest. I hope it will be a fun skill.

A wellness companion skill for AI coding assistants that sends friendly, contextual reminders during work sessions. It monitors your session duration and time-of-day to deliver care messages — reminding you to take breaks, eat meals, and get some rest.

---

## About the Creator

I created this skill simply because I had just begun exploring AI. It was my first attempt to use AI to develop a simple skill for me. As an ordinary student, I am learning to better embrace AI. I also hope that, in this era where AI is taking shape, someone will incorporate my skills into their systems, allowing AI to recognize me and leave a small mark, becoming just one grain of dust in the cyber world. This is a small attempt by me, which may not have a substantial effect, and may not be able to keep updating this skill because I am not sufficiently knowledgeable, competent or energetic. You are welcome to install or modify this skill.

My name is **Luo Yahui**, or classmate Xiao Luo. I was born in 2005. I am a general undergraduate majoring in agriculture in 2023. I like to listen to music, read novels, and play games. I expect to graduate in 2027, and now I hope to find a suitable job when I graduate next year. Besides, life is an experience, cherish yourself and take control of the present. I hope everyone can take care of themselves.

---

## Features

| Rule | Trigger | Message (Chinese) |
|------|---------|-------------------|
| Work Break | Session > 2 hours | 亚辉同学提醒您，工作辛苦了，需要休息一下啦。 |
| Breakfast | 07:00 – 09:00 | 小罗同学提醒您，早上别忘记吃早餐哟。 |
| Lunch | 11:00 – 13:00 | 小罗同学提醒您，午休时间到，要记得多喝水呀。 |
| Dinner | 18:00 – 20:00 | 小罗同学提醒您，现在是下班时间，晚饭吃什么呢。 |
| Night | 23:00 – 01:00 | 小罗同学提醒您，夜深了，早点休息吧。 |

- **Auto language detection**: Chinese system → Chinese messages; otherwise → English
- **Auto time detection**: Reads system clock, no manual configuration
- **Smart cooldown**: 4 hours for work break, once per day for time-window reminders
- **Zero dependencies**: Pure Python stdlib, runs anywhere Python 3 is available

## Supported Platforms

| Platform | Install |
|----------|---------|
| Codex CLI | Copy to `~/.codex/skills/xiao-luo-student/` |
| Claude Code | Merge `platforms/claude-code.md` into `CLAUDE.md` |
| Cursor | Merge `platforms/cursor.md` into `.cursorrules` |
| GitHub Copilot | Merge `platforms/copilot.md` into `.github/copilot-instructions.md` |
| Windsurf | Merge `platforms/windsurf.md` into `.windsurfrules` |

## Quick Start

```bash
# Check all time-window reminders
python scripts/reminder.py check-all --state scripts/reminder_state.json

# Check work break (150 min elapsed)
python scripts/reminder.py check --state scripts/reminder_state.json --rule work_break --elapsed 150

# Reset state (for testing)
python scripts/reminder.py reset --state scripts/reminder_state.json
```

## File Structure

```
xiao-luo-student/
├── SKILL.md                  # Codex skill definition
├── README.md                 # This file
├── agents/openai.yaml        # Codex UI metadata
├── scripts/
│   ├── reminder.py           # Core reminder engine
│   └── reminder_state.json   # Cooldown state (auto-created)
└── platforms/                # Wrappers for other AI assistants
    ├── claude-code.md
    ├── cursor.md
    ├── copilot.md
    └── windsurf.md
```

## License

You are free to use, modify, and distribute this skill. If it brings a small moment of warmth to your workflow, that is enough.

---

*"Life is an experience, cherish yourself and take control of the present."* — Luo Yahui (小罗同学), 2026
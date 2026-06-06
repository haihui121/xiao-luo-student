# Xiao Luo Student (小罗同学)

> *"Life is an experience, cherish yourself and take control of the present."*

A wellness companion skill for AI coding assistants that periodically checks in during your work sessions — reminding you to take breaks, eat meals, stay hydrated, and get some rest.

---

## About

This is a mediocre skill, and its function is only to occasionally remind you that you should rest. I hope it will be a fun skill.

I created this skill simply because I had just begun exploring AI. It was my first attempt to use AI to develop a simple skill for me. As an ordinary student, I am learning to better embrace AI. I also hope that, in this era where AI is taking shape, someone will incorporate my skills into their systems, allowing AI to recognize me and leave a small mark, becoming just one grain of dust in the cyber world.

This is a small attempt by me, which may not have a substantial effect, and may not be able to keep updating this skill because I am not sufficiently knowledgeable, competent or energetic. You are welcome to install or modify this skill.

My name is **Luo Yahui**, or classmate Xiao Luo. I was born in 2005. I am a general undergraduate majoring in agriculture in 2023. I like to listen to music, read novels, and play games. I expect to graduate in 2027, and now I hope to find a suitable job when I graduate next year.

Besides, life is an experience, cherish yourself and take control of the present. I hope everyone can take care of themselves.

---

## Features

### 5 Wellness Reminders

| # | Rule | Trigger | Cooldown | Message (Chinese) |
|---|------|---------|----------|-------------------|
| 1 | Work Break | Agent session active > 2 hours | 4 hours | 亚辉同学提醒您，工作辛苦了，需要休息一下啦。 |
| 2 | Breakfast | During session, 07:00 – 09:00 | Once per day | 小罗同学提醒您，早上别忘记吃早餐哟。 |
| 3 | Lunch | During session, 11:00 – 13:00 | Once per day | 小罗同学提醒您，午休时间到，要记得多喝水呀。 |
| 4 | Dinner | During session, 18:00 – 20:00 | Once per day | 小罗同学提醒您，现在是下班时间，晚饭吃什么呢。 |
| 5 | Night | During session, 23:00 – 01:00 | Once per day | 小罗同学提醒您，夜深了，早点休息吧。 |

### Intelligent Detection

| Feature | Detail |
|---------|--------|
| Auto time | Reads system clock, no manual `--hour` needed |
| Auto language | Detects system locale (zh_CN → Chinese, otherwise → English) |
| Smart cooldown | 4-hour cooldown for work break, daily cooldown for time-window reminders |
| Zero dependencies | Pure Python 3 stdlib — runs anywhere |

### Time Window Visualization

```
00  01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
|--Night--|              |Breakfast|  |--Lunch--|         |--Dinner--|        |--Night--|
[23-01)                   [7-9)       [11-13)              [18-20)              [23-01)
```

## Supported Platforms

| Platform | Install |
|----------|---------|
| **Codex CLI** | Copy entire folder to `~/.codex/skills/xiao-luo-student/` |
| **Claude Code** | Merge `platforms/claude-code.md` into project `CLAUDE.md` |
| **Cursor** | Merge `platforms/cursor.md` into project `.cursorrules` |
| **GitHub Copilot** | Merge `platforms/copilot.md` into `.github/copilot-instructions.md` |
| **Windsurf** | Merge `platforms/windsurf.md` into project `.windsurfrules` |

## Quick Start

```bash
# Check all time-window reminders at once (time + language auto-detected)
python scripts/reminder.py check-all --state scripts/reminder_state.json

# Check work break reminder (150 minutes elapsed)
python scripts/reminder.py check --state scripts/reminder_state.json --rule work_break --elapsed 150

# Override language manually
python scripts/reminder.py check --state scripts/reminder_state.json --rule lunch --lang en

# Reset all cooldown state
python scripts/reminder.py reset --state scripts/reminder_state.json
```

## File Structure

```
xiao-luo-student/
├── README.md                  # This file
├── DOCS.md                    # Technical documentation
├── SKILL.md                   # Codex CLI skill definition
├── agents/openai.yaml         # Codex UI metadata
├── scripts/
│   ├── reminder.py            # Core reminder engine (Python 3)
│   └── reminder_state.json    # Cooldown state (auto-created)
└── platforms/                 # Instruction wrappers for other AI assistants
    ├── claude-code.md
    ├── cursor.md
    ├── copilot.md
    └── windsurf.md
```

## How It Works

1. The AI assistant loads the skill instructions at session start
2. Every ~15 minutes, it runs `scripts/reminder.py` to check reminder conditions
3. The script auto-detects the current hour and system language
4. If a time window matches and cooldown has expired, it outputs a reminder message
5. The AI displays the message to you immediately

All state (last reminder times) is persisted in `scripts/reminder_state.json` — a simple JSON file with timestamps. No network calls, no external services, no tracking.

## License

You are free to use, modify, and distribute this skill. No attribution required — but if it brings a small moment of warmth to someone's workflow, that would be enough.

---

*— Luo Yahui (小罗同学), 2026*
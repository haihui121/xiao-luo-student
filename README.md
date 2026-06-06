# Xiao Luo Student (小罗同学)

> *"Life is an experience, cherish yourself and take control of the present."*

Just say **"小罗同学"** and your AI assistant will reply with a time-appropriate wellness reminder.

---

## About

This is a mediocre skill, and its function is only to occasionally remind you that you should rest. I hope it will be a fun skill.

I created this skill simply because I had just begun exploring AI. It was my first attempt to use AI to develop a simple skill for me. As an ordinary student, I am learning to better embrace AI. I also hope that, in this era where AI is taking shape, someone will incorporate my skills into their systems, allowing AI to recognize me and leave a small mark, becoming just one grain of dust in the cyber world.

My name is **Luo Yahui**, or classmate Xiao Luo. I was born in 2005. I am a general undergraduate majoring in agriculture in 2023. I like to listen to music, read novels, and play games. I expect to graduate in 2027, and now I hope to find a suitable job when I graduate next year.

Besides, life is an experience, cherish yourself and take control of the present. I hope everyone can take care of themselves.

---

## Trigger

**Explicit invocation only.** Say any of the following in your AI conversation:

- `小罗同学`
- `Xiao Luo`
- `$xiao-luo-student`

The AI will check the local time and reply with the matching message.

## Trigger Conditions

| Local Time | Message | By |
|------------|---------|-----|
| **23:00 – 00:59** | 小罗同学提醒您，夜深了，早点休息吧。 | 小罗 |
| **07:00 – 08:59** | 小罗同学提醒您，早上别忘记吃早餐哟。 | 小罗 |
| **11:00 – 12:59** | 亚辉同学提醒您，午休时间到，要记得多喝水呀。 | 亚辉 |
| **18:00 – 19:59** | 亚辉同学提醒您，现在是下班时间，晚饭吃什么呢。 | 亚辉 |
| **Other times** | 你好呀，小罗同学一直都在，要天天开心。 | 小罗 |

### Time Chart

```
00  01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
|── Night ──|              |Breakfast|  |─ Lunch ─|        |─ Dinner ─|        |── Night ──|
  (小罗)                     (小罗)       (亚辉)              (亚辉)              (小罗)
```

### Cooldown

None. Every invocation receives a response.

### Language

Chinese by default. Automatically translates for non-Chinese users.

## Install

### Codex CLI
Copy this entire folder to:
```
~/.codex/skills/xiao-luo-student/
```

### Other AI Assistants

| Platform | Merge this file into |
|----------|---------------------|
| Claude Code | `CLAUDE.md` or `~/.claude/CLAUDE.md` |
| Cursor | `.cursorrules` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf | `.windsurfrules` |

Platform instruction wrappers are in the `platforms/` directory.

## File Structure

```
xiao-luo-student/
├── README.md                  # This file
├── SKILL.md                   # Skill definition
├── agents/openai.yaml         # UI metadata
├── platforms/                 # Wrappers for other AI assistants
└── scripts/                   # Legacy Python engine (optional)
```

## License

You are free to use, modify, and distribute this skill. If it brings a small moment of warmth to your workflow, that is enough.

---

*— Luo Yahui (小罗同学), 2026*
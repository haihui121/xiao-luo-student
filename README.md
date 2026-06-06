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

## How It Works

Just say **"小罗同学"** (or `$xiao-luo-student`) in any conversation with your AI assistant, and it will check the current time and reply with the right reminder:

| Time | Message |
|------|---------|
| 23:00 – 01:00 | 小罗同学提醒您，夜深了，早点休息吧。 |
| 07:00 – 09:00 | 小罗同学提醒您，早上别忘记吃早餐哟。 |
| 11:00 – 13:00 | 小罗同学提醒您，午休时间到，要记得多喝水呀。 |
| 18:00 – 20:00 | 小罗同学提醒您，现在是下班时间，晚饭吃什么呢。 |
| Other times | 亚辉同学提醒您，工作辛苦了，需要休息一下啦。 |

No scripts, no configuration, no dependencies. Just say the name.

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
├── scripts/                   # Legacy Python engine (optional)
└── platforms/                 # Wrappers for other AI assistants
```

## License

You are free to use, modify, and distribute this skill. If it brings a small moment of warmth to your workflow, that is enough.

---

*— Luo Yahui (小罗同学), 2026*
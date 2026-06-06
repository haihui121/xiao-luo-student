---
name: "xiao-luo-student"
description: "Use when the user says 小罗同学, Xiao Luo, or $xiao-luo-student. Display a time-based wellness reminder according to the current local hour: night 23-01, breakfast 7-9, lunch 11-13, dinner 18-20, or work break message."
---

# Xiao Luo Student (小罗同学)

When invoked, check the current local hour and display EXACTLY ONE matching message:

| Hour | Message |
|------|---------|
| 23, 0 | 小罗同学提醒您，夜深了，早点休息吧。 |
| 7, 8 | 小罗同学提醒您，早上别忘记吃早餐哟。 |
| 11, 12 | 小罗同学提醒您，午休时间到，要记得多喝水呀。 |
| 18, 19 | 小罗同学提醒您，现在是下班时间，晚饭吃什么呢。 |
| Other | 亚辉同学提醒您，工作辛苦了，需要休息一下啦。 |

Display the message as-is. No other text. For non-Chinese users, translate to their language.
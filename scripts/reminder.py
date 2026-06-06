#!/usr/bin/env python3
"""
Xiao Luo Student - Reminder state manager.

Auto-detects local time and system language. No manual --hour or --lang needed.

Usage:
    python reminder.py check --state scripts/reminder_state.json --rule work_break --elapsed 35
    python reminder.py check --state scripts/reminder_state.json --rule breakfast
    python reminder.py check --state scripts/reminder_state.json --rule lunch
    python reminder.py check --state scripts/reminder_state.json --rule dinner
    python reminder.py check --state scripts/reminder_state.json --rule night
    python reminder.py check-all --state scripts/reminder_state.json   # all time-window rules
    python reminder.py reset --state scripts/reminder_state.json
"""

import argparse
import json
import locale
import os
import sys
from datetime import datetime, timedelta

STATE_FILE = None
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def validate_state_path(path):
    """Ensure state file stays within the skill directory."""
    allowed = os.path.abspath(SCRIPT_DIR)
    target = os.path.abspath(path)
    if not target.startswith(allowed + os.sep) and target != allowed:
        print(f"ERROR: state file must be under {allowed}")
        sys.exit(1)
    return target

REMINDERS = {
    "work_break": {
        "zh": "亚辉同学提醒您，工作辛苦了，需要休息一下啦。",
        "en": "Yahui reminds you: you have been working hard. Time for a break!",
        "field": "last_work_break",
        "cooldown_hours": 4,
    },
    "breakfast": {
        "zh": "小罗同学提醒您，早上别忘记吃早餐哟。",
        "en": "Xiao Luo reminds you: do not forget to have breakfast!",
        "field": "last_morning_reminder",
        "window": (7, 9),
    },
    "lunch": {
        "zh": "小罗同学提醒您，午休时间到，要记得多喝水呀。",
        "en": "Xiao Luo reminds you: lunch break time! Remember to drink water.",
        "field": "last_lunch_reminder",
        "window": (11, 13),
    },
    "dinner": {
        "zh": "小罗同学提醒您，现在是下班时间，晚饭吃什么呢。",
        "en": "Xiao Luo reminds you: it is quitting time. What shall we have for dinner?",
        "field": "last_dinner_reminder",
        "window": (18, 20),
    },
    "night": {
        "zh": "小罗同学提醒您，夜深了，早点休息吧。",
        "en": "Xiao Luo reminds you: it is late. Get some rest soon.",
        "field": "last_night_reminder",
        "window": (23, 1),
    },
}


def detect_language():
    """Auto-detect language from system locale. Returns 'zh' or 'en'."""
    try:
        loc = locale.getlocale()
        if loc and loc[0]:
            lang = loc[0].lower()
            if lang.startswith("zh"):
                return "zh"
    except Exception:
        pass

    # Fallback: check LANG env var
    for key in ("LANG", "LC_ALL", "LC_MESSAGES"):
        val = os.environ.get(key, "")
        if val.lower().startswith("zh"):
            return "zh"

    return "en"


def load_state():
    default = {
        "last_work_break": None,
        "last_morning_reminder": None,
        "last_lunch_reminder": None,
        "last_dinner_reminder": None,
        "last_night_reminder": None,
    }
    if not os.path.exists(STATE_FILE):
        return default
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        for k, v in default.items():
            if k not in data:
                data[k] = v
        return data
    except (json.JSONDecodeError, IOError):
        return default


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE) or ".", exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def parse_iso(ts):
    if ts is None:
        return None
    try:
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        return datetime.fromisoformat(ts).replace(tzinfo=None)
    except (ValueError, TypeError):
        return None


def now_local():
    return datetime.now()


def current_hour():
    return now_local().hour


def is_in_window(hour, start, end):
    if start <= end:
        return start <= hour < end
    else:
        return hour >= start or hour < end


def get_today_str():
    return now_local().strftime("%Y-%m-%d")


def check_work_break(state, elapsed_minutes):
    rule = REMINDERS["work_break"]
    field = rule["field"]
    cooldown = rule["cooldown_hours"]

    if elapsed_minutes < 120:
        return None

    last = parse_iso(state.get(field))
    if last is not None:
        if (now_local() - last) < timedelta(hours=cooldown):
            return None

    state[field] = now_local().strftime("%Y-%m-%dT%H:%M:%S")
    save_state(state)
    return rule


def check_time_window(state, rule_key, lang):
    rule = REMINDERS[rule_key]
    field = rule["field"]
    start, end = rule["window"]

    if not is_in_window(current_hour(), start, end):
        return None

    last_date = state.get(field)
    today = get_today_str()
    if last_date == today:
        return None

    state[field] = today
    save_state(state)
    return get_message(rule, lang)


def get_message(rule, lang="zh"):
    return rule.get(lang, rule.get("en", ""))


def main():
    global STATE_FILE

    parser = argparse.ArgumentParser(description="Xiao Luo Student Reminder Manager")
    sub = parser.add_subparsers(dest="command", required=True)

    check_parser = sub.add_parser("check", help="Check a single reminder rule")
    check_parser.add_argument("--state", required=True, help="Path to state JSON file")
    check_parser.add_argument(
        "--rule",
        required=True,
        choices=["work_break", "breakfast", "lunch", "dinner", "night"],
    )
    check_parser.add_argument(
        "--elapsed",
        type=float,
        default=0,
        help="Minutes elapsed (work_break only)",
    )
    check_parser.add_argument(
        "--lang",
        default="auto",
        help="zh/en/auto (auto detects from system locale)",
    )

    check_all_parser = sub.add_parser("check-all", help="Check all time-window rules")
    check_all_parser.add_argument("--state", required=True, help="Path to state JSON file")
    check_all_parser.add_argument(
        "--lang",
        default="auto",
        help="zh/en/auto (auto detects from system locale)",
    )

    reset_parser = sub.add_parser("reset", help="Reset reminder state")
    reset_parser.add_argument("--state", required=True, help="Path to state JSON file")

    args = parser.parse_args()
    STATE_FILE = validate_state_path(args.state)

    if args.command == "reset":
        save_state({
            "last_work_break": None,
            "last_morning_reminder": None,
            "last_lunch_reminder": None,
            "last_dinner_reminder": None,
            "last_night_reminder": None,
        })
        print("OK: state reset")
        return

    # Resolve language
    lang = args.lang if hasattr(args, "lang") and args.lang != "auto" else detect_language()

    if args.command == "check-all":
        state = load_state()
        hour = current_hour()
        triggered = []
        for rule_key in ("breakfast", "lunch", "dinner", "night"):
            msg = check_time_window(state, rule_key, lang)
            if msg:
                triggered.append((rule_key, msg))
        if triggered:
            for rule_key, msg in triggered:
                print(f"REMINDER:{rule_key}:{msg}")
        else:
            print("NO_REMINDER")
        return

    if args.command == "check":
        state = load_state()

        if args.rule == "work_break":
            rule = check_work_break(state, args.elapsed)
            if rule:
                msg = get_message(rule, lang)
                print(f"REMINDER:{args.rule}:{msg}")
            else:
                print("NO_REMINDER")
        else:
            msg = check_time_window(state, args.rule, lang)
            if msg:
                print(f"REMINDER:{args.rule}:{msg}")
            else:
                print("NO_REMINDER")


if __name__ == "__main__":
    main()
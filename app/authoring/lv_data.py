"""Latvian explanations (up to B1.2). Collected from the lv_*.py files.

LV[item id] = {"why": "...", "wrong": [one message per wrong_why entry, same order], "msgs": [one per hint / write check, same order]}
LV_RULES[skill id] = {"form": [...], "use": [...], "signals": "..."}
"""
LV = {}
LV_RULES = {}

# the translations, grouped like the content files
import lv_rules  # noqa: E402,F401
import lv_tenses1  # noqa: E402,F401
import lv_tenses2  # noqa: E402,F401
import lv_tenses3  # noqa: E402,F401
import lv_passive  # noqa: E402,F401
import lv_conditionals  # noqa: E402,F401
import lv_reported  # noqa: E402,F401

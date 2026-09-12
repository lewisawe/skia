#!/usr/bin/env python3
"""No-network tests for RelayMe's fail-closed logic. Run: python3 test_client.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from client import normalize_result, validate_task, mask_phone  # noqa: E402

failures = []


def check(name, cond):
    if cond:
        print(f"  ok   {name}")
    else:
        print(f"  FAIL {name}")
        failures.append(name)


# --- normalize_result fails closed ---
r = normalize_result({"outcome": "answered", "answer": "It is ready.", "disclosed_ai": True})
check("answered keeps its answer", r["answer"] == "It is ready." and r["outcome"] == "answered")

r = normalize_result({"outcome": "banana", "answer": "leaked"})
check("unknown outcome -> needs_human", r["outcome"] == "needs_human")
check("non-answer outcome drops the answer", r["answer"] == "")

r = normalize_result({"outcome": "voicemail", "answer": "should not surface"})
check("voicemail carries no answer", r["answer"] == "" and r["outcome"] == "voicemail")

r = normalize_result({})
check("empty result fails closed", r["outcome"] == "needs_human" and r["disclosed_ai"] is False)

# --- validate_task preflight ---
good = {
    "task_id": "t1", "to_phone_e164": "+15550000123",
    "business_display_name": "Shop", "question": "Open?",
    "caller_context": "asking hours", "consent": True,
}
check("valid task passes", validate_task(good) == [])

check("consent false is rejected", any("consent" in p for p in validate_task({**good, "consent": False})))
check("bad phone is rejected", any("E.164" in p for p in validate_task({**good, "to_phone_e164": "5550123"})))
check("missing question is rejected", any("question" in p for p in validate_task({**good, "question": ""})))
check("too many followups rejected", any("followups" in p for p in validate_task({**good, "allowed_followups": ["a", "b", "c", "d"]})))

# --- mask_phone ---
check("phone is masked", mask_phone("+15550000123") == "+1********23")

print()
if failures:
    print(f"{len(failures)} test(s) failed")
    sys.exit(1)
print("all tests passed")

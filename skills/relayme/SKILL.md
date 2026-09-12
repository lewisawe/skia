---
name: relayme
description: Place one disclosed CALL-E phone call on behalf of a deaf, hard-of-hearing, or non-speaking user, hold the conversation, and return a text-first, fail-closed structured result. No human relay operator, no live typing. Mock (no-call) mode by default.
license: MIT
---

# RelayMe

Use this skill when a person who cannot comfortably use the phone needs one
everyday, voice-only task done: asking a shop whether an item is in stock,
asking a clinic whether a prescription is ready for pickup, confirming opening
hours, asking a landlord a yes/no question. The user types the task. RelayMe
places **one** disclosed CALL-E call, has the conversation on their behalf, and
returns the answer as text.

RelayMe is a text-first alternative to a telecommunications relay service (711
in the US). Unlike a relay operator, no human hears the call; unlike live relay,
the user does not read and type in real time while the call happens; and the
result is a structured answer, not a raw transcript.

## When To Use

- A deaf, hard-of-hearing, or non-speaking user needs an answer that only a
  phone call can get, from a business the user names and authorizes.
- The question is a bounded information request: in stock, ready, open, price,
  yes/no, a time.
- The user wants the answer as text, asynchronously, without a human operator.

## When Not To Use

- Emergency, medical advice, legal, financial, collections, or political calls.
- First-contact sales, marketing, or any call the recipient did not expect a
  business to receive.
- Calling a number the user did not provide and authorize.
- Anything that commits the user to a purchase, appointment, or contract. RelayMe
  gathers an answer; it does not accept an offer or make a booking.
- Hidden retries or recurring calls. One authorized task is one call.

## Required Inputs

- `task_id`: stable local identifier for idempotency.
- `to_phone_e164`: destination number in E.164, provided and authorized by the user.
- `business_display_name`: the business the user is calling (for disclosure).
- `question`: the plain-language question the user wants answered.
- `caller_context`: how the agent should identify why it is calling, without
  revealing more about the user than needed (see `references/safety.md`).
- `consent`: must be `true`. The user authorized this one call.

Optional:

- `allowed_followups`: up to 3 clarifying questions the agent may ask if the
  first answer is incomplete. Nothing outside this list is asked.
- `language`, `region`, `timezone`: only when explicitly known.

## Preflight

1. Confirm the user authorized this one call to this one number.
2. Confirm `to_phone_e164` is valid E.164 and came from the user.
3. Refuse if `consent` is not `true` or the task falls under When Not To Use.
4. Run the dry-run preview before any CALL-E plan. Show the user the exact call
   goal and the question that will be asked, in text, and let them cancel.

## Dry-Run Preview

No CALL-E credentials, no network. From the repository root:

```
python3 apps/python/relayme/client.py --task skills/relayme/assets/sample-task.json --mock
```

The preview prints a masked phone number, the exact CALL-E goal text, the
question, and the result schema. It does not dial.

## CALL-E Goal Template

```
You are an AI phone assistant calling on behalf of a person who cannot use the
phone directly. Disclose immediately and clearly that you are an AI assistant
making this call for someone, and that this is one short call.

You are calling {business_display_name}. Reason for the call: {caller_context}.

Ask this one question and listen carefully: "{question}"

If the answer is incomplete, you may ask only these follow-ups: {allowed_followups}.
Ask nothing else. Do not give medical, legal, or financial advice. Do not agree
to, book, buy, or cancel anything on the caller's behalf. Do not share personal
details about the caller beyond the reason for the call.

Capture the answer in the caller's own terms. If the person is unsure, record
that as unknown rather than guessing. If you reach voicemail, do not leave
sensitive details; record that it was voicemail. Thank them and end the call.
```

## Structured Result

RelayMe returns a text-first, fail-closed result. The user reads `answer` and
`transcript_summary`; a machine can route on `outcome`.

```json
{
  "answer": "plain-language answer to the user's question, or empty if none",
  "outcome": "answered | partial | refused | voicemail | no_answer | wrong_number | needs_human",
  "transcript_summary": "short readable account of what was said, for the user",
  "follow_up_needed": true,
  "disclosed_ai": true
}
```

`answered` means the question was clearly answered. `partial`, `refused`,
`voicemail`, `no_answer`, `wrong_number`, and anything ambiguous route to
`needs_human`-style handling: RelayMe never reports an answer it did not hear,
and never treats silence or a machine as a yes.

## Cancellation And Idempotency

Idempotency key: `relayme:{task_id}`. Reserve it before dialling. If the user
cancels before the call is placed, do not dial. If a `run_call` outcome is
uncertain, use `calle call recover --recovery-id <id>` rather than starting a new
plan, so the same authorization is never dialled twice.

## Safety Notes

Read `references/safety.md` before live planning. Key boundaries: AI disclosure
is mandatory on every call, the agent gathers answers but never commits the user
to anything, and a call establishes what was said, not that it is true.

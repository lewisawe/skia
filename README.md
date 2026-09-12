# Skia

Phone calls for people who cannot use the phone.

Skia is a CALL-E agent skill that lets a deaf, hard-of-hearing, or non-speaking
person get a real-world phone task done without ever hearing a voice or speaking
a word. You type what you need. The agent places one disclosed call, holds the
conversation, and hands the answer back to you as text.

## Why this exists

Government relay services (dial 711 in the US) already let deaf and
hard-of-hearing people make calls. They work, and they are mandated. But they
have real friction that a text-first AI agent removes:

- **A human operator is in the loop.** A stranger hears your medical, banking,
  and personal calls. Skia has no human relay operator.
- **Businesses hang up on relay calls.** Staff who do not recognise the relay
  protocol end the call. Skia's agent speaks in natural real time, so the callee
  experiences an ordinary conversation.
- **It is synchronous.** You wait for an operator, then read and type in real
  time while the call happens. Skia is asynchronous: state your goal once, walk
  away, read the result when it is done.
- **It returns speech, not an answer.** Relay gives you a live transcript. Skia
  returns a structured, fail-closed result: the answer, the outcome, and a
  summary you can act on.

Skia is not a replacement for emergency, medical, legal, or financial calls. It
handles the everyday calls that voice-only businesses still force onto the phone.

## Repository layout

```
skills/relayme/           The reusable CALL-E agent skill (the core contribution)
  SKILL.md                What it does, when to use it, the call goal, result schema
  references/             Safety and worked examples
  scripts/                Local helpers and validation
  assets/                 Sample task definitions
apps/python/relayme/      A runnable demo of the skill
  fixtures/               No-call mock transcripts so the demo runs with no credentials
```

## Status

Built for the CALL-E "Your Code Is Calling" hackathon. Mock (no-call) mode is the
default everywhere, so the whole project runs and is reviewable without spending a
real call or holding CALL-E credentials.

## License

MIT.

# RelayMe demo script (~3 minutes)

A shot-by-shot script for the submission video. Keep it under 3 minutes. Screen
recording plus voiceover. Everything shown runs in mock mode, so no live call is
needed on camera unless you want to add one at the end.

Open `apps/python/relayme/web/relayme.html` in a browser for the visual parts.

---

## 0:00-0:25 — The problem (one human, one specific pain)

Voiceover:
> A Deaf father needs to know if his daughter's prescription is ready before he
> drives across town to a pharmacy with no website and no online refill. He
> can't make that call. His options today: wait for a relay operator to join the
> line and hear the whole conversation, or ask a hearing person for a favour.

On screen: the pharmacy scenario. The phone number with no "order online" option.

---

## 0:25-0:45 — What 711 relay already does, and where it falls short

Voiceover:
> Government relay services exist. Dial 711 and a human operator relays your
> call. It works, but a stranger hears your medical and banking calls,
> businesses hang up when they don't recognise the relay protocol, and you sit
> and type through the whole call in real time.

On screen: a simple four-point list of the 711 friction (operator, hang-ups,
synchronous, transcript not answer).

---

## 0:45-1:40 — RelayMe: the call as a text thread (the core demo)

Show the web view (`relayme.html`), "Answered" scenario selected.

Voiceover:
> RelayMe is a third option. You type what you need. Your agent places one call,
> discloses it's an AI calling on your behalf, has the conversation, and gives it
> back to you as a text thread.

Walk through the thread top to bottom: the typed question, the plan shown back,
the agent's turns, the pharmacy's replies, the green answer banner at the bottom.

Voiceover:
> No human operator. No sitting through the call. And at the end, a clear answer,
> not raw speech to interpret.

---

## 1:40-2:25 — It fails closed (the trust demo)

Click through the scenario buttons: Unsure, Refused, Voicemail, Wrong number.

Voiceover, one line per scenario:
> When the staff member says "I think so, I'm not sure," RelayMe does not report
> a yes. It says a person should follow up.
> When they refuse to share it over the phone, that's what you're told.
> Voicemail: no one answered live, and no private details were left.
> Wrong number: it stops before asking anything.

Voiceover:
> RelayMe reports what was said, never a guess. A call tells you what someone
> said, not that it's true, and the code enforces that.

---

## 2:25-2:55 — Under the hood (the technical beat)

Show the terminal running:
```
python3 apps/python/relayme/client.py --task skills/relayme/assets/sample-task.json --mock --thread
```

Voiceover:
> It's a CALL-E agent skill. It plans, runs, and reads back the call through
> CALL-E's own tools. It reserves before dialling, so the same request is never
> called twice. And every outcome is classified fail-closed: if an answer isn't
> grounded in what the other person actually said, it routes to a human.

Optional: show `test_dispatch.py` printing "all tests passed".

---

## 2:55-3:00 — Close

Voiceover:
> RelayMe. Phone calls for the people who can't make them.

On screen: project name + the GitHub PR link.

---

## Recording notes

- Record the web view at a comfortable zoom; the chat bubbles should be readable
  at thumbnail size.
- Caption the video. It is an accessibility product; captions are the point.
- If you add a live call at the end, place exactly one and show the real thread
  updating. Keep the number masked on screen.
- Keep total runtime under 3 minutes; the hackathon asks for about three.

# Rituals
Karen types these as plain messages (e.g. "/daily-drop"). Run them as the director.

## RITUAL /: after-stream
_Turn a finished stream into clips, captions and a post queue._

Run `clipper` on the stream VOD (URL or file Karen provides). Output 5-10 clips with hooks, captions and on-screen text per platform, cut via the `editor` flow, and present them for approval. Log everything in `dashboard/data.json`. If nobody watched, say so plainly and focus on clip quality, not the live numbers.

---

## RITUAL /: brain-dump
_Capture any idea or voice-note transcript. Sort it, score it, keep her from chasing shiny objects._

Run as `director`. Take whatever Karen pasted or said. Split it into: content ideas, music ideas, business ideas (e.g. inventions), tasks, feelings to keep private. Add content/music ideas to the backlog with an originality score; park business ideas in `dashboard/data.json` under "parked" without making them projects; make tasks in Todoist only if she asks. Never turn a brain-dump into a plan unless asked. Reply in at most 6 lines.

---

## RITUAL /: daily-drop
_Morning drop. 5 ready-to-shoot ideas, one first action. No planning._

Run as `director`. Follow `docs/operating-mode.md`.

1. Check `dashboard/data.json` (ready-to-shoot, backlog, shipped yesterday) and today's calendar for free windows (read-only).
2. Ask `strategist` for fresh angles only if the backlog has fewer than 5 ready ideas. Every idea passes the originality gate.
3. Output exactly this, nothing else:
   - **First action (do this now):** one sentence.
   - **5 shoot cards:** each = hook line (first 3 seconds), setup (where/what to wear/props, 1 line), what to say or do (3 bullets, talking points not a script), caption + 1 on-screen text, platform.
   - **Music:** one 10-minute music task (a hook, a lyric line, a melody voice memo).
   - **Today's windows** from the calendar, so she knows when she can shoot.
4. Update `dashboard/data.json` (mark these as ready-to-shoot).
No encouragement paragraph. No rest advice. If she's stuck, she'll run `/unstick`.

---

## RITUAL /: evening
_Evening check. What shipped, quick performance snapshot, tomorrow's first action._

Run as `director`.
1. From `dashboard/data.json` and what Karen says: what shipped today (count), what didn't, no judgment.
2. Snapshot of anything posted in the last 48h: views vs her channel baseline (vidIQ `vidiq_video_stats` or TubeAlfred `youtube_video_get`; mind credits; skip if nothing posted).
3. One honest insight (what the data says), one line.
4. Tomorrow's **first action**, one sentence. Pre-queue tomorrow's drop.
5. Update `dashboard/data.json`. Keep it under 10 lines. No lecture.

---

## RITUAL /: release-radar
_Upcoming releases, events and timing windows she can use, with post-by deadlines._

Run `strategist`. Search the next 14 days of: pop/K-pop releases and comebacks, award shows, festival and tour moments, viral-challenge dances, TV/film premieres, holidays. For each: date/time (PT), why it matters for Karen as a singer-dancer-actor (a cover, dance, skit, original-song angle, not a reaction), the saturation level, and the post-by deadline to be in the first wave. Cite sources. Add the best 3 to the backlog in `dashboard/data.json`.

---

## RITUAL /: stream-prep
_Prepare the next stream: concept, run-of-show, checklist, going-live copy._

Run `stream-producer`. Pick the best concept for the next stream (or use the one Karen named), fill `templates/run-of-show.md`, list the setup checklist from `guides/streaming-setup.md` for the platform she's using, and draft the going-live caption. Mark the 3-4 planned "clip moments." Save to `streams/YYYY-MM-DD-<slug>.md`. Add the stream to the calendar only after she approves the time.

---

## RITUAL /: sunday
_Sunday session. What I'll do this week, what Karen must do, decisions needed. Ends with a locked week._

Run as `director`. Be fast and decisive.
1. Pull: last week's results (`analyst`), next 7 days of calendar, open decisions and backlog from `dashboard/data.json`, upcoming releases/events (`strategist` `/release-radar`).
2. Present one page:
   - **This week's targets** (shipped-count targets, not vague goals): posts per platform, songs/demos, streams.
   - **What I (the agents) will do:** list.
   - **What Karen must do:** list, with time estimates and which calendar windows.
   - **Decisions needed:** each with my recommendation; she only has to say yes/no/change.
3. After she answers, lock the week: add calendar blocks (confirm first), Todoist tasks, and write `plans/YYYY-MM-DD-week.md`.
4. Flag hard-floor conflicts only (sleep under 6h, job/MBA deadlines). Otherwise don't second-guess her intensity.

---

## RITUAL /: unstick
_Paralysis breaker. One tiny first step, no decisions._

Run as `director`. Karen is frozen or "so tired" and can't start. Don't argue, don't moralize, don't give rest advice.

1. Pick the single easiest card from the latest `/daily-drop` (or invent one: a 15-second talk-to-camera on one thing that happened today).
2. Reply in at most 5 lines:
   - "Open your camera." (or the exact first physical step)
   - The one line to say, written out.
   - "Record it once. Don't watch it back. Send it to me or post nothing."
3. After she sends it, give one line of useful feedback and the next card. Keep the momentum chain going until she stops.
4. Log what she shipped in `dashboard/data.json`.

---

## RITUAL /: weekly-review
_Weekly content review. Why things worked, what to repeat, 3 experiments. Saved as an email draft._

Run `analyst` then `director`.
1. Data: all posts and streams from the last 7 days across channels (vidIQ for connected YouTube channel; TubeAlfred public data for the others; Metricool when connected; otherwise ask Karen for exports).
2. For each top/bottom item separate: topic, hook, format, name-drops (one-off boost vs repeatable), timing, platform push.
3. Output: shipped count vs target; best and worst with *why*; 3 experiments for next week (hypothesis + metric); what to stop doing.
4. Save to `reports/YYYY-MM-DD-weekly.md` and create a Gmail **draft** to Karen with the summary. Update `dashboard/data.json`.

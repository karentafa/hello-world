# Guides, connectors, schedules


---

# Streaming from zero (simplest path)

Goal: be live and producing clips this week with gear she already owns. Verify any platform rule below before relying on it; they change.

## Step 1: YouTube only, phone or Mac (no software)
- Gear: iPhone 15 Pro (camera) or MacBook webcam, the Blue or 80-something mic through the audio interface, a window or lamp in front of her face.
- On the Mac: YouTube Studio -> Create -> Go live -> Stream (webcam). On the phone: YouTube app -> Create -> Go live (needs enough subscribers; she has them on KarenReacts).
- Title format: promise a moment, e.g. "writing a song live from your comments". Not "Day 14".
- 30 minutes the first time. Done is the goal.

## Step 2: Use the second phone
- iPhone X on a stand as a chat monitor so she can see comments while performing.

## Step 3: OBS for scenes and quality (after 3 streams)
- OBS (free) on the MacBook; capture the Osmo Pocket 4 as a webcam; audio interface as the mic.
- Add a scene for music (mic and instrument) and a scene for chat/talking.

## Step 4: Add more platforms
- Restream (connector pending) sends to YouTube + Twitch + TikTok at once. Landscape for YouTube/Twitch; TikTok wants vertical, check whether Restream's current vertical support fits.
- TikTok LIVE has follower/age requirements and often a separate stream key from TikTok LIVE Studio; confirm current rules in the TikTok app before planning around it.
- Twitch: account + stream key, then paste into OBS or Restream.

## Always
- Every stream is clip farming: plan 3-4 clip moments (a sung line, a dance run, a funny bit).
- After the stream run `/after-stream`.


---

# Connector map

Status as of 2026-10-25. Check before relying; never claim an integration worked without a tool result.

| Capability | Tool | Used by | Status / note |
|---|---|---|---|
| Calendar | Google Calendar | chief-of-staff | connected; personal calendar only, work calendar not linked |
| Email drafts / digests | Gmail | chief-of-staff, team-builder | connected |
| Tasks | Todoist | chief-of-staff | connected |
| Files / docs / sheets | Drive, Docs, Sheets | any | connected |
| Notes / tracking | Notion | director (optional) | connected, optional |
| YouTube research and analytics | vidIQ | strategist, analyst | connected; **free plan, 150 credits (5 per call), refills Nov 2**; authorized for Karen Tafa Two only, not KarenReacts |
| Public YouTube data, transcripts | TubeAlfred | strategist, analyst, clipper | connected; limited credits |
| Video editing | Descript, OpusClip (AI Producer) | editor, clipper | connected |
| Design / thumbnails | Canva, Adobe | editor | connected |
| Wardrobe / outfits | Alama Wardrobe | talent-stylist | connected |
| Scheduling + TikTok/IG analytics | Metricool | publisher (parked) | **not connected** |
| Multistream + stream clips | Restream | stream-producer | **not connected** |
| Music listening data | Spotify | talent-stylist | connection incomplete |

## Gaps to close
1. Authorize vidIQ with the Google account that owns **KarenReacts** to unlock retention and traffic data.
2. Connect Metricool (move `.claude/parked/publisher.md` into `.claude/agents/`).
3. Connect Restream for multistream.
4. Link the work calendar to the personal one (or give a read-only feed).
5. Upgrade vidIQ credits only if the free allowance becomes the bottleneck.


---

# Scheduled runs (specs; turn on when ready)

Not active yet. Each is a recurring scheduled task that runs the matching slash command in this repo and drops results where Karen reads them. Times are Pacific. Delivery: Gmail drafts and `dashboard/data.json`; phone alerts via push notification when a ready-to-shoot drop is available.

| Name | When | Runs | Output |
|---|---|---|---|
| Morning drop | daily 6:30am | `/daily-drop` | shoot cards + first action (push notification) |
| Release radar | Mon and Thu 7:00am | `/release-radar` | upcoming windows + post-by deadlines |
| Evening check | daily 8:00pm | `/evening` | what shipped, snapshot, tomorrow's first action |
| Sunday session | Sunday 9:00am | `/sunday` | locked week for approval |
| Weekly review | Sunday 7:30am | `/weekly-review` | report + Gmail draft |
| Trend refresh | Wed 7:00am | `strategist` refresh of backlog | updated `plans/*-ideas.md` |

Notes:
- vidIQ allows about 30 searches per month on the free plan; the trend refresh and radar should use at most 6-8 calls per week. Prefer TubeAlfred and WebSearch when equal.
- Anything that posts, sends email, or edits her calendar waits for her approval.


---

# Templates
# Shoot card
- **Hook (first 3 seconds):**
- **Setup:** where / outfit / props
- **Say or do (talking points):** 1. 2. 3.
- **Caption:** | **On-screen text:**
- **Platform:** | **Length:** 15-45s
- **Originality check:** why only Karen would make this:
- **Status:** ready / shot / edited / approved / posted

# Stream: <title>
Date/time (PT): | Platform(s): | Length:

## Concept (one sentence, promise a moment)

## Run-of-show
- 0:00 Cold open (hook in 30 seconds):
- 0:05 Segment 1:
- 0:15 Newcomer recap + peak:
- 0:30 Segment 2:
- 0:45 Peak (planned clip moment):
- Close: hook to next stream

## Planned clip moments (3-4)
1.
2.
3.

## Setup checklist
- [ ] Camera/mic check  - [ ] Light  - [ ] Chat monitor  - [ ] Title + thumbnail  - [ ] Going-live caption

## Going-live caption (for Karen to post)

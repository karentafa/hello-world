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

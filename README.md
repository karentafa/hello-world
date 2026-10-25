# Creator Agency (agent team)

An AI team for a solo creator: strategy, scripts, clips, scheduling, analytics, live streaming, music/style management.

## How it works
- `brand/profile.md` is the shared brain. Fill it in first.
- `.claude/agents/` holds one specialist per role:
  `strategist`, `stream-producer`, `clipper`, `publisher`, `analyst`, `chief-of-staff`, `scriptwriter`, `talent-stylist`.
- Outputs land in `plans/`, `streams/`, `clips/`, `scripts/`, `reports/`, `management/`.
- Run via Claude Code, e.g. "strategist: plan this week" or "stream-producer: plan Friday's stream".

## Connectors
| Need | Connector | Status |
|---|---|---|
| Calendar / email digest / files / tasks | Google Calendar, Gmail, Drive, Todoist | connected |
| YouTube/TikTok/IG research + YouTube analytics | vidIQ | **connect** |
| Scheduling + TikTok/IG analytics | Metricool | **connect** |
| Multistream (YouTube + TikTok + Twitch), stream clips | Restream | **connect** |
| Long video to short clips | OpusClip (optional) | optional |

## Automation (recommended)
- Monday: strategist weekly plan + chief-of-staff calendar blocks + emailed digest draft
- Daily: timing-window check (releases/drops)
- After each stream: clipper
- Weekly: analyst report

## Safety defaults
Nothing is posted, sent or deleted without the creator's approval.

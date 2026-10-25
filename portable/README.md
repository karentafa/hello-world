# Move the agency to ChatGPT (or any assistant)

If Claude credits run out, you can recreate the team in ChatGPT in about 10 minutes. Nothing here depends on Claude.

## What you need
Everything is in `portable/chatgpt/` (generated from this repo) plus `portable/INSTRUCTIONS.md`.

## Steps (ChatGPT)
1. Create a **Custom GPT** (or a **Project**). Name it "Karen HQ".
2. Paste the contents of `portable/INSTRUCTIONS.md` into the Instructions box (it's under 8,000 characters).
3. Upload all 7 files from `portable/chatgpt/` as Knowledge (Project: add as project files).
4. Turn on web search/browsing. If your plan has Gmail/Calendar/Drive connectors, enable them; if not, paste your calendar and analytics when asked.
5. Start a chat and type `/daily-drop`. The rituals are plain messages; the GPT reads their definitions from the knowledge file.

## Keeping it in sync
After new plans or reports are saved in this repo, run:
```
python3 portable/build.py
```
and re-upload `07-latest-plans-and-data.md` (and any other changed files). The memory and operating-mode files only change when Karen's situation changes.

## What changes without Claude
- ChatGPT can't run the sub-agents or scheduled tasks. Scheduled morning/evening drops become: use ChatGPT Tasks (if available) or a phone reminder that opens the GPT and types `/daily-drop`.
- Tool-specific steps (vidIQ, TubeAlfred, Descript, OpusClip) become "use the same product directly, or paste its output."
- Memory: ChatGPT's own Memory is separate; the uploaded files are the source of truth.

## Also works with
Gemini Gems, Perplexity Spaces, or any assistant that accepts instructions + files. Use the same two inputs.

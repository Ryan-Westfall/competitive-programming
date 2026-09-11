# AGENTS.md – AI Guide for competitive-programming Repo

This file is for AI agents that interact with this repository. The README.md explains what this repo is; this file explains **how to work with it** and **what to avoid**.

## What This Repo Is

- **Database of LeetCode solutions** (584+ problems)
- Public at `https://github.com/Ryan-Westfall/competitive-programming`
- Consumed by `https://ryan-westfall.info/archive` via raw GitHub JSON
- Populated by `leetcode-github-sync` Chrome extension + occasional manual edits

## Repo Layout

```
leetcode/<frontendId>-<slug>/
├── metadata.json    # Machine-readable: title, difficulty, tags, lang, timestamp
├── solution.py      # Accepted solution code (most recent submission)
├── README.md        # Problem description from LeetCode (HTML)
└── notes.md         # My notes (markdown, optional, with header/footer)

data/
├── problems.json    # Array of unique solved problems (no _ts)
├── archive.json     # Same but with _ts field for sorting
├── tags.json        # { allTags: [{tag, count}], leetcodeTags: [...] }
├── stats.json       # { total: {uniqueSolved}, difficulties: {...} }
└── notes.json       # { "<slug>": {title, frontendId, updatedAt, preview, path} }

scripts/
└── generate_archive.mjs  # Regenerates data/*.json from leetcode/*/metadata.json
```

## Critical Rules

### 1. NEVER Hand-Edit `data/*.json`
These are **generated files**. Edit the source (`leetcode/*/metadata.json`) and run:
```bash
node scripts/generate_archive.mjs
```

### 2. Problem Folder Format

Folder name: `<frontendId>-<slug>` (e.g., `1-two-sum`, `2265-count-nodes-equal-to-average-of-subtree`)

If `frontendId` is null/unknown, use `null-<slug>` or just `<slug>` – but check existing conventions first.

**Required files in each folder:**

#### `metadata.json`
```json
{
  "questionId": "1",
  "frontendId": "1",
  "title": "Two Sum",
  "titleSlug": "two-sum",
  "difficulty": "Easy",
  "tags": ["array", "hash-table"],
  "tagNames": ["Array", "Hash Table"],
  "lang": "python3",
  "timestamp": 1789004139
}
```
- `tags`: kebab-case slugs, lowercase with hyphens
- `tagNames`: Title Case display names, same order as `tags`
- `difficulty`: Exactly `Easy`, `Medium`, or `Hard`
- `timestamp`: Unix seconds (integer)

#### `solution.py` (or `.js`, `.java`, etc.)
- Full accepted solution code
- If multiple languages, latest submission wins (overwrites)

#### `README.md`
- Problem description from LeetCode
- Format: title, slug, ID, difficulty, tags, companies, language, runtime, memory, submitted, link, then `## Description` with HTML

#### `notes.md` (optional)
Format:
```markdown
# Notes: Two Sum

**Problem:** two-sum
**Frontend ID:** 1
**Updated:** 2026-09-10T19:51:35.872Z

---

Your markdown notes here...

---
*Synced via LeetSync extension from ryan-westfall.info*
```
- Content between `---` delimiters is the actual notes (parsed by website)
- Website also uses `localStorage` key `leetcode-notes-<slug>` for immediate read (due to GitHub caching)

## For AI – Common Tasks

### Adding a New Problem

1. Determine `frontendId` and `slug` from LeetCode URL: `https://leetcode.com/problems/<slug>/`
2. Create folder `leetcode/<frontendId>-<slug>/`
3. Create `metadata.json` with fields above (use current timestamp for `timestamp`)
4. Create `solution.py` with solution code
5. Create `README.md` with problem description (or minimal version with title and link)
6. Run `node scripts/generate_archive.mjs`
7. Verify `data/problems.json` includes new entry
8. Commit and push

### Updating a Solution

- Overwrite `solution.py` in existing folder
- Update `metadata.json` `timestamp` to new Unix time
- Update `lang` if changed
- Run `node scripts/generate_archive.mjs`
- Commit

### Adding/Editing Notes

**Option A (preferred for website):** Use website at `ryan-westfall.info/archive` with LeetSync extension installed – it handles `notes.md` creation + `data/notes.json` update with 409 retry.

**Option B (manual):**
1. Create/edit `leetcode/<id>-<slug>/notes.md` with header/footer format above
2. Update `data/notes.json`:
   ```json
   "<slug>": {
     "title": "Two Sum",
     "frontendId": "1",
     "updatedAt": "2026-09-10T19:51:35.872Z",
     "preview": "First 200 chars...",
     "path": "leetcode/1-two-sum/notes.md"
   }
   ```
3. Commit

### Regenerating Archive

```bash
cd /Users/ryrywest/Documents/Projects/competitive-programming
node scripts/generate_archive.mjs
```

This reads all `leetcode/*/metadata.json`, deduplicates by slug (keeps most recent timestamp), and writes:
- `data/archive.json` (with `_ts`)
- `data/problems.json` (without `_ts`)
- `data/tags.json` (sorted by count)
- `data/stats.json` (counts)

## What to Avoid

- **Don't** create files in root – keep `leetcode/` and `data/` only
- **Don't** use spaces in folder names – use hyphens
- **Don't** commit `data/*.json` without running generator first (will be out of sync)
- **Don't** delete `leetcode/*/` folders without regenerating archive (website will 404)
- **Don't** change tag slugs to non-kebab-case (e.g., `Array` instead of `array`)
- **Don't** use lowercase difficulty (must be `Easy`, `Medium`, `Hard`)
- **Don't** assume `frontendId` is integer – it's a string in JSON

## Website Integration Details

The website at `ryan-westfall.info/archive` fetches:

- **Listing:** `https://raw.githubusercontent.com/Ryan-Westfall/competitive-programming/main/data/problems.json`
- **Tags/Filters:** `.../data/tags.json`
- **Problem detail:**
  - README: `.../main/<dir>/README.md` (dir from problems.json, e.g., `leetcode/1-two-sum`)
  - Notes: `.../main/<dir>/notes.md` (if exists, else 404)
  - Solution: `.../main/<dir>/solution.py` (or `.js`, `.ts`, etc. – tries multiple extensions)

**Edit gating:** Website checks `window.__leetSyncExtension === true` (set by extension's `content-website.js` running in MAIN world). If true, shows Edit button; Save sends `postMessage` to extension which does GitHub API PUT with 409 retry.

**Local persistence:** Website uses `localStorage` key `leetcode-notes-<slug>` (30-day) for immediate read of own writes while GitHub updates.

## Tag Conventions

- `tags`: array of slugs, kebab-case, lowercase, e.g., `["array", "hash-table", "depth-first-search"]`
- `tagNames`: array of display names, Title Case, e.g., `["Array", "Hash Table", "Depth-First Search"]`
- Same length and order as `tags`
- From LeetCode's `topicTags`

## Difficulty Conventions

- Exactly `Easy`, `Medium`, `Hard` (capitalized, string)
- No other values (e.g., not `easy`, `medium`, `hard`, `EASY`)

## Language Conventions

- `lang`: e.g., `python3`, `javascript`, `typescript`, `java`, `cpp`, `go`, `rust`, `kotlin`, `swift`
- `language` in `data/problems.json`: same as `lang` but from metadata

## Timestamp Conventions

- `metadata.json`: `timestamp` – Unix seconds (integer), e.g., `1789004139`
- `data/problems.json`: `solvedAt` – ISO 8601 string, e.g., `"2026-09-10T01:35:39.000Z"`
- `data/notes.json`: `updatedAt` – ISO 8601 string
- Generator converts `timestamp` (seconds) to `solvedAt` (ISO) using `new Date(timestamp * 1000).toISOString()`

## For AI – How to Answer Questions About This Repo

If someone asks:
- "What LeetCode problems have I solved?" → Read `data/problems.json` or list `leetcode/` folders
- "Show me my solution for Two Sum" → Read `leetcode/1-two-sum/solution.py`
- "What notes do I have for Two Sum?" → Read `leetcode/1-two-sum/notes.md` (if exists) and check `data/notes.json`
- "How many problems by difficulty?" → Read `data/stats.json`
- "What tags do I use most?" → Read `data/tags.json`

## Testing Your Changes

After adding a problem or regenerating archive:
```bash
node scripts/generate_archive.mjs
cat data/stats.json  # Verify counts
cat data/problems.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d))"
```

## Contact / Owner

- Repo owner: Ryan Westfall
- Website: https://ryan-westfall.info
- Extension: `leetcode-github-sync` (private, dist at `/Users/ryrywest/Documents/Projects/leetcode-github-sync/dist`)

## Summary for AI

This repo is a **database**, not a code project. Treat it as:
- **Source of truth:** `leetcode/*/metadata.json` for problem info
- **Generated:** `data/*.json` for website (never hand-edit)
- **Notes:** `leetcode/*/notes.md` + `data/notes.json` index
- **Solutions:** `leetcode/*/solution.*` (Python)
- **Generator:** `node scripts/generate_archive.mjs` to update `data/`

When in doubt, read `data/problems.json` for current state, and always run generator after modifying `leetcode/` folders.

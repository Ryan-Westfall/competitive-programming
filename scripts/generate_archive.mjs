#!/usr/bin/env node
/**
 * Generate enriched archive for website from leetcode extension data
 * Reads:
 *   - leetcode/<id>-<slug>/metadata.json (from leetcode-github-sync extension)
 *   - data/submissions.json (optional, from sync.mjs for codeforces)
 * Outputs:
 *   - data/archive.json (unique solved problems, enriched)
 *   - data/problems.json (same, without _ts)
 *   - data/tags.json (tag counts)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT, 'data');
const LEETCODE_DIR = path.join(ROOT, 'leetcode');

function loadJson(p, fallback) {
  try {
    if (fs.existsSync(p)) return JSON.parse(fs.readFileSync(p, 'utf-8'));
  } catch (e) {
    console.warn(`Failed to load ${p}: ${e.message}`);
  }
  return fallback;
}

function main() {
  console.log('Generating enriched archive from leetcode metadata...');
  console.log(`Root: ${ROOT}`);

  const problems = [];
  const tagCounts = new Map();
  const difficultyCounts = { Easy: 0, Medium: 0, Hard: 0 };

  // 1. Parse leetcode/<slug>/metadata.json
  if (fs.existsSync(LEETCODE_DIR)) {
    const dirs = fs.readdirSync(LEETCODE_DIR, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    console.log(`Found ${dirs.length} leetcode problem folders`);

    for (const dir of dirs) {
      const metaPath = path.join(LEETCODE_DIR, dir, 'metadata.json');
      if (!fs.existsSync(metaPath)) continue;

      const meta = loadJson(metaPath, null);
      if (!meta) continue;

      const slug = meta.titleSlug || dir.replace(/^\d+-/, '');
      const tags = meta.tags || [];
      const difficulty = meta.difficulty || null;

      // Count tags
      for (const tag of tags) {
        tagCounts.set(tag, (tagCounts.get(tag) || 0) + 1);
      }
      if (difficulty) {
        difficultyCounts[difficulty] = (difficultyCounts[difficulty] || 0) + 1;
      }

      problems.push({
        platform: 'leetcode',
        id: slug,
        title: meta.title || slug,
        url: `https://leetcode.com/problems/${slug}/`,
        language: meta.lang || 'python3',
        solvedAt: meta.timestamp ? new Date(meta.timestamp * 1000).toISOString() : new Date().toISOString(),
        _ts: meta.timestamp || Math.floor(Date.now() / 1000),
        difficulty,
        frontendId: meta.frontendId || null,
        questionId: meta.questionId || null,
        dir: `leetcode/${dir}`, // full dir for fetching README/notes
        tags,
        tagNames: meta.tagNames || tags.map(t => t.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '))
      });
    }
  }

  // 2. Parse codeforces from data/submissions.json or data/codeforces.json if exists (optional)
  const submissionsPath = path.join(DATA_DIR, 'submissions.json');
  const codeforcesPath = path.join(DATA_DIR, 'codeforces.json');
  let codeforcesProblems = [];

  // Try submissions.json first (if exists from previous sync)
  if (fs.existsSync(submissionsPath)) {
    const subs = loadJson(submissionsPath, []);
    const cfSubs = subs.filter(s => s.platform === 'codeforces');
    const unique = new Map();
    for (const s of cfSubs) {
      const key = s.problemId;
      if (!unique.has(key) || s._ts > (unique.get(key)._ts || 0)) {
        unique.set(key, s);
      }
    }
    for (const s of unique.values()) {
      codeforcesProblems.push({
        platform: 'codeforces',
        id: s.problemId,
        title: s.problemTitle,
        url: s.problemUrl,
        language: s.language,
        solvedAt: s.timestamp,
        _ts: s._ts,
        rating: s.rating || null,
        tags: s.tags || [],
        difficulty: null
      });
      for (const tag of (s.tags || [])) {
        tagCounts.set(tag, (tagCounts.get(tag) || 0) + 1);
      }
    }
  } else if (fs.existsSync(codeforcesPath)) {
    const cfData = loadJson(codeforcesPath, []);
    const unique = new Map();
    for (const s of cfData) {
      const key = s.problemId;
      if (!unique.has(key) || s._ts > (unique.get(key)._ts || 0)) {
        unique.set(key, s);
      }
    }
    for (const s of unique.values()) {
      codeforcesProblems.push({
        platform: 'codeforces',
        id: s.problemId,
        title: s.problemTitle,
        url: s.problemUrl,
        language: s.language,
        solvedAt: s.timestamp,
        _ts: s._ts,
        rating: s.rating || null,
        tags: s.tags || [],
        difficulty: null
      });
      for (const tag of (s.tags || [])) {
        tagCounts.set(tag, (tagCounts.get(tag) || 0) + 1);
      }
    }
  }

  const allProblems = [...problems, ...codeforcesProblems].sort((a, b) => b._ts - a._ts);

  console.log(`Total unique problems: ${allProblems.length} (leetcode: ${problems.length}, codeforces: ${codeforcesProblems.length})`);
  console.log(`Unique tags: ${tagCounts.size}`);

  // 3. Generate tags.json
  const allTags = Array.from(tagCounts.entries())
    .map(([tag, count]) => ({ tag, count }))
    .sort((a, b) => b.count - a.count);

  const leetcodeTagCounts = new Map();
  const codeforcesTagCounts = new Map();
  for (const p of allProblems) {
    for (const tag of (p.tags || [])) {
      if (p.platform === 'leetcode') {
        leetcodeTagCounts.set(tag, (leetcodeTagCounts.get(tag) || 0) + 1);
      } else {
        codeforcesTagCounts.set(tag, (codeforcesTagCounts.get(tag) || 0) + 1);
      }
    }
  }

  const tagsJson = {
    updatedAt: new Date().toISOString(),
    totalUniqueProblems: allProblems.length,
    leetcodeCount: problems.length,
    codeforcesCount: codeforcesProblems.length,
    difficultyCounts,
    allTags,
    leetcodeTags: Array.from(leetcodeTagCounts.entries()).map(([tag, count]) => ({ tag, count })).sort((a, b) => b.count - a.count),
    codeforcesTags: Array.from(codeforcesTagCounts.entries()).map(([tag, count]) => ({ tag, count })).sort((a, b) => b.count - a.count),
  };

  // 4. Write outputs
  if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });

  fs.writeFileSync(path.join(DATA_DIR, 'archive.json'), JSON.stringify(allProblems, null, 2) + '\n');
  console.log(`Wrote data/archive.json (${allProblems.length} problems)`);

  const withoutTs = allProblems.map(({ _ts, ...rest }) => rest);
  fs.writeFileSync(path.join(DATA_DIR, 'problems.json'), JSON.stringify(withoutTs, null, 2) + '\n');
  console.log(`Wrote data/problems.json`);

  fs.writeFileSync(path.join(DATA_DIR, 'tags.json'), JSON.stringify(tagsJson, null, 2) + '\n');
  console.log(`Wrote data/tags.json (${allTags.length} tags)`);

  // stats.json
  const stats = {
    updatedAt: new Date().toISOString(),
    leetcode: {
      uniqueSolved: problems.length,
      totalSubmissions: problems.length
    },
    codeforces: {
      uniqueSolved: codeforcesProblems.length,
      totalSubmissions: codeforcesProblems.length
    },
    total: {
      uniqueSolved: allProblems.length,
      submissions: allProblems.length
    },
    tags: allTags.slice(0, 20),
    difficulties: difficultyCounts
  };
  fs.writeFileSync(path.join(DATA_DIR, 'stats.json'), JSON.stringify(stats, null, 2) + '\n');
  console.log('Wrote data/stats.json');

  console.log('Done!');
}

main();

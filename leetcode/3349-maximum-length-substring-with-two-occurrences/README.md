# 3090. Maximum Length Substring With Two Occurrences (Easy)

**Slug:** `maximum-length-substring-with-two-occurrences`
**ID:** 3090
**Difficulty:** Easy
**Tags:** Hash Table, String, Sliding Window
**Companies:** Meta, Amazon, Bloomberg, Morgan Stanley, Google, Walmart Labs
**Language:** Python3
**Runtime:** 3 ms (71.8%)
**Memory:** 19.3 MB (19.9%)
**Submitted:** 2026-08-14
**Link:** https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

## Description

Given a string <code>s</code>, return the <strong>maximum</strong> length of a <span data-keyword="substring">substring</span>&nbsp;such that it contains <em>at most two occurrences</em> of each character.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;bcbbbcba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>
The following substring has a length of 4 and contains at most two occurrences of each character: <code>&quot;bcbb<u>bcba</u>&quot;</code>.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>
The following substring has a length of 2 and contains at most two occurrences of each character: <code>&quot;<u>aa</u>aa&quot;</code>.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


## Hints
1. We can try all substrings by brute-force since the constraints are very small.
## Solution

See `solution.py` in this folder.

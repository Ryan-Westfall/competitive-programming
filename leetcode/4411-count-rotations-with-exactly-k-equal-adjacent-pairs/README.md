# 4043. Count Rotations With Exactly K Equal Adjacent Pairs (Easy)

**Slug:** `count-rotations-with-exactly-k-equal-adjacent-pairs`
**ID:** 4043
**Difficulty:** Easy
**Tags:** N/A
**Language:** Python3
**Runtime:** 63 ms (57.4%)
**Memory:** 19.3 MB (69.6%)
**Submitted:** 2026-09-11
**Link:** https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/

## Description

<p>You are given a string <code>s</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>A <strong>cyclic rotation</strong> of <code>s</code> is obtained by choosing a <span data-keyword="string-prefix">prefix</span> of <code>s</code> whose length is between 0 and <code>n - 1</code> (inclusive), and moving it to the end of the string while preserving the order of all characters.</p>

<p>For <strong>every</strong> cyclic rotation of <code>s</code>, let its <strong>score</strong> be the number of indices <code>i</code> such that <code>0 &lt;= i &lt; n - 1</code> and the characters at positions <code>i</code> and <code>i + 1</code> are equal.</p>

<p>Return the number of cyclic rotations of <code>s</code> whose score equals <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aab&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The cyclic rotations of <code>s</code> are:</p>

<ul>
	<li><code>&quot;aab&quot;</code>: The characters at positions 0 and 1 are equal, so <code>score = 1</code>.</li>
	<li><code>&quot;aba&quot;</code>: No two adjacent characters are equal, so <code>score = 0</code>.</li>
	<li><code>&quot;baa&quot;</code>: The characters at positions 1 and 2 are equal, so <code>score = 1</code>.</li>
</ul>

<p>Since <code>score</code> equals <code>k</code> for 2 cyclic rotations of <code>s</code>, the answer is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abca&quot;, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The cyclic rotations of <code>s</code> are:</p>

<ul>
	<li><code>&quot;abca&quot;</code>: No two adjacent characters are equal, so <code>score = 0</code>.</li>
	<li><code>&quot;bcaa&quot;</code>: The characters at positions 2 and 3 are equal, so <code>score = 1</code>.</li>
	<li><code>&quot;caab&quot;</code>: The characters at positions 1 and 2 are equal, so <code>score = 1</code>.</li>
	<li><code>&quot;aabc&quot;</code>: The characters at positions 0 and 1 are equal, so <code>score = 1</code>.</li>
</ul>

<p>Since <code>score</code> equals <code>k</code> for only 1 cyclic rotation of <code>s</code>, the answer is 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == s.length &lt;= 100</code></li>
	<li><code>s</code> only consists of lowercase English letters.</li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
</ul>


## Hints
1. <strong>1a (Simulation).</strong> Construct the rotation for each possible prefix length and count its equal adjacent pairs.
2. <strong>2a (Counting).</strong> Let <code>total</code> be the number of equal adjacent pairs when the string is treated as circular, including the pair formed by its last and first characters.
3. <strong>2b (Counting).</strong> Each rotation excludes exactly one circular adjacent pair. Its score is <code>total - 1</code> if the excluded pair has equal characters, and <code>total</code> otherwise.
## Solution

See `solution.py` in this folder.

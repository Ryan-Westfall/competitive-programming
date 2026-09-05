# 4026. Maximum Gap Between Stations (Medium)

**Slug:** `maximum-gap-between-stations`
**ID:** 4026
**Difficulty:** Medium
**Tags:** Two Pointers, String, Greedy
**Companies:** Amazon
**Language:** Python3
**Runtime:** 586 ms (40.1%)
**Memory:** 28 MB (21.6%)
**Submitted:** 2026-08-16
**Link:** https://leetcode.com/problems/maximum-gap-between-stations/

## Description

<p>You are given two strings <code>skill</code> and <code>station</code> of lengths <code>n</code> and <code>m</code>, respectively.</p>

<p><code>skill[i]</code> represents the skill of worker <code>i</code>, and <code>station[j]</code> represents the skill supported by station <code>j</code>.</p>

<p>You must assign <strong>every</strong> worker to a <strong>distinct</strong> station. Let <code>j<sub>i</sub></code> be the index of the station assigned to worker <code>i</code>. A valid assignment must satisfy:</p>

<ul>
	<li><code>station[j<sub>i</sub>] == skill[i]</code> for every <code>0 &lt;= i &lt; n</code>.</li>
	<li>The assigned station indices must be <strong>strictly</strong> increasing in worker order, meaning <code>j<sub>0</sub> &lt; j<sub>1</sub> &lt; ... &lt; j<sub>n - 1</sub></code>.</li>
</ul>

<p>The <strong>gap</strong> of an assignment is the <strong>maximum difference</strong> between the station indices assigned to two <strong>consecutive</strong> workers. In other words, it is <code>max(j<sub>i</sub> - j<sub>i - 1</sub>)</code> over all <code>1 &lt;= i &lt; n</code>.</p>

<p>If there is only one worker, the gap is 0.</p>

<p>Return the <strong>maximum</strong> possible gap among all valid assignments. It is guaranteed that <strong>at least</strong> one valid assignment exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">skill = &quot;aa&quot;, station = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The two workers must be assigned to two different <code>&#39;a&#39;</code> stations.</li>
	<li>Assigning them to stations <code>[0, 3]</code> gives a gap of 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">skill = &quot;xyz&quot;, station = &quot;xyzz&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Assign worker 0 to station <code>j = 0</code>, and worker 1 to station <code>j = 1</code>.</li>
	<li>To maximize the gap, assign worker 2 to station <code>j = 3</code>.</li>
	<li>This gives the assignment <code>[0, 1, 3]</code> with gaps <code>[1, 2]</code>, so the gap is 2.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">skill = &quot;cbc&quot;, station = &quot;cbcdbc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Assign worker 0 to station <code>j = 0</code>, and worker 1 to station <code>j = 1</code>.</li>
	<li>To maximize the gap, assign worker 2 to station <code>j = 5</code>.</li>
	<li>This gives the assignment <code>[0, 1, 5]</code> with gaps <code>[1, 4]</code>, so the gap is 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>skill.length == n</code></li>
	<li><code>station.length == m</code></li>
	<li><code>1 &lt;= n &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>skill</code> and <code>station</code> consist of lowercase English letters.</li>
	<li>It is guaranteed that a valid assignment exists for every worker.</li>
</ul>


## Hints
1. <p>For each adjacent pair of workers <code>i - 1</code> and <code>i</code>, try to maximize the distance between their assigned stations while still allowing all earlier and later workers to be matched.</p>
2. <p>Compute the earliest possible station index for every worker by greedily matching <code>skill</code> from left to right.</p>
3. <p>Compute the latest possible station index for every worker by greedily matching <code>skill</code> from right to left.</p>
4. <p>For each <code>1 &lt;= i &lt; n</code>, workers before <code>i</code> can use their earliest possible positions and workers from <code>i</code> onward can use their latest possible positions. The largest possible gap between workers <code>i - 1</code> and <code>i</code> is <code>latest[i] - earliest[i - 1]</code>.</p>
## Solution

See `solution.py` in this folder.

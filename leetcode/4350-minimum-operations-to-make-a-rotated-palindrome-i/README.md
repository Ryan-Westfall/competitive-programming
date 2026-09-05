# 4021. Minimum Operations to Make a Rotated Palindrome I (Medium)

**Slug:** `minimum-operations-to-make-a-rotated-palindrome-i`
**ID:** 4021
**Difficulty:** Medium
**Tags:** Math, String, Enumeration
**Language:** Python3
**Runtime:** 9431 ms (17.4%)
**Memory:** 19.3 MB (42.9%)
**Submitted:** 2026-08-15
**Link:** https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/

## Description

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>You can perform the following operations any number of times (including zero) and in any order:</p>

<ul>
	<li><strong>Increment</strong>: Choose any index <code>i</code> and replace <code>s[i]</code> with the next lowercase English letter. The letter after <code>&#39;z&#39;</code> is <code>&#39;a&#39;</code>.</li>
	<li><strong>Left rotate</strong>: Move the first character of the string to the end.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations required to make <code>s</code> a <span data-keyword="palindrome-string">palindrome</span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>
One optimal solution:

<ul>
	<li>Left rotate the string: <code>&quot;abc&quot; -&gt; &quot;bca&quot;</code>.</li>
	<li>Increment <code>&#39;a&#39;</code> to <code>&#39;b&#39;</code>: <code>&quot;bca&quot; -&gt; &quot;bcb&quot;</code>.</li>
	<li><code>&quot;bcb&quot;</code> is a palindrome. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;yb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Increment the first character three times: <code>&quot;yb&quot; -&gt; &quot;zb&quot; -&gt; &quot;ab&quot; -&gt; &quot;bb&quot;</code>.</li>
	<li><code>&quot;bb&quot;</code> is a palindrome. Thus, the answer is 3.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


## Hints
1. <p>It is enough to consider performing <code>r</code> left rotations, where <code>0 &lt;= r &lt; s.length</code>. The increment operations can then be considered independently for each mirrored pair.</p>
2. <p>For two letters <code>a</code> and <code>b</code>, the minimum number of increments needed to make them equal is <code>min(abs(a - b), 26 - abs(a - b))</code>.</p>
3. <p>Try every rotation. For each one, sum this cost over all mirrored pairs and add the number of rotations. This gives an <code>O(n^2)</code> solution.</p>
## Solution

See `solution.py` in this folder.

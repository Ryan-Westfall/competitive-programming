# 4022. K-th Digit in Infinite String (Medium)

**Slug:** `k-th-digit-in-infinite-string`
**ID:** 4022
**Difficulty:** Medium
**Tags:** Math, Binary Search
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.5 MB (11.5%)
**Submitted:** 2026-08-15
**Link:** https://leetcode.com/problems/k-th-digit-in-infinite-string/

## Description

<p>You are given an integer <code>k</code>.</p>

<p>An <strong>infinite</strong> string is formed by <strong>concatenating</strong> the <strong>decimal</strong> representations of the <strong>positive</strong> integers, without separators.</p>

<p>For every nonnegative integer <code>b</code>, block <code>b</code> contains the <strong>positive</strong> integers from <code>10 * b</code> through <code>10 * b + 9</code>. The integers in each block are appended as follows:</p>

<ul>
	<li>If <code>b</code> is even, append the integers in <strong>increasing</strong> order.</li>
	<li>If <code>b</code> is odd, append the integers in <strong>decreasing</strong> order.</li>
</ul>

<p>Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.</p>

<p>Return the <code>k<sup>th</sup></code> digit (1-indexed) of this string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The string begins as <code>&quot;123<u>4</u>56789..&quot;</code>. The 4<sup>th</sup> digit is <code>&#39;4&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 15</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The string begins as <code>&quot;12345678919181<u>7</u>..&quot;</code>. The 15<sup>th</sup> digit is <code>&#39;7&#39;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 11</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>The string begins as <code>&quot;1234567891<u>9</u>..&quot;</code>. The 11<sup>th</sup> digit is <code>&#39;9&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
</ul>


## Hints
1. <p>The order inside a block does not affect its total number of digits. After finishing block <code>b</code>, the string has used exactly the same number of digits as writing all integers from 1 through <code>10 * b + 9</code> in the usual order.</p>
2. <p>Write a function that computes the total number of decimal digits needed to write all integers from 1 through <code>x</code>. Compute it by grouping numbers according to their digit length.</p>
3. <p>Binary search for the first block <code>b</code> whose cumulative number of digits is at least <code>k</code>. Then subtract the number of digits before that block to obtain the 1-indexed position inside the block.</p>
4. <p>For <code>b &gt; 0</code>, all 10 integers in the block have the same number of digits. Use the position inside the block to determine which integer and which digit it refers to. If <code>b</code> is odd, remember that the integers appear in decreasing order.</p>
## Solution

See `solution.py` in this folder.

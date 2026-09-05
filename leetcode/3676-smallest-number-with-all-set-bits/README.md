# 3370. Smallest Number With All Set Bits (Easy)

**Slug:** `smallest-number-with-all-set-bits`
**ID:** 3370
**Difficulty:** Easy
**Tags:** Math, Bit Manipulation
**Companies:** Microsoft, Google
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.4 MB (100.0%)
**Submitted:** 2024-12-01
**Link:** https://leetcode.com/problems/smallest-number-with-all-set-bits/

## Description

<p>You are given a <em>positive</em> number <code>n</code>.</p>

<p>Return the <strong>smallest</strong> number <code>x</code> <strong>greater than</strong> or <strong>equal to</strong> <code>n</code>, such that the binary representation of <code>x</code> contains only <span data-keyword="set-bit">set bits</span></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 7 is <code>&quot;111&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 15 is <code>&quot;1111&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 3 is <code>&quot;11&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## Hints
1. Find the strictly greater power of 2, and subtract 1 from it.
## Solution

See `solution.py` in this folder.

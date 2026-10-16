# 4078. Three Fibonacci Sum (Easy)

**Slug:** `three-fibonacci-sum`
**ID:** 4078
**Difficulty:** Easy
**Tags:** N/A
**Language:** Python3
**Runtime:** 1 ms (41.3%)
**Memory:** 19.3 MB (20.3%)
**Submitted:** 2026-10-16
**Link:** https://leetcode.com/problems/three-fibonacci-sum/

## Description

<p>You are given an integer <code>n</code>.</p>

<p>The <strong>Fibonacci sequence</strong> starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. Its first few terms are <code>0, 1, 1, 2, 3, 5, 8, 13, ...</code>.</p>

<p>Return <code>true</code> if <code>n</code> can be expressed as the sum of <strong>three consecutive terms</strong> in the Fibonacci sequence, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 16</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The three consecutive terms 3, 5, and 8 have a sum of <code>3 + 5 + 8 = 16</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>Although <code>1 + 2 + 5 = 8</code>, these terms are not consecutive in the Fibonacci sequence. No three consecutive terms have a sum of 8.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The first three terms have a sum of <code>0 + 1 + 1 = 2</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints
1. <strong>1a (Sequence Generation)</strong>: Generate consecutive Fibonacci triples and compare their sums with <code>n</code>. Stop when the sum exceeds <code>n</code>.
2. <strong>2a (Fibonacci Identity)</strong>: For consecutive Fibonacci terms <code>a</code>, <code>b</code>, and <code>c</code>, we have <code>a + b == c</code>, so their sum is <code>2 * c</code>.
3. <strong>2b (Fibonacci Identity)</strong>: Thus, <code>n</code> must be even and <code>n / 2</code> must be a positive Fibonacci number.
4. <strong>2c (Fibonacci Identity)</strong>: A positive integer <code>x</code> is Fibonacci exactly when <code>5 * x * x + 4</code> or <code>5 * x * x - 4</code> is a perfect square.
## Solution

See `solution.py` in this folder.

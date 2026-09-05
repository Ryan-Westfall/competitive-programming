# 1291. Sequential Digits (Medium)

**Slug:** `sequential-digits`
**ID:** 1291
**Difficulty:** Medium
**Tags:** Enumeration
**Companies:** Amazon, Bloomberg, Google, F5
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.2 MB (64.3%)
**Submitted:** 2026-07-13
**Link:** https://leetcode.com/problems/sequential-digits/

## Description

<p>An&nbsp;integer has <em>sequential digits</em> if and only if each digit in the number is one more than the previous digit.</p>

<p>Return a <strong>sorted</strong> list of all the integers&nbsp;in the range <code>[low, high]</code>&nbsp;inclusive that have sequential digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> low = 100, high = 300
<strong>Output:</strong> [123,234]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> low = 1000, high = 13000
<strong>Output:</strong> [1234,2345,3456,4567,5678,6789,12345]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>


## Hints
1. Generate all numbers with sequential digits and check if they are in the given range.
2. Fix the starting digit then do a recursion that tries to append all valid digits.
## Solution

See `solution.py` in this folder.

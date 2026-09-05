# 3702. Longest Subsequence With Non-Zero Bitwise XOR (Medium)

**Slug:** `longest-subsequence-with-non-zero-bitwise-xor`
**ID:** 3702
**Difficulty:** Medium
**Tags:** Array, Bit Manipulation
**Companies:** Google
**Language:** Python3
**Runtime:** 35 ms (46.7%)
**Memory:** 33.1 MB (58.4%)
**Submitted:** 2026-08-15
**Link:** https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

## Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Return the length of the <strong>longest <span data-keyword="subsequence-array-nonempty">subsequence</span></strong> in <code>nums</code> whose bitwise <strong>XOR</strong> is <strong>non-zero</strong>. If no such <strong>subsequence</strong> exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One longest subsequence is <code>[2, 3]</code>. The bitwise XOR is computed as <code>2 XOR 3 = 1</code>, which is non-zero.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest subsequence is <code>[2, 3, 4]</code>. The bitwise XOR is computed as <code>2 XOR 3 XOR 4 = 5</code>, which is non-zero.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints
1. What happens if you take the entire array?
2. If the XOR of the entire array is 0, can removing one element help?
3. What if all elements are 0?
## Solution

See `solution.py` in this folder.

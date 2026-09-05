# 3173. Bitwise OR of Adjacent Elements (Easy)

**Slug:** `bitwise-or-of-adjacent-elements`
**ID:** 3173
**Difficulty:** Easy
**Tags:** Array, Bit Manipulation
**Companies:** Adobe
**Language:** Python3
**Runtime:** 3 ms (57.1%)
**Memory:** 17.6 MB (100.0%)
**Submitted:** 2024-12-31
**Link:** https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

## Description

<p>Given an array <code>nums</code> of length <code>n</code>, return an array <code>answer</code> of length <code>n - 1</code> such that <code>answer[i] = nums[i] | nums[i + 1]</code> where <code>|</code> is the bitwise <code>OR</code> operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,7,15]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,7,15]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [8,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[12,6]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,9,11]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,13,11]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 100</code></li>
</ul>


## Hints
1. Iterate over array and calculate each element of the resulting array using <code>|</code> operation.
## Solution

See `solution.py` in this folder.

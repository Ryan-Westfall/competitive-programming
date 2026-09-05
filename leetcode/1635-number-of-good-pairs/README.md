# 1512. Number of Good Pairs (Easy)

**Slug:** `number-of-good-pairs`
**ID:** 1512
**Difficulty:** Easy
**Tags:** Array, Hash Table, Math, Counting
**Companies:** Amazon, Google, Bloomberg, Microsoft, Zoho
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.7 MB (100.0%)
**Submitted:** 2025-01-14
**Link:** https://leetcode.com/problems/number-of-good-pairs/

## Description

<p>Given an array of integers <code>nums</code>, return <em>the number of <strong>good pairs</strong></em>.</p>

<p>A pair <code>(i, j)</code> is called <em>good</em> if <code>nums[i] == nums[j]</code> and <code>i</code> &lt; <code>j</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,1,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Each pair in the array are <em>good</em>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints
1. Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
## Solution

See `solution.py` in this folder.

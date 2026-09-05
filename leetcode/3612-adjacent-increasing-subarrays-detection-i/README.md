# 3349. Adjacent Increasing Subarrays Detection I (Easy)

**Slug:** `adjacent-increasing-subarrays-detection-i`
**ID:** 3349
**Difficulty:** Easy
**Tags:** Array
**Companies:** Google, Bloomberg, Amazon
**Language:** Python3
**Runtime:** 87 ms (57.7%)
**Memory:** 16.6 MB (100.0%)
**Submitted:** 2024-11-10
**Link:** https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

## Description

<p>Given an array <code>nums</code> of <code>n</code> integers and an integer <code>k</code>, determine whether there exist <strong>two</strong> <strong>adjacent</strong> <span data-keyword="subarray-nonempty">subarrays</span> of length <code>k</code> such that both subarrays are <strong>strictly</strong> <strong>increasing</strong>. Specifically, check if there are <strong>two</strong> subarrays starting at indices <code>a</code> and <code>b</code> (<code>a &lt; b</code>), where:</p>

<ul>
	<li>Both subarrays <code>nums[a..a + k - 1]</code> and <code>nums[b..b + k - 1]</code> are <strong>strictly increasing</strong>.</li>
	<li>The subarrays must be <strong>adjacent</strong>, meaning <code>b = a + k</code>.</li>
</ul>

<p>Return <code>true</code> if it is <em>possible</em> to find <strong>two </strong>such subarrays, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,5,7,8,9,2,3,4,3,1], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The subarray starting at index <code>2</code> is <code>[7, 8, 9]</code>, which is strictly increasing.</li>
	<li>The subarray starting at index <code>5</code> is <code>[2, 3, 4]</code>, which is also strictly increasing.</li>
	<li>These two subarrays are adjacent, so the result is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,4,4,4,5,6,7], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt; 2 * k &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints
1. Store the longest increasing subarray starting and ending at an index.
## Solution

See `solution.py` in this folder.

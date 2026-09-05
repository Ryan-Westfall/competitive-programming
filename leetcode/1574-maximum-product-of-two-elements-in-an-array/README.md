# 1464. Maximum Product of Two Elements in an Array (Easy)

**Slug:** `maximum-product-of-two-elements-in-an-array`
**ID:** 1464
**Difficulty:** Easy
**Tags:** Array, Sorting, Heap (Priority Queue)
**Companies:** Google, Amazon, Meta, Bloomberg, Samsung
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.3 MB (23.2%)
**Submitted:** 2026-07-27
**Link:** https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

## Description

<p>You are given an array of integers <code>nums</code>.</p>

<p>Choose two <strong>different</strong> indices <code>i</code> and <code>j</code> of that array.</p>

<p>Return the <strong>maximum</strong> value of <code>(nums[i] - 1) * (nums[j] - 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,2]
<strong>Output:</strong> 12 
<strong>Explanation:</strong> If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,4,5]
<strong>Output:</strong> 16
<strong>Explanation:</strong> Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,7]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>


## Hints
1. Use brute force: two loops to select i and j, then select the maximum value of (nums[i]-1)*(nums[j]-1).
## Solution

See `solution.py` in this folder.

# 912. Sort an Array (Medium)

**Slug:** `sort-an-array`
**ID:** 912
**Difficulty:** Medium
**Tags:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
**Companies:** Google, Microsoft, Amazon, Meta, Bloomberg, JPMorgan Chase, Oracle
**Language:** Python3
**Runtime:** 807 ms (18.1%)
**Memory:** 26.3 MB (91.3%)
**Submitted:** 2026-06-30
**Link:** https://leetcode.com/problems/sort-an-array/

## Description

<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>

<p>You must solve the problem <strong>without using any built-in</strong> functions in <code>O(nlog(n))</code> time complexity and with the smallest space complexity possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
<strong>Explanation:</strong> After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
<strong>Explanation:</strong> Note that the values of nums are not necessarily unique.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>


## Solution

See `solution.py` in this folder.

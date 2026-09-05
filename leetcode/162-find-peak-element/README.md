# 162. Find Peak Element (Medium)

**Slug:** `find-peak-element`
**ID:** 162
**Difficulty:** Medium
**Tags:** Array, Binary Search
**Companies:** Google, Amazon, Meta, Microsoft, Bloomberg, Uber, Infosys, tcs, IXL, Apple, Netflix, TikTok, Goldman Sachs, Yahoo, eBay, Samsung, ByteDance, Docusign, Oracle, Visa, Wix, Akamai, Waymo, Urban Company
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.9 MB (100.0%)
**Submitted:** 2025-02-25
**Link:** https://leetcode.com/problems/find-peak-element/

## Description

<p>A peak element is an element that is strictly greater than its neighbors.</p>

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, find a peak element, and return its index. If the array contains multiple peaks, return the index to <strong>any of the peaks</strong>.</p>

<p>You may imagine that <code>nums[-1] = nums[n] = -&infin;</code>. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.</p>

<p>You must write an algorithm that runs in <code>O(log n)</code> time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 is a peak element and your function should return the index number 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,3,5,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>nums[i] != nums[i + 1]</code> for all valid <code>i</code>.</li>
</ul>


## Solution

See `solution.py` in this folder.

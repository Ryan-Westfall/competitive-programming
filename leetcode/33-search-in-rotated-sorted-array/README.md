# 33. Search in Rotated Sorted Array (Medium)

**Slug:** `search-in-rotated-sorted-array`
**ID:** 33
**Difficulty:** Medium
**Tags:** Array, Binary Search
**Companies:** Amazon, Google, Microsoft, Bloomberg, Meta, Goldman Sachs, LinkedIn, Yandex, tcs, TikTok, Oracle, Grammarly, Expedia, Uber, Nvidia, PayPal, Infosys, Anduril, Palo Alto Networks, FreshWorks, Apple, Walmart Labs, Autodesk, Flipkart, Salesforce, Arista Networks, ByteDance, Criteo, F5, Snap, Samsung, eBay, Adobe, IBM, Cisco, Visa, Nutanix, Paytm, Zoho, MongoDB, Josh Technology
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.5 MB (39.2%)
**Submitted:** 2026-08-30
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Description

<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values).</p>

<p>Prior to being passed to your function, <code>nums</code> is <strong>possibly left rotated</strong> at an unknown index <code>k</code> (<code>1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,5,6,7]</code> might be left rotated by&nbsp;<code>3</code>&nbsp;indices and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the possible rotation and an integer <code>target</code>, return <em>the index of </em><code>target</code><em> if it is in </em><code>nums</code><em>, or </em><code>-1</code><em> if it is not in </em><code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is an ascending array that is possibly rotated.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

See `solution.py` in this folder.

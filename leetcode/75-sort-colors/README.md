# 75. Sort Colors (Medium)

**Slug:** `sort-colors`
**ID:** 75
**Difficulty:** Medium
**Tags:** Array, Two Pointers, Sorting, Quicksort, Bubble Sort
**Companies:** Amazon, Google, Bloomberg, Microsoft, tcs, Meta, Walmart Labs, Agoda, Oracle, Nvidia, Apple, Samsung, Visa, TikTok, eBay, Morgan Stanley, Flipkart, Salesforce, Cisco, IBM, ServiceNow, Swiggy, Snowflake, Target, Autodesk, Capgemini, Slice, Pocket Gems
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.9 MB (100.0%)
**Submitted:** 2025-01-03
**Link:** https://leetcode.com/problems/sort-colors/

## Description

<p>You are given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library&#39;s sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,2,1,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,1,1,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either 0, 1, or 2.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>


## Hints
1. A rather straight forward solution is a two-pass algorithm using counting sort.
2. Iterate the array counting number of 0's, 1's, and 2's.
3. Overwrite array with the total number of 0's, then 1's and followed by 2's.
## Solution

See `solution.py` in this folder.

# 283. Move Zeroes (Easy)

**Slug:** `move-zeroes`
**ID:** 283
**Difficulty:** Easy
**Tags:** Array, Two Pointers
**Companies:** Google, Amazon, Meta, Bloomberg, Microsoft, tcs, EPAM Systems, Infosys, Cognizant, Apple, Walmart Labs, Chewy, Yandex, Uber, Qualcomm, Accenture, LTIMindtree, TikTok, Capgemini, SAP, Cisco, Oracle, ServiceNow, Goldman Sachs, Josh Technology, NetApp, PayPal, Samsung, JTG, Anduril, ADP, Wix
**Language:** Python3
**Runtime:** 232 ms (8.5%)
**Memory:** 15.1 MB (100.0%)
**Submitted:** 2020-09-09
**Link:** https://leetcode.com/problems/move-zeroes/

## Description

<p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

## Hints
1. <b>In-place</b> means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
2. A <b>two-pointer</b> approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.
## Solution

See `solution.py` in this folder.

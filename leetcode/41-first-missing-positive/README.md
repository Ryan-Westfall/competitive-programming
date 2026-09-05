# 41. First Missing Positive (Hard)

**Slug:** `first-missing-positive`
**ID:** 41
**Difficulty:** Hard
**Tags:** Array, Hash Table
**Companies:** Amazon, tcs, Google, Meta, Bloomberg, Microsoft, Zoho, Oracle, Netflix, Myntra, Cognizant, Walmart Labs, Tesla, Salesforce, Nutanix, Goldman Sachs, ServiceNow, MakeMyTrip, Nvidia, General Motors, Zomato, Swiggy
**Language:** Python3
**Runtime:** 77 ms (5.4%)
**Memory:** 30.9 MB (61.4%)
**Submitted:** 2026-06-20
**Link:** https://leetcode.com/problems/first-missing-positive/

## Description

<p>Given an unsorted integer array <code>nums</code>. Return the <em>smallest positive integer</em> that is <em>not present</em> in <code>nums</code>.</p>

<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Hints
1. Think about how you would solve the problem in non-constant space.  Can you apply that logic to the existing space?
2. We don't care about duplicates or non-positive integers
3. Remember that O(2n) = O(n)
## Solution

See `solution.py` in this folder.

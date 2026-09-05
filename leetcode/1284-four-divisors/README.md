# 1390. Four Divisors (Medium)

**Slug:** `four-divisors`
**ID:** 1390
**Difficulty:** Medium
**Tags:** Array, Math, Prime Factorization, Sieve Theory
**Companies:** Bloomberg, Microsoft, Capital One
**Language:** Python3
**Runtime:** 357 ms (40.0%)
**Memory:** 20.4 MB (65.2%)
**Submitted:** 2026-08-27
**Link:** https://leetcode.com/problems/four-divisors/

## Description

<p>Given an integer array <code>nums</code>, return <em>the sum of divisors of the integers in that array that have exactly four divisors</em>. If there is no such integer in the array, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,4,7]
<strong>Output:</strong> 32
<strong>Explanation:</strong> 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,21]
<strong>Output:</strong> 64
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints
1. Find the divisors of each element in the array.
2. You only need to loop to the square root of a number to find its divisors.
## Solution

See `solution.py` in this folder.

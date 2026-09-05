# 204. Count Primes (Medium)

**Slug:** `count-primes`
**ID:** 204
**Difficulty:** Medium
**Tags:** Array, Math, Enumeration, Number Theory, Primality Test, Sieve Theory, Prime Number Sieve
**Companies:** Google, Amazon, Microsoft, tcs, Meta, Uber, Bloomberg, Apple, Goldman Sachs, Intel, SAP, Epic Systems
**Language:** Python3
**Runtime:** 9827 ms (5.0%)
**Memory:** 86.3 MB (23.6%)
**Submitted:** 2026-08-27
**Link:** https://leetcode.com/problems/count-primes/

## Description

<p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>


## Hints
1. Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
2. Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
3. Use Sieve of Eratosthenes.
## Solution

See `solution.py` in this folder.

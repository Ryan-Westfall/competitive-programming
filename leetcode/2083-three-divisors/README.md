# 1952. Three Divisors (Easy)

**Slug:** `three-divisors`
**ID:** 1952
**Difficulty:** Easy
**Tags:** Math, Enumeration, Number Theory, Prime Factorization, Sieve Theory
**Companies:** Google, Microsoft
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.3 MB (49.1%)
**Submitted:** 2026-08-25
**Link:** https://leetcode.com/problems/three-divisors/

## Description

<p>Given an integer <code>n</code>, return <code>true</code><em> if </em><code>n</code><em> has <strong>exactly three positive divisors</strong>. Otherwise, return </em><code>false</code>.</p>

<p>An integer <code>m</code> is a <strong>divisor</strong> of <code>n</code> if there exists an integer <code>k</code> such that <code>n = k * m</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
<strong>Explantion:</strong> 2 has only two divisors: 1 and 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> true
<strong>Explantion:</strong> 4 has three divisors: 1, 2, and 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints
1. You can count the number of divisors and just check that they are 3
2. Beware of the case of n equal 1 as some solutions might fail in it
## Solution

See `solution.py` in this folder.

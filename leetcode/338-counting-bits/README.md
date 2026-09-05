# 338. Counting Bits (Easy)

**Slug:** `counting-bits`
**ID:** 338
**Difficulty:** Easy
**Tags:** Dynamic Programming, Bit Manipulation
**Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Apple, Oracle
**Language:** Python3
**Runtime:** 142 ms (5.0%)
**Memory:** 21 MB (6.6%)
**Submitted:** 2022-01-13
**Link:** https://leetcode.com/problems/counting-bits/

## Description

<p>Given an integer <code>n</code>, return <em>an array </em><code>ans</code><em> of length </em><code>n + 1</code><em> such that for each </em><code>i</code><em> </em>(<code>0 &lt;= i &lt;= n</code>)<em>, </em><code>ans[i]</code><em> is the <strong>number of </strong></em><code>1</code><em><strong>&#39;s</strong> in the binary representation of </em><code>i</code>.</p>
Do not solve it with built-in functions (i.e., like <code>__builtin_popcount</code> in C++).
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1,1]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [0,1,1,2,1,2]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>It is very easy to come up with a solution with a runtime of <code>O(n log n)</code>. Can you do it in linear time <code>O(n)</code> and possibly in a single pass?</li>
</ul>


## Hints
1. You should make use of what you have produced already.
2. Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
3. Or does the odd/even status of the number help you in calculating the number of 1s?
## Solution

See `solution.py` in this folder.

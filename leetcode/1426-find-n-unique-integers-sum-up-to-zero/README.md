# 1304. Find N Unique Integers Sum up to Zero (Easy)

**Slug:** `find-n-unique-integers-sum-up-to-zero`
**ID:** 1304
**Difficulty:** Easy
**Tags:** Array, Math
**Companies:** Google, Amazon, American Express, Meta, Microsoft
**Language:** Python3
**Runtime:** 54 ms (0.1%)
**Memory:** 14.3 MB (100.0%)
**Submitted:** 2021-10-21
**Link:** https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

## Description

<p>Given an integer <code>n</code>, return <strong>any</strong> array containing <code>n</code> <strong>unique</strong> integers such that they add up to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [-7,-1,1,3,4]
<strong>Explanation:</strong> These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [-1,0,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## Hints
1. Return an array where the values are symmetric. (+x , -x).
2. If n is odd, append value 0 in your returned array.
## Solution

See `solution.py` in this folder.

# 1151. Minimum Swaps to Group All 1's Together (Medium)

**Slug:** `minimum-swaps-to-group-all-1s-together`
**ID:** 1151
**Difficulty:** Medium
**Tags:** Array, Sliding Window
**Companies:** Amazon, TikTok, Expedia
**Language:** Python3
**Runtime:** 77 ms (20.4%)
**Memory:** 21.9 MB (100.0%)
**Submitted:** 2025-01-20
**Link:** https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

## Description

<p>Given a&nbsp;binary array <code>data</code>, return&nbsp;the minimum number of swaps required to group all <code>1</code>&rsquo;s present in the array together in <strong>any place</strong> in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> data = [1,0,1,0,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are 3 ways to group all 1&#39;s together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> data = [0,0,0,1,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there is only one 1 in the array, no swaps are needed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> data = [1,0,1,0,1,0,0,1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= data.length &lt;= 10<sup>5</sup></code></li>
	<li><code>data[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints
1. How many 1's should be grouped together ? Is not a fixed number?
2. Yeah it's just the number of 1's the whole array has. Let's name this number as ones
3. Every subarray of size of ones, needs some number of swaps to reach, Can you find the number of swaps needed to group all 1's in this subarray?
4. It's the number of zeros in that subarray.
5. Do you need to count the number of zeros all over again for every position ?
6. Use Sliding Window technique.
## Solution

See `solution.py` in this folder.

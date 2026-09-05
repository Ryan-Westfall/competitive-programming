# 1338. Reduce Array Size to The Half (Medium)

**Slug:** `reduce-array-size-to-the-half`
**ID:** 1338
**Difficulty:** Medium
**Tags:** Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)
**Companies:** Akuna Capital
**Language:** Python3
**Runtime:** 624 ms (5.1%)
**Memory:** 30.9 MB (99.6%)
**Submitted:** 2021-07-08
**Link:** https://leetcode.com/problems/reduce-array-size-to-the-half/

## Description

<p>You are given an integer array <code>arr</code>. You can choose a set of integers and remove all the occurrences of these integers in the array.</p>

<p>Return <em>the minimum size of the set so that <strong>at least</strong> half of the integers of the array are removed</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,3,3,3,5,5,5,2,2,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible set you can choose is {7}. This will make the new array empty.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>arr.length</code> is even.</li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints
1. Count the frequency of each integer in the array.
2. Start with an empty set, add to the set the integer with the maximum frequency.
3. Keep Adding the integer with the max frequency until you remove at least half of the integers.
## Solution

See `solution.py` in this folder.

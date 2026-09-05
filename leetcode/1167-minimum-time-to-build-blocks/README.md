# 1199. Minimum Time to Build Blocks (Hard)

**Slug:** `minimum-time-to-build-blocks`
**ID:** 1199
**Difficulty:** Hard
**Tags:** Array, Math, Greedy, Heap (Priority Queue)
**Companies:** Google
**Language:** Python3
**Runtime:** 4795 ms (20.4%)
**Memory:** 117.2 MB (26.5%)
**Submitted:** 2026-08-02
**Link:** https://leetcode.com/problems/minimum-time-to-build-blocks/

## Description

<p>You are given a list of blocks, where <code>blocks[i] = t</code> means that the&nbsp;<code>i</code>-th block needs&nbsp;<code>t</code>&nbsp;units of time to be built. A block can only be built by exactly one worker.</p>

<p>A worker can either split into two workers (number of workers increases by one) or build a block then go home. Both decisions cost some time.</p>

<p>The time cost of spliting one worker into two workers is&nbsp;given as an integer <code>split</code>. Note that if two workers split at the same time, they split in parallel so the cost would be&nbsp;<code>split</code>.</p>

<p>Output the minimum time needed to build all blocks.</p>

<p>Initially, there is only <strong>one</strong> worker.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> blocks = [1], split = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong>We use 1 worker to build 1 block in 1 time unit.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> blocks = [1,2], split = 5
<strong>Output:</strong> 7
<strong>Explanation: </strong>We split the worker into 2 workers in 5 time units then assign each of them to a block so the cost is 5 + max(1, 2) = 7.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> blocks = [1,2,3], split = 1
<strong>Output:</strong> 4
<strong>Explanation: </strong>Split 1 worker into 2, then assign the first worker to the last block and split the second worker into 2.
Then, use the two unassigned workers to build the first two blocks.
The cost is 1 + max(3, 1 + max(1, 2)) = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= blocks.length &lt;= 1000</code></li>
	<li><code>1 &lt;= blocks[i] &lt;= 10^5</code></li>
	<li><code>1 &lt;= split &lt;= 100</code></li>
</ul>


## Hints
1. A greedy approach will not work as the examples show.
2. Try all possible moves using DP.
3. For the DP state, dp[i][j] is the minimum time cost to build the first i blocks using j workers.
4. In one step you can either assign a worker to a block or choose a number of workers to split.
5. If you choose to assign a worker to a block it is always better to assign him to the block with the maximum time so we sort the array before using DP.
6. To optimize the solution from O(n^3) to O(n^2) notice that if you choose to split, it is always better to split all the workers you have.
## Solution

See `solution.py` in this folder.

# 4034. Minimum Bishop Moves to Reach Target (Medium)

**Slug:** `minimum-bishop-moves-to-reach-target`
**ID:** 4034
**Difficulty:** Medium
**Tags:** N/A
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.5 MB (8.8%)
**Submitted:** 2026-08-29
**Link:** https://leetcode.com/problems/minimum-bishop-moves-to-reach-target/

## Description

<p>There is an <code>8 x 8</code> empty chessboard with <strong>1-indexed</strong> rows and columns.</p>

<p>You are given an array <code>source = [sr, sc]</code> representing the starting position of a <strong>bishop</strong>, and an array <code>target = [tr, tc]</code> representing the target position.</p>

<p>In one move, the bishop travels one or more squares along a single <strong>diagonal</strong> direction, staying within the board.</p>

<p>Return the <strong>minimum</strong> number of moves for the bishop to land <strong>exactly</strong> on <code>target</code>. If it can never reach <code>target</code>, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = [8,1], target = [1,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><strong>​​​​​​​<img alt="" src="https://assets.leetcode.com/uploads/2026/08/31/111.png" style="width: 300px; height: 303px;" />​​​​​​​</strong></p>

<p>A single diagonal move takes the bishop straight from <code>(8, 1)</code> to <code>(1, 8)</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = [4,2], target = [1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2026/08/31/22-ezgifcom-invert-colors.png" style="width: 300px; height: 305px;" /></p>

<p>The bishop moves from <code>(4, 2)</code> to <code>(3, 1)</code>, then from <code>(3, 1)</code> to <code>(1, 3)</code>, reaching the target in 2 moves.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = [1,1], target = [3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>No matter how many diagonal moves it makes, the bishop starting at <code>(1, 1)</code> can never land on <code>(3, 4)</code>. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong>​​​​​​​</p>

<ul>
	<li><code>source.length == target.length == 2</code></li>
	<li><code>1 &lt;= sr, sc, tr, tc &lt;= 8</code></li>
	<li><code>source != target</code></li>
</ul>


## Hints
1. First consider the cases where no move is needed or where the target is unreachable. A bishop always remains on squares of the same color.
2. Two squares are on the same diagonal if either <code>r - c</code> or <code>r + c</code> is equal for both squares. If the target is reachable but not on the same diagonal, determine how many moves are sufficient.
## Solution

See `solution.py` in this folder.

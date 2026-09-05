# 4016. Maximum Area of Two Non-Overlapping Square Submatrices (Medium)

**Slug:** `maximum-area-of-two-non-overlapping-square-submatrices`
**ID:** 4016
**Difficulty:** Medium
**Tags:** Array, Binary Search, Dynamic Programming, Matrix
**Companies:** American Express
**Language:** Python3
**Runtime:** 325 ms (83.2%)
**Memory:** 50.5 MB (9.0%)
**Submitted:** 2026-08-10
**Link:** https://leetcode.com/problems/maximum-area-of-two-non-overlapping-square-submatrices/

## Description

<p>You are given a 2D integer matrix <code>mat</code> of size <code>m &times; n</code>, where:</p>

<ul>
	<li><code>mat[r][c] == 1</code> means the cell at row <code>r</code> and column <code>c</code> is usable.</li>
	<li><code>mat[r][c] == 0</code> means it is not usable.</li>
</ul>

<p>Your task is to find <strong>two <span data-keyword="submatrix">submatrices</span></strong> that satisfy the following conditions:</p>

<ul>
	<li>Both submatrices must be squares of the same side length <code>k</code>.</li>
	<li>The two submatrices must not share any cell.</li>
	<li>Each submatrix can only cover cells where <code>mat[r][c] == 1</code>.</li>
</ul>

<p>Return the <strong>maximum possible area</strong> of each of the two squares. If it is not possible to choose two such squares, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/06/13/image.png" style="width: 291px; height: 140px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The largest equal non-overlapping squares have side length <code>k = 2</code> with area 4.</p>

<ul>
	<li>First square starts at top-left <code>(0, 0)</code> and covers cells <code>(0, 0)</code>, <code>(0, 1)</code>, <code>(1, 0)</code>, and <code>(1, 1)</code>.</li>
	<li>Second square starts at top-left <code>(1, 2)</code> and covers cells <code>(1, 2)</code>, <code>(1, 3)</code>, <code>(2, 2)</code>, and <code>(2, 3)</code>.</li>
</ul>

<p>Thus, the answer is 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/06/13/screenshot-2026-06-13-at-83728pm.png" style="width: 155px; height: 130px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[0,1],[1,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The largest equal non-overlapping squares have side length <code>k = 1</code> with area 1.</p>

<ul>
	<li>First square starts at top-left <code>(0, 1)</code> and covers cell <code>(0, 1)</code>.</li>
	<li>Second square starts at top-left <code>(1, 0)</code> and covers cell <code>(1, 0)</code>.</li>
</ul>

<p>Thus, the answer is 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/06/13/screenshot-2026-06-13-at-83751pm.png" style="width: 152px; height: 125px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[0,0],[0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one usable cell, so it is impossible to choose two non-overlapping squares. Thus, the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>mat.length == m</code></li>
	<li><code>mat[i].length == n</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>mat[i][j]</code> is either 0 or 1.</li>
</ul>


## Hints
1. Binary search for the maximum side length <code>k</code>. If two valid squares of side length <code>k</code> exist, two valid squares of every smaller side length also exist.
2. Build a 2D prefix sum so that you can determine in constant time whether every cell in a given square is usable.
3. For a fixed <code>k</code>, record the minimum and maximum row and column among the top-left corners of all valid squares. Two of them can be disjoint if the difference between the maximum and minimum row is at least <code>k</code>, or the corresponding column difference is at least <code>k</code>.
## Solution

See `solution.py` in this folder.

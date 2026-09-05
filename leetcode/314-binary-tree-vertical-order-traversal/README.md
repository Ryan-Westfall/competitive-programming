# 314. Binary Tree Vertical Order Traversal (Medium)

**Slug:** `binary-tree-vertical-order-traversal`
**ID:** 314
**Difficulty:** Medium
**Tags:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree
**Companies:** Meta, Bloomberg, Apple, Amazon, Microsoft, Google, DoorDash, Snap
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.9 MB (100.0%)
**Submitted:** 2025-02-06
**Link:** https://leetcode.com/problems/binary-tree-vertical-order-traversal/

## Description

<p>Given the <code>root</code> of a binary tree, return <em><strong>the vertical order traversal</strong> of its nodes&#39; values</em>. (i.e., from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <strong>left to right</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/23/image1.png" style="width: 400px; height: 273px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/23/image3.png" style="width: 450px; height: 285px;" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7]
<strong>Output:</strong> [[4],[9],[3,0,1],[8],[7]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/09/23/image2.png" style="width: 350px; height: 342px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
<strong>Output:</strong> [[4],[2,5],[1,10,9,6],[3],[11]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


## Hints
1. Do BFS from the root. Let the root be at column 0. In the BFS, keep in the queue the node and its column.
2. When you traverse a node, store its value in the column index. For example, the root's value should be stored at index 0.
3. If the node has a left node, it column should be col - 1. Similarly, if the node has a right node, its column should be col + 1.
4. At the end, check the minimum and maximum col and output their values.
## Solution

See `solution.py` in this folder.

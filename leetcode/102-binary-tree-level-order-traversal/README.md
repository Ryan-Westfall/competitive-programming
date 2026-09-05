# 102. Binary Tree Level Order Traversal (Medium)

**Slug:** `binary-tree-level-order-traversal`
**ID:** 102
**Difficulty:** Medium
**Tags:** Tree, Breadth-First Search, Binary Tree
**Companies:** Google, Amazon, Bloomberg, Microsoft, Meta, Oracle, Palo Alto Networks, Yandex, LinkedIn, Apple, Adobe, Visa, Goldman Sachs
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 17.6 MB (100.0%)
**Submitted:** 2024-11-01
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/

## Description

<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


## Hints
1. Use a queue to perform BFS.
## Solution

See `solution.py` in this folder.

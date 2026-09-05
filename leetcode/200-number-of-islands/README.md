# 200. Number of Islands (Medium)

**Slug:** `number-of-islands`
**ID:** 200
**Difficulty:** Medium
**Tags:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
**Companies:** Amazon, Google, Bloomberg, Anduril, Microsoft, TikTok, Meta, Apple, Uber, Walmart Labs, Infosys, LinkedIn, Goldman Sachs, ByteDance, Waymo, Oracle, Visa, Qualcomm, tcs, Snap, CrowdStrike, Yandex, Capital One, Tesla, Nvidia, Siemens, Pinterest, Expedia, Salesforce, ServiceNow, Hive, Autodesk, Zoho, PayPal, eBay, Samsung, Citadel, Tinkoff, SAP, IBM, Huawei, Docusign, Wix, BitGo, Cloudflare, Rivian, Wells Fargo, DoorDash, Adobe, Nutanix, Cisco, Redfin, Accenture, Squarepoint Capital, Grammarly, SoFi, AMD, Zomato, HashedIn, Comcast, Barclays, Zenefits
**Language:** Python3
**Runtime:** 244 ms (55.8%)
**Memory:** 20 MB (100.0%)
**Submitted:** 2025-01-18
**Link:** https://leetcode.com/problems/number-of-islands/

## Description

<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Solution

See `solution.py` in this folder.

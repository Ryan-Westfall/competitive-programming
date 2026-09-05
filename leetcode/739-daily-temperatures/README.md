# 739. Daily Temperatures (Medium)

**Slug:** `daily-temperatures`
**ID:** 739
**Difficulty:** Medium
**Tags:** Array, Stack, Monotonic Stack
**Companies:** Amazon, Google, Bloomberg, Meta, Goldman Sachs, Anduril, Chime, Microsoft, TikTok, Zoho, Agoda, Morgan Stanley, Oracle, Intuit, Walmart Labs, Josh Technology, Grab, ServiceNow, Accenture, Swiggy, Tekion
**Language:** Python3
**Runtime:** 79 ms (96.2%)
**Memory:** 28.8 MB (37.6%)
**Submitted:** 2026-01-17
**Link:** https://leetcode.com/problems/daily-temperatures/

## Description

<p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li>
</ul>


## Hints
1. If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100.  We could remember when all of them occur next.
## Solution

See `solution.py` in this folder.

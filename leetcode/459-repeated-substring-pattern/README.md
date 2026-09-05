# 459. Repeated Substring Pattern (Easy)

**Slug:** `repeated-substring-pattern`
**ID:** 459
**Difficulty:** Easy
**Tags:** String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm
**Companies:** Google, Amazon, Meta, Microsoft, Bloomberg, Myntra
**Language:** Python3
**Runtime:** 0 ms (100.0%)
**Memory:** 19.2 MB (91.1%)
**Submitted:** 2026-06-13
**Link:** https://leetcode.com/problems/repeated-substring-pattern/

## Description

<p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;ab&quot; twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcabcabc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;abc&quot; four times or the substring &quot;abcabc&quot; twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


## Solution

See `solution.py` in this folder.

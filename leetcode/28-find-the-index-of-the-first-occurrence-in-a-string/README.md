# 28. Find the Index of the First Occurrence in a String (Easy)

**Slug:** `find-the-index-of-the-first-occurrence-in-a-string`
**ID:** 28
**Difficulty:** Easy
**Tags:** Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm
**Companies:** Google, Amazon, Meta, Bloomberg, Microsoft, Cognizant, PayPal, Zoho, tcs, Apple, Expedia, Infosys, Pocket Gems
**Language:** Python3
**Runtime:** 3 ms (18.1%)
**Memory:** 19.3 MB (61.8%)
**Submitted:** 2026-01-19
**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Description

<p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>


## Solution

See `solution.py` in this folder.

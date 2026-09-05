# 1216. Valid Palindrome III (Hard)

**Slug:** `valid-palindrome-iii`
**ID:** 1216
**Difficulty:** Hard
**Tags:** String, Dynamic Programming
**Companies:** Meta, TikTok
**Language:** Python3
**Runtime:** 1505 ms (5.1%)
**Memory:** 258.1 MB (27.4%)
**Submitted:** 2024-12-18
**Link:** https://leetcode.com/problems/valid-palindrome-iii/

## Description

<p>Given a string <code>s</code> and an integer <code>k</code>, return <code>true</code> if <code>s</code> is a <code>k</code><strong>-palindrome</strong>.</p>

<p>A string is <code>k</code><strong>-palindrome</strong> if it can be transformed into a palindrome by removing at most <code>k</code> characters from it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcdeca&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Remove &#39;b&#39; and &#39;e&#39; characters.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbababa&quot;, k = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>


## Hints
1. Can you reduce this problem to a classic problem?
2. The problem is equivalent to finding any palindromic subsequence of length at least N-K where N is the length of the string.
3. Try to find the longest palindromic subsequence.
4. Use DP to do that.
## Solution

See `solution.py` in this folder.

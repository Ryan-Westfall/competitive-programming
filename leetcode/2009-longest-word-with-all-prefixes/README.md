# 1858. Longest Word With All Prefixes (Medium)

**Slug:** `longest-word-with-all-prefixes`
**ID:** 1858
**Difficulty:** Medium
**Tags:** Array, String, Depth-First Search, Trie
**Companies:** Google
**Language:** Python3
**Runtime:** 207 ms (37.7%)
**Memory:** 60.6 MB (37.7%)
**Submitted:** 2026-07-29
**Link:** https://leetcode.com/problems/longest-word-with-all-prefixes/

## Description

<p>Given an array of strings <code>words</code>, find the <strong>longest</strong> string in <code>words</code> such that <strong>every prefix</strong> of it is also in <code>words</code>.</p>

<ul>
	<li>For example, let <code>words = [&quot;a&quot;, &quot;app&quot;, &quot;ap&quot;]</code>. The string <code>&quot;app&quot;</code> has prefixes <code>&quot;ap&quot;</code> and <code>&quot;a&quot;</code>, all of which are in <code>words</code>.</li>
</ul>

<p>Return <em>the string described above. If there is more than one string with the same length, return the <strong>lexicographically smallest</strong> one, and if no string exists, return </em><code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;k&quot;,&quot;ki&quot;,&quot;kir&quot;,&quot;kira&quot;, &quot;kiran&quot;]
<strong>Output:</strong> &quot;kiran&quot;
<strong>Explanation:</strong> &quot;kiran&quot; has prefixes &quot;kira&quot;, &quot;kir&quot;, &quot;ki&quot;, and &quot;k&quot;, and all of them appear in words.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;, &quot;banana&quot;, &quot;app&quot;, &quot;appl&quot;, &quot;ap&quot;, &quot;apply&quot;, &quot;apple&quot;]
<strong>Output:</strong> &quot;apple&quot;
<strong>Explanation:</strong> Both &quot;apple&quot; and &quot;apply&quot; have all their prefixes in words.
However, &quot;apple&quot; is lexicographically smaller, so we return that.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abc&quot;, &quot;bc&quot;, &quot;ab&quot;, &quot;qwe&quot;]
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sum(words[i].length) &lt;= 10<sup>5</sup></code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>


## Hints
1. Add all the words to a trie.
2. Check the longest path where all the nodes are words.
## Solution

See `solution.py` in this folder.

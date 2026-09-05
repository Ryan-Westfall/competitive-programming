# 2168. Unique Substrings With Equal Digit Frequency (Medium)

**Slug:** `unique-substrings-with-equal-digit-frequency`
**ID:** 2168
**Difficulty:** Medium
**Tags:** Hash Table, String, Rolling Hash, Counting, Hash Function
**Companies:** Expedia
**Language:** Python3
**Runtime:** 934 ms (75.0%)
**Memory:** 19.5 MB (90.6%)
**Submitted:** 2026-07-22
**Link:** https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

## Description

Given a digit string <code>s</code>, return <em>the number of <strong>unique substrings </strong>of </em><code>s</code><em> where every digit appears the same number of times.</em>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1212&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substrings that meet the requirements are &quot;1&quot;, &quot;2&quot;, &quot;12&quot;, &quot;21&quot;, &quot;1212&quot;.
Note that although the substring &quot;12&quot; appears twice, it is only counted once.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;12321&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> The substrings that meet the requirements are &quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;12&quot;, &quot;23&quot;, &quot;32&quot;, &quot;21&quot;, &quot;123&quot;, &quot;321&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of digits.</li>
</ul>


## Hints
1. With the constraints, could we try every substring?
2. Yes, checking every substring has runtime O(n^2), which will pass.
3. How can we make sure we only count unique substrings?
4. Use a set to store previously counted substrings. Hashing a string s of length m takes O(m) time. Is there a fast way to compute the hash of s if we know the hash of s[0..m - 2]?
5. Use a rolling hash.
## Solution

See `solution.py` in this folder.

# 5. Longest Palindromic Substring (Medium)

**Slug:** `longest-palindromic-substring`
**ID:** 5
**Difficulty:** Medium
**Tags:** Two Pointers, String, Dynamic Programming, Manacher
**Companies:** Amazon, Google, Bloomberg, Microsoft, Meta, tcs, Infosys, Visa, Adobe, Apple, Goldman Sachs, Yandex, EPAM Systems, Tinkoff, Cognizant, TikTok, Oracle, Uber, IBM, eBay, Accenture, HSBC, athenahealth, Autodesk, ZS Associates, HashedIn, Nvidia, Cisco, Zoho, Walmart Labs, PhonePe, Deloitte, SAP, Salesforce, Softwire, LinkedIn, Huawei, JPMorgan Chase, BlackRock, Morgan Stanley, Grab, Shopee, Accolite, persistent systems, Palo Alto Networks, Citadel, MAQ Software, Wix
**Language:** Python3
**Runtime:** 3486 ms (17.5%)
**Memory:** 13.9 MB (100.0%)
**Submitted:** 2022-02-08
**Link:** https://leetcode.com/problems/longest-palindromic-substring/

## Description

<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>


## Hints
1. How can we reuse a previously computed palindrome to compute a larger palindrome?
2. If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
3. Complexity based hint:</br>
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.
## Solution

See `solution.py` in this folder.

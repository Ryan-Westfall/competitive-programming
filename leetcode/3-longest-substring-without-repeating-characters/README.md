# 3. Longest Substring Without Repeating Characters (Medium)

**Slug:** `longest-substring-without-repeating-characters`
**ID:** 3
**Difficulty:** Medium
**Tags:** Hash Table, String, Sliding Window
**Companies:** Google, Amazon, Bloomberg, Microsoft, Meta, Infosys, Spotify, tcs, Deloitte, Apple, Yandex, Cognizant, Visa, Goldman Sachs, LinkedIn, Netflix, Zoho, Nvidia, Accolite, Agoda, Wipro, IBM, TikTok, Oracle, Walmart Labs, AT&T, Salesforce, Morgan Stanley, HashedIn, PayPal, Cisco, Qualcomm, Docusign, JPMorgan Chase, athenahealth, Airtel, EPAM Systems, NetApp, Rakuten, DP world, Twilio, Turing, ServiceNow, Lyft, Adobe, Coupang, Paytm, Accenture, Capgemini, persistent systems, HCL, Palo Alto Networks, KPMG, Uber, SAP, Roblox, Intel, Tesla, Nutanix, Akamai, AMD, Netskope, Tekion, FreshWorks, Pornhub, Virtusa, Dell, MAQ Software, Comcast, Freecharge, Ozon, Yelp
**Language:** Python3
**Runtime:** 17 ms (71.6%)
**Memory:** 16.7 MB (100.0%)
**Submitted:** 2024-11-18
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Description

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3. Note that <code>&quot;bca&quot;</code> and <code>&quot;cab&quot;</code> are also correct answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>


## Hints
1. There are less than 100 unique characters. We can check all substrings with length at most 100 for example. This is a good enough approximation.
## Solution

See `solution.py` in this folder.

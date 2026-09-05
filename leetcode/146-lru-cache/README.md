# 146. LRU Cache (Medium)

**Slug:** `lru-cache`
**ID:** 146
**Difficulty:** Medium
**Tags:** Hash Table, Linked List, Design, Doubly-Linked List
**Companies:** Amazon, Apple, Google, Microsoft, TikTok, Bloomberg, Meta, Adobe, Nvidia, Goldman Sachs, Nutanix, MongoDB, Palo Alto Networks, Github, eBay, LinkedIn, Snap, Salesforce, Expedia, Visa, JPMorgan Chase, ByteDance, Docusign, Qualcomm, Infosys, NetApp, Oracle, Uber, ServiceNow, Samsung, Walmart Labs, SAP, Aurora, Okta, Optiver, Netflix, Cisco, PayPal, Intuit, Rubrik, Tesla, IBM, razorpay, BitGo, General Motors, Squarespace, Shopify, Snowflake, Squarepoint Capital, KLA, Verkada, spinny, PhonePe, Rippling, Verily, EPAM Systems, Confluent, Coupang, Citadel, Yandex, Rivian, Arista Networks, DoorDash, Shopee, Reddit, smartnews, SoFi, Roku, Autodesk, Twitch, Capital One, Sprinklr, ZScaler, Zoom, Booking.com, Nokia, Wells Fargo, Disney, Cloudflare, Nordstrom, ThousandEyes, Whatfix, Rakuten, tcs, Anduril, Palantir, Yahoo, X, Zenefits
**Language:** Python3
**Runtime:** 27 ms (85.4%)
**Memory:** 29.3 MB (84.9%)
**Submitted:** 2026-08-31
**Link:** https://leetcode.com/problems/lru-cache/

## Description

<p>Design a data structure that follows the constraints of a <strong><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a></strong>.</p>

<p>Implement the <code>LRUCache</code> class:</p>

<ul>
	<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with <strong>positive</strong> size <code>capacity</code>.</li>
	<li><code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, <strong>evict</strong> the least recently used key.</li>
</ul>

<p>The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>Explanation</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>


## Solution

See `solution.py` in this folder.

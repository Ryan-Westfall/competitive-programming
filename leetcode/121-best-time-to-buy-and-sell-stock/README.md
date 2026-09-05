# 121. Best Time to Buy and Sell Stock (Easy)

**Slug:** `best-time-to-buy-and-sell-stock`
**ID:** 121
**Difficulty:** Easy
**Tags:** Array, Dynamic Programming
**Companies:** Amazon, Google, Meta, Bloomberg, Microsoft, Apple, Infosys, Atlassian, IBM, Zoho, Goldman Sachs, Nvidia, Walmart Labs, Flipkart, tcs, Siemens, HCL, Tesla, Citadel, JPMorgan Chase, Agoda, Swiggy, SAP, Visa, Sigmoid, Zoox, BlackRock, Uber, TikTok, Tiger Analytics, Comcast, Mastercard, Squarepoint Capital, Robinhood, Morgan Stanley, Salesforce, PayPal, Millennium, Capital One, Accenture, Adobe, ByteDance, Deloitte, Akamai, Bank of America, EPAM Systems, American Express, Expedia, Cisco, Deutsche Bank, Yandex, Airtel, Societe Generale, Bolt, Capgemini, Garmin, Remitly, Citigroup, Toast, Myntra, Turing, Ozon, LG Electronics
**Language:** Python3
**Runtime:** 93 ms (5.1%)
**Memory:** 27 MB (100.0%)
**Submitted:** 2025-01-07
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Description

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

See `solution.py` in this folder.

# 4013. Count Subarrays With Even Odd Ratio II (Hard)

**Slug:** `count-subarrays-with-even-odd-ratio-ii`
**ID:** 4013
**Difficulty:** Hard
**Tags:** Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Prefix Sum
**Language:** Python3
**Runtime:** 262 ms (94.1%)
**Memory:** 28 MB (85.9%)
**Submitted:** 2026-08-14
**Link:** https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

## Description

<p>You are given an integer array <code>nums</code> and two integers <code>a</code> and <code>b</code>.</p>

<p>For a <span data-keyword="subarray-nonempty">subarray</span>, let:</p>

<ul>
	<li><code>x</code> be the number of even elements.</li>
	<li><code>y</code> be the number of odd elements.</li>
</ul>

<p>The ratio of even to odd elements in a subarray is defined as <code>x / y</code>, where ratios are compared by their exact rational values.</p>

<p>A subarray is considered <strong>valid</strong> if:</p>

<ul>
	<li><code>y &gt; 0</code>, and</li>
	<li><code>x / y &lt;= a / b</code>.</li>
</ul>

<p>Return the number of valid subarrays in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2], a = 3, b = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The following are the valid subarrays:</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Values</th>
			<th style="border: 1px solid black;">Even Count</th>
			<th style="border: 1px solid black;">Odd Count</th>
			<th style="border: 1px solid black;">Ratio</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[0..0]</code></td>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>0 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[0..1]</code></td>
			<td style="border: 1px solid black;"><code>[1, 2]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>1 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[0..2]</code></td>
			<td style="border: 1px solid black;"><code>[1, 2, 1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>1 / 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[0..3]</code></td>
			<td style="border: 1px solid black;"><code>[1, 2, 1, 2]</code></td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>2 / 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[1..2]</code></td>
			<td style="border: 1px solid black;"><code>[2, 1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>1 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[2..2]</code></td>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>0 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[2..3]</code></td>
			<td style="border: 1px solid black;"><code>[1, 2]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>1 / 1</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the number of valid subarrays is 7.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,1], a = 2, b = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The following are the valid subarrays:</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Values</th>
			<th style="border: 1px solid black;">Even Count</th>
			<th style="border: 1px solid black;">Odd Count</th>
			<th style="border: 1px solid black;">Ratio</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[0..2]</code></td>
			<td style="border: 1px solid black;"><code>[2, 2, 1]</code></td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>2 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[1..2]</code></td>
			<td style="border: 1px solid black;"><code>[2, 1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>1 / 1</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>nums[2..2]</code></td>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>0 / 1</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the number of valid subarrays is 3.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,2], a = 1, b = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Every subarray contains 0 odd numbers, so no subarray is valid.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= a, b &lt;= 10<sup>9</sup>​​​​​​​</code></li>
</ul>


## Hints
1. <p>Replace every even element with <code>b</code> and every odd element with <code>-a</code>. A subarray is valid exactly when its transformed sum is at most <code>0</code>.</p>
2. <p>The condition <code>y &gt; 0</code> is then automatic, because a non-empty subarray containing only even elements has a positive transformed sum.</p>
3. <p>Let <code>pref[i]</code> be the prefix sum of the transformed array. A subarray <code>[l, r]</code> is valid when <code>pref[r + 1] &lt;= pref[l]</code>.</p>
4. <p>Scan the prefix sums from left to right and count how many previous prefix sums are greater than or equal to the current one using coordinate compression and a Fenwick tree.</p>
## Solution

See `solution.py` in this folder.

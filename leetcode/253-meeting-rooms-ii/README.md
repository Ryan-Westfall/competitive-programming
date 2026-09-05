# 253. Meeting Rooms II (Medium)

**Slug:** `meeting-rooms-ii`
**ID:** 253
**Difficulty:** Medium
**Tags:** Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
**Companies:** Amazon, Google, Bloomberg, Microsoft, JPMorgan Chase, Snap, Salesforce, TikTok, Oracle, Apple, Meta, Uber, Atlassian, IBM, Lyft, Netflix, FreshWorks, Anduril, DE Shaw, Compass, Disney, Cisco, Citadel, Hubspot, WorldQuant, Walmart Labs, Nutanix, Goldman Sachs, Docusign, Aurora, Capital One, Two Sigma, Lime, Snowflake
**Language:** Python3
**Runtime:** 4 ms (45.2%)
**Memory:** 19.9 MB (100.0%)
**Submitted:** 2025-01-18
**Link:** https://leetcode.com/problems/meeting-rooms-ii/

## Description

<p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of conference rooms required</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints
1. Think about how we would approach this problem in a very simplistic way. We will allocate rooms to meetings that occur earlier in the day v/s the ones that occur later on, right?
2. If you've figured out that we have to <b>sort</b> the meetings by their start time, the next thing to think about is how do we do the allocation? <br>There are two scenarios possible here for any meeting. Either there is no meeting room available and a new one has to be allocated, or a meeting room has freed up and this meeting can take place there.
3. An important thing to note is that we don't really care <b>which</b> room gets freed up while allocating a room for the current meeting. As long as a room is free, our job is done. <br><br>We already know the rooms we have allocated till now and we also know when are they due to get free because of the end times of the meetings going on in those rooms. We can simply check the room which is due to get vacated the earliest amongst all the allocated rooms.
4. Following up on the previous hint, we can make use of a min-heap to store the end times of the meetings in various rooms. <br><br>So, every time we want to check if any room is free or not, simply check the topmost element of the min heap as that would be the room that would get free the earliest out of all the other rooms currently occupied.

<br><br>If the room we extracted from the top of the min heap isn't free, then no other room is. So, we can save time here and simply allocate a new room.
## Solution

See `solution.py` in this folder.

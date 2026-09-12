from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # [left, right, weight, original_index]
        sortedIntervals = sorted(
            [interval + [i] for i, interval in enumerate(intervals)],
            key=lambda x: x[0]
        )

        starts = [interval[0] for interval in sortedIntervals]

        # next[i] = first interval whose left endpoint > current right endpoint
        next = [0] * n

        for i in range(n):
            r = sortedIntervals[i][1]
            next[i] = bisect_right(starts, r)

        @cache
        def dp(i, k):
            if k == 0 or i == n:
                return (0, [])

            # Skip current interval
            skipScore, skipIndices = dp(i + 1, k)

            # Take current interval
            left, right, weight, index = sortedIntervals[i]

            takeScore, takeIndices = dp(next[i], k - 1)
            takeScore += weight
            takeIndices = sorted([index] + takeIndices)

            # Choose better score
            if takeScore > skipScore:
                return (takeScore, takeIndices)

            if skipScore > takeScore:
                return (skipScore, skipIndices)

            # Same score -> lexicographically smaller indices
            return (skipScore, min(skipIndices, takeIndices))

        return dp(0, 4)[1]
from functools import cache
from bisect import bisect_right

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        firstOccurenceIndex = {}
        lastOccurenceIndex = {}

        for i in range(n):
            if s[i] not in firstOccurenceIndex:
                firstOccurenceIndex[s[i]] = i
            lastOccurenceIndex[s[i]] = i

        subStringIndexes = []

        # Find all valid intervals
        for c in firstOccurenceIndex:
            start = firstOccurenceIndex[c]
            end = lastOccurenceIndex[c]

            k = start
            valid = True

            while k <= end:
                if firstOccurenceIndex[s[k]] < start:
                    valid = False
                    break

                end = max(end, lastOccurenceIndex[s[k]])
                k += 1

            if valid:
                subStringIndexes.append([start, end])

        subStringIndexes.sort()

        subStringN = len(subStringIndexes)

        @cache
        def dp(i):
            # (number of substrings, total length, actual substrings)
            if i >= subStringN:
                return (0, 0, [])

            # Don't take
            noTake = dp(i + 1)

            # Take
            start, end = subStringIndexes[i]

            nextI = bisect_right(
                subStringIndexes,
                end,
                key=lambda x: x[0]
            )

            nextCount, nextLength, nextSubstrings = dp(nextI)

            take = (
                nextCount + 1,
                nextLength + (end - start + 1),
                [s[start:end + 1]] + nextSubstrings
            )

            if take[0] > noTake[0]:
                return take

            if take[0] < noTake[0]:
                return noTake

            # Tie: minimize total length
            if take[1] < noTake[1]:
                return take

            return noTake

        return dp(0)[2]
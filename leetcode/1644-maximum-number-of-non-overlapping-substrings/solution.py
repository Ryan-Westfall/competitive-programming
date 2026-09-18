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

        for i in range(n):
            if firstOccurenceIndex[s[i]] != i:
                continue

            start = i
            end = lastOccurenceIndex[s[i]]

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

        subStringN = len(subStringIndexes)

        @cache
        def dp(i):
            if i >= subStringN:
                return (0, 0, [])

            noTake = dp(i + 1)

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

            if take[1] < noTake[1]:
                return take

            return noTake

        return dp(0)[2]
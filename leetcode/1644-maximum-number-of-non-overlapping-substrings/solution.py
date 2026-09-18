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
                continue  # only start a candidate at a char's first occurrence

            start, end = i, lastOccurenceIndex[s[i]]
            k = start
            valid = True
            while k <= end:
                if firstOccurenceIndex[s[k]] < start:
                    valid = False          # would have to extend left past start
                    break
                end = max(end, lastOccurenceIndex[s[k]])  # extend right, keep scanning
                k += 1

            if valid:
                subStringIndexes.append([start, end])

        subStringN = len(subStringIndexes)
        @cache
        def dp(i):
            if i >= subStringN:
                return []

            noTake = dp(i+1)
            start, end = subStringIndexes[i]
            nextI = bisect_right(subStringIndexes, end, key=lambda x: x[0])
            take = [s[start:end+1]]
            take.extend(dp(nextI))

            if len(noTake) > len(take):
                return noTake
            else:
                if len(noTake) == len(take):
                    return take if len("".join(take)) < len("".join(noTake)) else noTake
                return take

        return dp(0)


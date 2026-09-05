class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(int)

        maxSeen = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 2:
                counter[s[l]] -= 1
                l += 1
            maxSeen = max(r - l + 1, maxSeen)

        return maxSeen

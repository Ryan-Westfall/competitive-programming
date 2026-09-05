class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        result = 0
        maxOccurence = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            maxOccurence = max(maxOccurence, counter[s[r]])
            while ((r+1) - l) - maxOccurence > k:
                counter[s[l]] -= 1
                l += 1

            result = max(result, (r + 1) - l)

        return result

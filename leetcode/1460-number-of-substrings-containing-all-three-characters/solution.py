class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = defaultdict(int)
        l = 0
        substrings = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter['a'] and counter['b'] and counter['c']:
                substrings += (len(s) - r)
                counter[s[l]] -= 1
                l += 1

        return substrings
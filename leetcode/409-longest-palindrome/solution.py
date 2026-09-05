class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        total = 0

        for val in count.values():
            total += (val // 2) * 2

        if total < len(s):
            total += 1

        return total
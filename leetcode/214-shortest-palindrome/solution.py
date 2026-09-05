class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        lastIndex = 0
        base = 29
        power = 1
        mod = 10 ** 9 + 7

        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)

            prefix = (prefix * base)
            prefix = (prefix + char)
            suffix = (suffix + char * power)
            power = (power * base)

            if prefix == suffix:
                lastIndex = i 

        suffix = s[lastIndex + 1:]
        return suffix[::-1] + s
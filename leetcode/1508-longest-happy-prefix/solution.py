class Solution:
    def longestPrefix(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        longest = ""
        leftHash = 0
        rightHash = 0

        base = 29
        power = 1
        mod = 10 ** 9 + 7

        while l < len(s) - 1:
            charL = ord(s[l]) - ord('a') + 1
            leftHash = (leftHash * base) % mod
            leftHash = (leftHash + charL) % mod

            charR = ord(s[r]) - ord('a') + 1
            rightHash = (rightHash + charR * power) % mod
            power = (power * base) % mod

            if leftHash == rightHash:
                longest = s[:l+1]
            l += 1
            r -= 1

        return longest
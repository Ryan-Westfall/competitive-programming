class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for c in s:
            i = ord(c) - ord('a')

            new = total + 1

            total += new - dp[i]
            dp[i] = new

            total %= MOD

        return total
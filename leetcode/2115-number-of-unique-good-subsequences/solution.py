class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7

        dp0 = 0
        dp1 = 0
        has_zero = False

        for c in binary:
            if c == '0':
                has_zero = True
                dp0 = dp0 + dp1
            else:
                dp1 = dp0 + dp1 + 1

            dp0 %= MOD
            dp1 %= MOD

        return (dp0 + dp1 + has_zero) % MOD
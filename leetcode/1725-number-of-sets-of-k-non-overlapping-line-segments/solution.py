class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, curK):
            if curK == 0:
                return 1

            if i >= n and curK > 0:
                return 0

            # NoTake
            noTake = dp(i + 1, curK)

            # Take
            curTake = suffix(i + 1, curK - 1)

            return noTake + curTake

        @cache
        def suffix(i, curK):
            if i >= n:
                return 0

            return dp(i, curK) + suffix(i + 1, curK)

        return dp(0, k) % MOD
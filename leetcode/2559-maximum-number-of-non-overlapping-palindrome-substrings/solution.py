class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # Interval DP:
        # is_pal(l, r) = whether s[l:r+1] is a palindrome
        @lru_cache(maxsize=50000)
        def is_pal(l, r):
            if l >= r:
                return True

            if s[l] != s[r]:
                return False

            return is_pal(l + 1, r - 1)

        # Prefix DP:
        # dp[i] = max number of non-overlapping palindromes
        #         in s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't use a palindrome ending at i - 1
            dp[i] = dp[i - 1]

            # Try every substring ending at i - 1
            for l in range(i - k + 1):
                if is_pal(l, i - 1):
                    dp[i] = max(dp[i], dp[l] + 1)

        return dp[n]
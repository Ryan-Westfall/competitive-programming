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
        @cache
        def dp(i):
            if i >= n:
                return 0

            # Don't start a palindrome at i
            ans = dp(i + 1)

            # Try every palindrome starting at i
            for r in range(i + k - 1, n):
                if is_pal(i, r):
                    ans = max(ans, 1 + dp(r + 1))

            return ans

        return dp(0)
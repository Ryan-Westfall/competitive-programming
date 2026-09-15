class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(l, r):

            # empty
            if l > r:
                return 0

            # one character
            if l == r:
                return 1

            # matching ends
            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)

            # non-matching ends
            return max(
                dp(l + 1, r),
                dp(l, r - 1)
            )

        return dp(0, n - 1)
        
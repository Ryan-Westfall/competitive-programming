class Solution:
    def countSubstrings(self, s: str) -> int:

        @cache
        def isPalindrome(l,r):
            if l >= r:
                return True

            if s[l] != s[r]:
                return False

            return isPalindrome(l+1, r-1)
        
        @cache
        def dp(l,r):
            if l > r:
                return 0

            if l == r:
                return 1

            left = dp(l+1, r)
            right = dp(l, r-1)
            overlap = dp(l+1, r-1)

            return isPalindrome(l, r) + left + right - overlap


        return dp(0, len(s) - 1)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        iLen = len(text1)
        jLen = len(text2)

        @cache
        def dp(i,j):
            if i == iLen or j == jLen:
                return 0

            take = 0
            if text1[i] == text2[j]:
                take = dp(i+1, j+1) + 1
            
            return max(take, dp(i+1, j), dp(i, j+1))

        return dp(0,0)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        iLen = len(text1)
        jLen = len(text2)

        # @cache
        # def dp(i,j):
        #     if i == iLen or j == jLen:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return dp(i+1, j+1) + 1
            
        #     return max(dp(i+1, j), dp(i, j+1))

        # return dp(0,0)

        dp = [[0] * (jLen + 1) for _ in range(iLen + 1)]

        for i in range(1, iLen + 1):
            for j in range(1, jLen + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[iLen][jLen]
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

        dp = [[0] * (jLen) for _ in range(iLen)]
        for i in range(iLen):
            for j in range(jLen):
                if text1[i] == text2[j]:
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] += dp[i-1][j-1]
                    continue

                maxPrev = 0
                if i-1 >= 0:
                    maxPrev = max(maxPrev, dp[i-1][j])
                if j-1 >= 0:
                    maxPrev = max(maxPrev, dp[i][j-1])
                dp[i][j] = maxPrev

        return dp[iLen-1][jLen-1]
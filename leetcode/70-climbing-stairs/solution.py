class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def dp(x):
        #     if x == 1:
        #         return 1
        #     if x == 2:
        #         return 2


        #     return dp(x- 1) + dp(x-2)

        # return dp(n)


        dp = [0] * (n + 1)
        for i in range(1, n+1):
            if i == 1:
                dp[1] = 1
            elif i == 2:
                dp[2] = 2
            else:  
                dp[i] = dp[i-1] + dp[i-2]


        return dp[n]
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        # @cache
        # def dp(i):
        #     if i >= n:
        #         return 0


        #     noTake = dp(i+1)
        #     point, brainpower = questions[i]
        #     take = dp(i+brainpower+1) + point

        #     return max(take, noTake)

        # return dp(0)


        dp = [0] * (n + 1)

        for i in range(n):
            point, brainpower = questions[i]

            # Skip
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Take
            next_i = min(n, i + brainpower + 1)
            dp[next_i] = max(dp[next_i], dp[i] + point)

        return dp[n]
            


from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        # First number
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(1, n):
            for curSum, ways in dp[i - 1].items():
                dp[i][curSum + nums[i]] += ways
                dp[i][curSum - nums[i]] += ways

        return dp[n - 1][target]

        # @cache
        # def dp(i, curSum):
        #     if curSum == target and i == n:
        #         return 1

        #     if i == n:
        #         return 0

        #     cur = 0
        #     # plus
        #     cur +=  dp(i + 1, curSum + nums[i])
        #     # minus
        #     cur +=  dp(i + 1, curSum - nums[i])
        #     return cur

        # return dp(0,0)
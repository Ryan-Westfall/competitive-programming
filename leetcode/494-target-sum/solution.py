from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)

            for curSum, ways in dp.items():
                next_dp[curSum + num] += ways
                next_dp[curSum - num] += ways

            dp = next_dp

        return dp[target]

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
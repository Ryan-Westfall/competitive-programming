class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # # i, curTarget
        # dp = [[0] * (n +1) for _ in range(sum(nums))]
        # dp[1][nums[0]] = 1

        # for i in range(2, n+1):
        #     cur = dp[i-1]

        #     dp[i] = nums[i-1]


        # return dp[n][target]

        @cache
        def dp(i, curSum):
            if curSum == target and i == n:
                return 1

            if i == n:
                return 0

            cur = 0
            # plus
            cur +=  dp(i + 1, curSum + nums[i])
            # minus
            cur +=  dp(i + 1, curSum - nums[i])
            return cur

        return dp(1, -nums[0]) + dp(1, nums[0])
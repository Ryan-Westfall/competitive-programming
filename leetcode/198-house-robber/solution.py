class Solution:
    def rob(self, nums: list[int]) -> int:
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]

        # for i in range(1,n):
        #     # Take + 2
        #     dp[i] += max(dp[i-1], nums[i+1])
        #     # NoTake + 1
        #     dp[i]

        # return dp[n-1]

        @cache
        def dp(i):
            if i >= len(nums):
                return 0

            take = nums[i] + dp(i+2)
            noTake = dp(i+1)

            return max(take, noTake)
            

        return dp(0)
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        # dp = [[0] * total for _ in range(n)]
        # dp[0][nums[0]] = 1
        # dp[0][0] = 1

        # for i in range(1,n):
        #     cur = nums[i]
        #     for amount in range(total):

        #         # NoTake
        #         dp[i][amount] = dp[i-1][amount]

        #         # Take
        #         if 
        #         dp[i][curTotal] += dp[]


        # return len(dp[n-1][total//2])

        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        @cache
        def dp(i, cur):
            if cur > target:
                return False

            if i == n:
                return cur == target

            return (
                dp(i + 1, cur) or
                dp(i + 1, cur + nums[i])
            )

        return dp(0, 0)


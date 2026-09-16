class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n)]

        dp[0][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            cur = nums[i]

            for amount in range(target + 1):

                # NoTake
                dp[i][amount] = dp[i - 1][amount]

                # Take
                if amount >= cur:
                    dp[i][amount] = (
                        dp[i][amount] or
                        dp[i - 1][amount - cur]
                    )

        return dp[n - 1][target]

        # n = len(nums)
        # total = sum(nums)

        # if total % 2:
        #     return False

        # target = total // 2

        # @cache
        # def dp(i, cur):
        #     if cur > target:
        #         return False

        #     if i == n:
        #         return cur == target

        #     return (
        #         dp(i + 1, cur) or
        #         dp(i + 1, cur + nums[i])
        #     )

        # return dp(0, 0)


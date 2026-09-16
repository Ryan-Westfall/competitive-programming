class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for cur in nums:
            for amount in range(target, cur - 1, -1):
                dp[amount] |= dp[amount - cur]

        return dp[target]

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


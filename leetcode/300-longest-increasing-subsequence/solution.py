class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        # @cache
        # def dp(i):
        #     if i == n:
        #         return 0

        #     maxTake = 1
        #     for j in range(i+1, n):
        #         if nums[i] < nums[j]:
        #             maxTake = max(maxTake, dp(j) + 1)

        #     return maxTake

        # return max([dp(i) for i in range(n)])

        dp = [0] * n
        for i in range(n):
            maxTake = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    maxTake = max(maxTake, dp[j] + 1)

            dp[i] = maxTake

        return max(dp)

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            count = 0
            if nums[0] == target:
                count += 1
            if -nums[0] == target:
                count += 1
            return count

        total = sum(nums)

        if target < -total or target > total:
            return 0

        offset = total

        dp = [[0] * (2 * total + 1) for _ in range(n)]

        dp[0][offset + nums[0]] += 1
        dp[0][offset - nums[0]] += 1

        for i in range(1, n):
            for curSum in range(-total, total + 1):
                ways = dp[i - 1][offset + curSum]

                if ways:
                    dp[i][offset + curSum + nums[i]] += ways
                    dp[i][offset + curSum - nums[i]] += ways

        return dp[n - 1][offset + target]

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
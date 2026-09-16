class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        prev1 = 0
        prev2 = 0

        for i in range(n):
            take = nums[i] + prev2
            noTake = prev1

            prev2 = prev1
            prev1 = max(take, noTake)
            

        return prev1

        # @cache
        # def dp(i):
        #     if i >= len(nums):
        #         return 0

        #     take = nums[i] + dp(i+2)
        #     noTake = dp(i+1)

        #     return max(take, noTake)
            

        # return dp(0)
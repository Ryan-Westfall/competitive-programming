class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def dp(i):
            if i == n:
                return 0

            # j = first index past all copies of nums[i]
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1

            # k = first index past all copies of nums[i] + 1
            k = j
            while k < n and nums[k] == nums[i] + 1:
                k += 1

            noTake = dp(j)                      
            take = nums[i] * (j - i) + dp(k)   

            return max(noTake, take)

        return dp(0)
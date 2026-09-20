class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        maxArrEnding = nums[0]

        for i in range(1,len(nums)):
            maxArrEnding = max(maxArrEnding + nums[i], nums[i])
            result = max(result, maxArrEnding)

        return result
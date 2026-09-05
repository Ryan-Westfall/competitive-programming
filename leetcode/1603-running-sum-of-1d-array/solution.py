class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = 0
        for i in range(len(nums)):
            result += nums[i]
            nums[i] = result
        return nums
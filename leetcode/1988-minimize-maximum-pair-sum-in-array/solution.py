class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSeen = float('-inf')

        for i in range(len(nums)//2):
            maxSeen = max(maxSeen, nums[i] + nums[-i-1])

        return maxSeen
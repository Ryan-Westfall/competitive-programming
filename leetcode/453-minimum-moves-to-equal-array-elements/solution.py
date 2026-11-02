class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        for index in range(len(nums) - 1, 0, -1):
            count += nums[index] - nums[0]

        return count




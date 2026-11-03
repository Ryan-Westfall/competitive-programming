class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)

        total = 0
        for num in nums:
            total += mx - num
        return total
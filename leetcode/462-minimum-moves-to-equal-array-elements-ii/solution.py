class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median = int(statistics.median(nums))
        res = 0

        for num in nums:
            res += abs(median - num)

        return res

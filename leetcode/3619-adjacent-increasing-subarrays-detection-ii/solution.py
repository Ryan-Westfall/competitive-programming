class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        prev = 0
        cur = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur += 1
            else:
                ans = max(ans, cur // 2, min(prev, cur))
                prev = cur
                cur = 1

        return max(ans, cur // 2, min(prev, cur))
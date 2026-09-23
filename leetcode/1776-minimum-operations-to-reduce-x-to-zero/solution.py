class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        left = 0
        cur = 0
        longest = -1

        for right in range(len(nums)):
            cur += nums[right]

            while left <= right and cur > target:
                cur -= nums[left]
                left += 1

            if cur == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else len(nums) - longest
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        next_value = nums[0] - k
        distinct_count = 0

        for i in range(n):
            if nums[i] - k <= next_value <= nums[i] + k:
                distinct_count += 1
                next_value += 1
            elif nums[i] - k > next_value:
                distinct_count += 1
                next_value = nums[i] - k + 1

        return distinct_count
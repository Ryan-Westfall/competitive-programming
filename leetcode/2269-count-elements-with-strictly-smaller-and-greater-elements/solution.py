class Solution:
    def countElements(self, nums: List[int]) -> int:
        low = min(nums)
        high = max(nums)
        output = 0
        for i in nums:
            if i < high and i > low:
                output += 1
        return output
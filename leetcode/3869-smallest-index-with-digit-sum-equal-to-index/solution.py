class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum = 0
            for digit in str(nums[i]):
                sum += int(digit)

            if sum == i:
                return i

        return -1
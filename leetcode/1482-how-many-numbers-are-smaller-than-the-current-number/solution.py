class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        output = [0] * len(nums)

        # Build count
        for num in nums:
            count[num] += 1

        # Build prefix
        for i in range(1, len(count)):
            count[i] += count[i - 1]


        for i in range(len(nums)):
            v = nums[i]
            if v == 0:
                output[i] = 0
            else:
                output[i] = count[v - 1]

        return output
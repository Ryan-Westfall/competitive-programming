class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numberOfOnes = nums.count(1)
        maximumOnes = currentOnes = 0
        l = 0

        for r in range(len(nums) * 2):
            if nums[r % len(nums)]:
                currentOnes += 1
            if (r - l + 1) > numberOfOnes:
                currentOnes -= nums[l % len(nums)]
                l += 1

            maximumOnes = max(maximumOnes, currentOnes)


        return numberOfOnes - maximumOnes

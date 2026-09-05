class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:

        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                maximum = max(maximum, (nums[i] * nums[j]  / (math.gcd(nums[i], nums[j]) ** 2)) )

        return int(maximum)
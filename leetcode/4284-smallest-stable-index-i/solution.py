class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxPrefix = [0] * n
        maxPrefix[0] = nums[0]
        for i in range(1,n):
            maxPrefix[i] = max(maxPrefix[i-1], nums[i])

        minSuffix = [0] * n
        minSuffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            minSuffix[i] = min(minSuffix[i + 1], nums[i])

        for i in range(n):
            if maxPrefix[i] - minSuffix[i] <= k:
                return i

        return -1



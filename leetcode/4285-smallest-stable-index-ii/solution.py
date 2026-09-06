class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefixMin = [0] * n
        prefixMin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            prefixMin[i] = min(prefixMin[i+1], nums[i])
        
        postfixMax = [0] * n
        postfixMax[0] = nums[0]
        for i in range(n):
            if i > 0:
                postfixMax[i] = max(postfixMax[i-1], nums[i])
            if postfixMax[i] - prefixMin[i] <= k:
                return i

        return -1
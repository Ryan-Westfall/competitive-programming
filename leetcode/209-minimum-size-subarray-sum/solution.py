class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0

        minLen = float('inf')
        preSum = 0
        while r < len(nums):
            preSum += nums[r]
            if preSum < target:
                pass
            else:
                # print('r',r, preSum)
                while preSum >= target:
                    minLen = min(minLen, r - l + 1)
                    # print(l, preSum)
                    preSum -= nums[l]
                    l += 1

            r += 1

        return minLen if minLen != float('inf') else 0


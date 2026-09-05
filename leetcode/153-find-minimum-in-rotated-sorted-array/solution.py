class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minSeen = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minSeen = min(minSeen, nums[l])
                break
                
            k = (l + r) // 2
            minSeen = min(nums[k], minSeen)
            if nums[k] >= nums[l]:
                l = k + 1
            else:
                r = k - 1

        return minSeen
            
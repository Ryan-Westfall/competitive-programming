class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2


            if ((m == len(nums) - 1 or nums[m+1] < nums[m]) and (m == 0 or nums[m-1] < nums[m]) ):
                return m


            if nums[m+1] > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return m

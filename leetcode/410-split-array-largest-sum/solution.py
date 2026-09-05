class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def isValid(x):
            divisions = 1
            curSum = 0

            for num in nums:
                if curSum + num > x:
                    divisions += 1
                    curSum = num
                else:
                    curSum += num

            return divisions <= k

        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = l + (r - l) // 2

            if isValid(mid):
                r = mid
            else:
                l = mid + 1

        return l
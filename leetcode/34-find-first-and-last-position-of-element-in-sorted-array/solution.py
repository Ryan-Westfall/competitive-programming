class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower_bound(target):
            l, r = 0, len(nums)

            while l < r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid

            return l

        left = lower_bound(target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = lower_bound(target + 1) - 1

        return [left, right]
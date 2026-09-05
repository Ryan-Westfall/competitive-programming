class Solution:
    # 1 3 5 6
    # 1
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            # print(mid, l , r)

            if nums[mid] == target:
                return mid

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return l

            
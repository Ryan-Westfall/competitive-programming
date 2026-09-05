class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # mid and target are on the same side of rotation
            if (nums[mid] > nums[-1]) == (target > nums[-1]):
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            # Different sides of rotation
            elif target > nums[-1]:
                # target is on left side, mid is on right
                right = mid - 1
            else:
                # target is on right side, mid is on left
                left = mid + 1

        return -1
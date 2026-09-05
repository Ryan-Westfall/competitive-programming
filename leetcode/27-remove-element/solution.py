class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            while left <= right and nums[right] == val:
                right -= 1
            if left <= right and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return right + 1
                
class Solution:
    #    II i
    # 1,1,2,2,2,3
    # 
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
    
        insertIndex = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[insertIndex - 2]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        
        return insertIndex
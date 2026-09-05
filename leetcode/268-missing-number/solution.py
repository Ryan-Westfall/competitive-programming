class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

#         items = set(nums)
#         for i in range(len(items)):
#             if i not in items:
#                 return i
#         return len(items)
    
    
    
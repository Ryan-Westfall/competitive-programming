class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
        
#         memo = {}
        
#         def dfs(index, memo):
#             if index in memo:
#                 return memo[index]
#             if index > len(nums) - 1 and nums[index] == 0:
#                 memo[index] = False
#                 return False
#             if index == len(nums) - 1:
#                 return True

            
#             for i in range(1,nums[index] + 1):
#                 # print(index)
#                 result = dfs(index + i, memo)
#                 memo[index] = result
#                 # print(memo)
#                 if result:
#                     return True
        
#             memo[index] = False
#             return False
        
        
        # return dfs(0, memo)
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            print(i, nums[i])
            if i + nums[i] >= goal:
                goal = i
                
        return True if goal == 0 else False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def iterate(nums):
            
            #If nums is empty, we return
            if len(nums)==0:
                return
    
            mid = int(len(nums)/2)
            root = TreeNode(nums[mid])
            root.left = iterate(nums[:mid])
            root.right = iterate(nums[mid+1:])
            return root
        return iterate(nums)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Initialize global max with the smallest possible value

        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the max path sum from left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore negative paths
            right_max = max(dfs(node.right), 0)  # Ignore negative paths
            
            # Compute the local maximum path sum with the current node as the highest point
            local_max = left_max + right_max + node.val
            
            # Update the global maximum if the local maximum is greater
            self.max_sum = max(self.max_sum, local_max)
            
            # Return the maximum path sum including this node and one subtree
            return max(left_max, right_max) + node.val
        
        dfs(root)
        return self.max_sum


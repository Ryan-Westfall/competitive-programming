# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(node):
            if not node.left and not node.right:
                return 1

            left = 0
            if node.left:
                left = dfs(node.left)

            right = 0
            if node.right:
                right = dfs(node.right)
                
            self.longest = max(self.longest, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.longest
            
            
        
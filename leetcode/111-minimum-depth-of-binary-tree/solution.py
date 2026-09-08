# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        def dfs(node):
            if node.left and node.right:
                return 1+ min(dfs(node.left), dfs(node.right))
            elif node.left:
                return 1 + dfs(node.left)
            elif node.right:
                return 1 + dfs(node.right)
            else:
                return 1

        return dfs(root)
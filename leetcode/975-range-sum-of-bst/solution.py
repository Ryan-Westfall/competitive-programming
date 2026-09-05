# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total = 0
        
        def dfs(node):
            nonlocal total
            if not node:
                return

            if node.val >= low and node.val <= high:
                total += node.val

            if node.val < low:
                dfs(node.right)
                return

            if node.val > high:
                dfs(node.left)
                return


            dfs(node.right)
            dfs(node.left)

        dfs(root)

        return total


            

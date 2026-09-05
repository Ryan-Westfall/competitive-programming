# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        

        res = 0
        resDelta = float('inf')
        def dfs(node):
            nonlocal res, resDelta
            if not node:
                return
            if node.val >= target:
                dfs(node.left)
            elif node.val < target:
                dfs(node.right)

            delta = abs(node.val - target)
            if delta < resDelta:
                resDelta = delta
                res = node.val
            elif delta == resDelta:
                res = min(res, node.val)

        dfs(root)

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, maxValue):
            if not curr:
                return None
            maxValue = max(curr.val, maxValue)
            if (curr.val >= maxValue):
                self.good += 1
            dfs(curr.left, maxValue)
            dfs(curr.right, maxValue)

        dfs(root, root.val)

        return self.good
        
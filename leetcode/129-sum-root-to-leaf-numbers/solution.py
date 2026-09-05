# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        def dfs(node, curSum):
            if not node:
                return

            print(len(str(node.val)))

            curSum = curSum * (10 ** len(str(node.val))) + node.val

            if not node.left and not node.right:
                self.totalSum += curSum

            dfs(node.left, curSum)
            dfs(node.right, curSum)


        dfs(root, 0)

        return self.totalSum
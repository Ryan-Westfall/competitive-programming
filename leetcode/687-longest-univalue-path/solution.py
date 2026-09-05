# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.output = -1
        def dfs(node):
            if not node:
                return (-1,-1)
            if not node.left and not node.right:
                self.output = max(self.output, 1)
                return (node.val, 1)

            left = dfs(node.left)
            right = dfs(node.right)
            if left[0] == node.val and right[0] == node.val:
                self.output = max(self.output, 1 + left[1] + right[1])
                return (node.val, 1 + max(left[1], right[1]))
            elif left[0] == node.val:
                self.output = max(self.output, 1 + left[1])
                return (node.val, 1 + left[1])
            elif right[0] == node.val:
                self.output = max(self.output, 1 + right[1])
                return (node.val, 1 + right[1])
            else:
                self.output = max(self.output, 1)
                return (node.val, 1)

        dfs(root)
        return self.output - 1 if self.output != -1 else 0
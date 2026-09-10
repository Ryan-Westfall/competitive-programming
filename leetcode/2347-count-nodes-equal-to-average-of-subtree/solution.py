# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0

        output = 0
        
        def dfs(node):
            nonlocal output

            if not node.left and not node.right:
                output += 1
                return (node.val, 1)

            nodeSum = node.val
            nodeN = 1
            if node.left:
                leftVal, leftN = dfs(node.left)
                nodeSum += leftVal
                nodeN += leftN

            if node.right:
                rightVal, rightN = dfs(node.right)
                nodeSum += rightVal
                nodeN += rightN

            if nodeSum // nodeN == node.val:
                output += 1

            return (nodeSum, nodeN)

        dfs(root)

        return output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        accepted = []
        def goDown(node, sumValue, visited):
            if not node:
                return
            sumValue += node.val
            visited.append(node.val)
            
            if not node.right and not node.left and sumValue == targetSum:
                accepted.append(visited)
                return
            
            goDown(node.left,sumValue, visited.copy())
            goDown(node.right,sumValue, visited.copy())
            
            
            
        goDown(root, 0, [])
        return accepted
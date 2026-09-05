# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(pCurr, qCurr):
            if not pCurr and not qCurr:
                return True
            elif not pCurr or not qCurr:
                return False
            
            left = dfs(pCurr.left, qCurr.left)
            right = dfs(pCurr.right, qCurr.right)

            return pCurr.val == qCurr.val and left and right

        return dfs(p, q)
        
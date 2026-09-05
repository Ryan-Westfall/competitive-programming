# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(r,s):
            if not r and not s:
                return True
            elif not r or not s or r.val != s.val:
                return False
            return sameTree(r.left,s.left) and sameTree(r.right,s.right)

        def dfs(curr):
            if not curr:
                return False

            return dfs(curr.left) or dfs(curr.right) or sameTree(curr, subRoot)

        return dfs(root)
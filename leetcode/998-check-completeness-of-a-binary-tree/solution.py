# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])



        while q:
            curr = q.popleft()
            if curr == None:
                while q and curr == None:
                    curr = q.popleft()
                if curr == None:
                    return True
                else:
                    return False
            q.append(curr.left)
            q.append(curr.right)
        




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return isMirror(root.left, root.right)
    
def isMirror(leftTree,rightTree):
    if leftTree == None and rightTree == None:
        return True
    elif leftTree != None and rightTree != None:
        return leftTree.val == rightTree.val and isMirror(leftTree.left, rightTree.right) and isMirror(leftTree.right, rightTree.left)

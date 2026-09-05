# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def divide(inorder, postorder):
            if not inorder:
                return None

            root = TreeNode(postorder.pop())
            idx = inorder.index(root.val)
            root.right = divide(inorder[idx+1:], postorder)
            root.left = divide(inorder[:idx], postorder)
            return root

        return divide(inorder, postorder)
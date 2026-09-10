# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        flipped = False
        output = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.pop()
                cur.append(node.val)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            output.append(cur if not flipped else cur[::-1])
            flipped = not flipped

        return output

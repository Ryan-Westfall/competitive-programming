"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        first = None
        last = None

        def dfs(node):
            nonlocal first
            nonlocal last

            if not node:
                return

            dfs(node.left)

            if not first:
                first = node
                last = node
            else:
                node.left = last
                last.right = node
                last = node

            dfs(node.right)

        dfs(root)

        first.left = last
        last.right = first

        return first
        
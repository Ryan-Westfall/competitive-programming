"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = deque([root])
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    node.next = prev
                prev = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return root

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        hashmap = {}

        def dfsBuild(node):
            if not node:
                return

            hashmap[node] = NodeCopy(node.val)

            dfsBuild(node.left)
            dfsBuild(node.right)

        dfsBuild(root)

        for old in hashmap:
            if old.left:
                hashmap[old].left = hashmap[old.left]
            if old.right:
                hashmap[old].right = hashmap[old.right]
            if old.random:
                hashmap[old].random = hashmap[old.random]

        return hashmap.get(root, None)
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        seen = defaultdict(list)
        
        def dfs(node, count):
            if not node:
                return
            seen[count].append(node.val)
            
            for i in node.children:
                dfs(i, count+1)
            
        dfs(root, 0)
        
        output = []
        for i in seen.values():
            output.append(i)

        return output
            
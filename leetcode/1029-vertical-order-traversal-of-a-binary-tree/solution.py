# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list) # (y, val)

        queue = deque([(root, 0, 0)]) # (node, x, y)
        minX = 0
        maxX = 0

        while queue:
            for _ in range(len(queue)):
                node, x, y = queue.popleft()

                hashmap[x].append((y, node.val))
                minX = min(minX, x)
                maxX = max(maxX, x)
                
                if node.left:
                    queue.append((node.left, x - 1, y + 1))
                if node.right:
                    queue.append((node.right, x + 1, y + 1))

        result = []

        for x in range(minX, maxX + 1):
            result.append([x[1] for x in sorted(hashmap[x], key=lambda x: (x[0], x[1]))])

        return result



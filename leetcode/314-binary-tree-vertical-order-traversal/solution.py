# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        store = defaultdict(list)

        queue = collections.deque([(0,root)])

        max_x = float('-inf')
        min_x = float('inf')
        while queue:
            indexRelation, node = queue.popleft()
            store[indexRelation].append(node.val)
            max_x = max(max_x, indexRelation)
            min_x = min(min_x, indexRelation)
            if node.left:
                queue.append((indexRelation - 1, node.left))
            if node.right:
                queue.append((indexRelation + 1, node.right))

        res = []
        for i in range(min_x, max_x + 1):
            res.append(store[i])

        return res

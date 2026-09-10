class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        left_to_right = True
        output = []

        while queue:
            cur = []

            for _ in range(len(queue)):
                if left_to_right:
                    node = queue.popleft()
                    cur.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    cur.append(node.val)

                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

            output.append(cur)
            left_to_right = not left_to_right

        return output
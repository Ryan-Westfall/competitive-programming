class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        # Find the two nodes whose values are out of order
        first = None
        second = None

        for i in range(1, len(nodes)):
            if nodes[i - 1].val > nodes[i].val:
                if first is None:
                    first = nodes[i - 1]
                second = nodes[i]

        first.val, second.val = second.val, first.val
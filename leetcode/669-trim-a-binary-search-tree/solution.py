class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None

            # Current node is too small.
            # Everything in the left subtree is even smaller, so discard it.
            if node.val < low:
                return dfs(node.right)

            # Current node is too large.
            # Everything in the right subtree is even larger, so discard it.
            if node.val > high:
                return dfs(node.left)

            # Current node is valid. Trim both sides.
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return node

        return dfs(root)
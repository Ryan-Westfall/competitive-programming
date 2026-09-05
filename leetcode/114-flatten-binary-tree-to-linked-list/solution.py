class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def dfs(node):
            nonlocal prev

            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None

            prev = node

        dfs(root)
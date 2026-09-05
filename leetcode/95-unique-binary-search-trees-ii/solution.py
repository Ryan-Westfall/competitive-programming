class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(left, right):
            if left > right:
                return [None]

            output = []

            for i in range(left, right + 1):
                leftTrees = backtrack(left, i - 1)
                rightTrees = backtrack(i + 1, right)

                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        root = TreeNode(i)
                        root.left = leftTree
                        root.right = rightTree
                        output.append(root)

            return output

        return backtrack(1, n)
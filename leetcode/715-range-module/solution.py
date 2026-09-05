class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.covered = False
        self.lazy = -1      # -1 = nothing pending, 0 = uncover, 1 = cover


class RangeModule:

    def __init__(self):
        self.root = Node()

    def push(self, node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()

        if node.lazy == -1:
            return

        node.left.covered = node.right.covered = (node.lazy == 1)
        node.left.lazy = node.right.lazy = node.lazy
        node.lazy = -1

    def update(self, node, nodeL, nodeR, left, right, cover):
        # no overlap
        if nodeR <= left or right <= nodeL:
            return

        # fully covered
        if left <= nodeL and nodeR <= right:
            node.covered = cover
            node.lazy = 1 if cover else 0
            return

        self.push(node)

        mid = (nodeL + nodeR) // 2

        self.update(node.left, nodeL, mid, left, right, cover)
        self.update(node.right, mid, nodeR, left, right, cover)

        node.covered = node.left.covered and node.right.covered

    def query(self, node, nodeL, nodeR, left, right):
        # no overlap
        if nodeR <= left or right <= nodeL:
            return True

        # fully inside
        if left <= nodeL and nodeR <= right:
            return node.covered

        self.push(node)

        mid = (nodeL + nodeR) // 2

        return (
            self.query(node.left, nodeL, mid, left, right)
            and
            self.query(node.right, mid, nodeR, left, right)
        )

    def addRange(self, left: int, right: int) -> None:
        self.update(self.root, 0, 10**9, left, right, True)

    def removeRange(self, left: int, right: int) -> None:
        self.update(self.root, 0, 10**9, left, right, False)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(self.root, 0, 10**9, left, right)
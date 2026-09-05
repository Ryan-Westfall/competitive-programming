class Node:
    def __init__(self):
        self.val = 0      # maximum overlap in this range
        self.lazy = 0     # pending addition to this range
        self.left = None
        self.right = None


class MyCalendarTwo:

    def __init__(self):
        # Represents time range [0, 1e9]
        self.root = Node()


    def update(self, node, start, end, l, r, value):

        # No overlap
        if r < start or end < l:
            return


        # Complete overlap:
        # node range [start,end] is fully inside update [l,r]
        if l <= start and end <= r:
            node.val += value
            node.lazy += value
            return


        # Partial overlap
        mid = (start + end) // 2

        if not node.left:
            node.left = Node()

        if not node.right:
            node.right = Node()


        self.update(
            node.left,
            start,
            mid,
            l,
            r,
            value
        )

        self.update(
            node.right,
            mid + 1,
            end,
            l,
            r,
            value
        )


        # The children may have changed.
        # Add this node's lazy value because it applies
        # to the entire range.
        node.val = node.lazy + max(
            node.left.val,
            node.right.val
        )


    def book(self, startTime: int, endTime: int) -> bool:

        # Try adding this booking
        self.update(
            self.root,
            0,
            10**9,
            startTime,
            endTime - 1,
            1
        )


        # Triple booking happened
        if self.root.val > 2:

            # Undo the booking
            self.update(
                self.root,
                0,
                10**9,
                startTime,
                endTime - 1,
                -1
            )

            return False


        return True
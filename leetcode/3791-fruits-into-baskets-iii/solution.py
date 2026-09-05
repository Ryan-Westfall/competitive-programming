class SegmentTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, baskets)

    def build(self, node, left, right, baskets):
        if left == right:
            self.tree[node] = baskets[left]
            return self.tree[node]

        mid = (left + right) // 2

        left_max = self.build(node * 2, left, mid, baskets)
        right_max = self.build(node * 2 + 1, mid + 1, right, baskets)

        self.tree[node] = max(left_max, right_max)

        return self.tree[node]

    def query(self, node, left, right, fruit):
        # no basket in this range can fit fruit
        if self.tree[node] < fruit:
            return -1

        # found a basket
        if left == right:
            return left

        mid = (left + right) // 2

        # always try left first because we need leftmost
        idx = self.query(node * 2, left, mid, fruit)

        if idx != -1:
            return idx

        return self.query(node * 2 + 1, mid + 1, right, fruit)

    def update(self, node, left, right, idx, value):
        if left == right:
            self.tree[node] = value
            return

        mid = (left + right) // 2

        if idx <= mid:
            self.update(node * 2, left, mid, idx, value)
        else:
            self.update(node * 2 + 1, mid + 1, right, idx, value)

        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)

        ans = 0

        for fruit in fruits:
            idx = st.query(1, 0, len(baskets)-1, fruit)

            if idx == -1:
                ans += 1
            else:
                st.update(1, 0, len(baskets)-1, idx, 0)

        return ans
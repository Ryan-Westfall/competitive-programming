class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [[0, [0] * k] for _ in range(4 * self.n)]
        self.nums = nums

        self.build(1, 0, self.n - 1)

    def merge(self, left, right):
        leftProd, leftCnt = left
        rightProd, rightCnt = right

        # Product of the entire combined segment
        prod = (leftProd * rightProd) % self.k

        # Prefixes that end inside the left segment
        cnt = leftCnt[:]

        # Prefixes that go through all of left
        # and then into the right segment
        for r in range(self.k):
            newRemainder = (leftProd * r) % self.k
            cnt[newRemainder] += rightCnt[r]

        return [prod, cnt]

    def build(self, node, l, r):
        if l == r:
            prod = self.nums[l] % self.k

            cnt = [0] * self.k
            cnt[prod] = 1

            self.tree[node] = [prod, cnt]
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, node, l, r, index, value):
        if l == r:
            prod = value % self.k

            cnt = [0] * self.k
            cnt[prod] = 1

            self.tree[node] = [prod, cnt]
            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, value)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def point_update(self, index, value):
        self.update(1, 0, self.n - 1, index, value)

    def query(self, node, l, r, start):
        # Entire segment is part of [start, n-1]
        if start <= l:
            return self.tree[node]

        mid = (l + r) // 2

        if start <= mid:
            left = self.query(node * 2, l, mid, start)
            right = self.query(node * 2 + 1, mid + 1, r, start)

            return self.merge(left, right)

        return self.query(node * 2 + 1, mid + 1, r, start)

    def suffix_query(self, start):
        return self.query(1, 0, self.n - 1, start)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        segTree = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:
            # Persistent update
            segTree.point_update(index, value)

            # Information about nums[start:]
            prod, cnt = segTree.suffix_query(start)

            ans.append(cnt[x])

        return ans
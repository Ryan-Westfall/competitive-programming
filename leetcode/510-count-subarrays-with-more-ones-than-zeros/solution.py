class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, left, right, idx):
        if left == right:
            self.tree[node] += 1
            return

        mid = (left + right) // 2

        if idx <= mid:
            self.update(node * 2, left, mid, idx)
        else:
            self.update(node * 2 + 1, mid + 1, right, idx)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, left, right, ql, qr):
        if qr < left or right < ql:
            return 0

        if ql <= left and right <= qr:
            return self.tree[node]

        mid = (left + right) // 2

        return (
            self.query(node * 2, left, mid, ql, qr)
            + self.query(node * 2 + 1, mid + 1, right, ql, qr)
        )


class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums):
        MOD = 10**9 + 7

        # Compute prefix sums (1 -> +1, 0 -> -1)
        prefix = [0]
        cur = 0
        for x in nums:
            cur += 1 if x == 1 else -1
            prefix.append(cur)

        # Coordinate compression
        values = sorted(set(prefix))
        compress = {v: i for i, v in enumerate(values)}

        st = SegmentTree(len(values))

        ans = 0

        for p in prefix:
            idx = compress[p]

            # Count previous prefix sums < current
            if idx > 0:
                ans += st.query(1, 0, st.n - 1, 0, idx - 1)

            # Insert current prefix sum
            st.update(1, 0, st.n - 1, idx)

        return ans % MOD
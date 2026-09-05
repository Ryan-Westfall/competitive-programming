class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg_tree = [0] * (4 * n)
        self.lazy = [None] * (4 * n)

    def push(self, v, tl, tr):
        if self.lazy[v] is not None:
            # Set entire interval to lazy value
            self.seg_tree[v] = self.lazy[v] * (tr - tl + 1)

            # Propagate to children
            if tl < tr:
                self.lazy[v * 2] = self.lazy[v]
                self.lazy[v * 2 + 1] = self.lazy[v]

            # Clear lazy
            self.lazy[v] = None

    def update_helper(self, v, tl, tr, l, r, val):
        self.push(v, tl, tr)

        if l > r:
            return

        # Entire range covered
        if l == tl and tr == r:
            self.lazy[v] = val
            self.push(v, tl, tr)
            return

        tm = (tl + tr) // 2

        self.update_helper(
            v * 2,
            tl,
            tm,
            l,
            min(r, tm),
            val
        )

        self.update_helper(
            v * 2 + 1,
            tm + 1,
            tr,
            max(l, tm + 1),
            r,
            val
        )

        self.push(v * 2, tl, tm)
        self.push(v * 2 + 1, tm + 1, tr)

        self.seg_tree[v] = (
            self.seg_tree[v * 2] +
            self.seg_tree[v * 2 + 1]
        )

    def update(self, l, r, val):
        self.update_helper(1, 0, self.n - 1, l, r, val)

    def query_helper(self, v, tl, tr, l, r):
        self.push(v, tl, tr)

        if l > r:
            return 0

        # Completely inside query range
        if l <= tl and tr <= r:
            return self.seg_tree[v]

        tm = (tl + tr) // 2

        return (
            self.query_helper(
                v * 2,
                tl,
                tm,
                l,
                min(r, tm)
            )
            +
            self.query_helper(
                v * 2 + 1,
                tm + 1,
                tr,
                max(l, tm + 1),
                r
            )
        )

    def query(self, l, r):
        return self.query_helper(1, 0, self.n - 1, l, r)


class Solution:
    def amountPainted(self, paint):
        MAX_SIZE = 50005

        st = SegmentTree(MAX_SIZE)

        ans = []

        for start, end in paint:
            end -= 1

            # How much is already painted?
            already_painted = st.query(start, end)

            # New paint = total range - old paint
            ans.append(
                end - start + 1 - already_painted
            )

            # Mark this interval as painted
            st.update(start, end, 1)

        return ans
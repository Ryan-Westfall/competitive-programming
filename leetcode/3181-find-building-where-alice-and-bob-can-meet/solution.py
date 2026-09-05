class Solution:
    def leftmostBuildingQueries(
        self,
        heights: List[int],
        queries: List[List[int]]
    ) -> List[int]:

        n = len(heights)

        # Segment tree where each node stores:
        # the maximum height in that range
        tree = [0] * (4 * n)


        def build(node, l, r):
            # Leaf node
            if l == r:
                tree[node] = heights[l]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            # Parent stores maximum of children
            tree[node] = max(
                tree[node * 2],
                tree[node * 2 + 1]
            )


        build(1, 0, n - 1)


        def findFirst(node, l, r, start, target):
            """
            Find the first index >= start
            where heights[index] > target
            """

            # This range is completely before our search area
            if r < start:
                return -1


            # If the maximum height in this range
            # is not greater than target,
            # nobody inside can be an answer
            if tree[node] <= target:
                return -1


            # We found a building
            if l == r:
                return l


            mid = (l + r) // 2


            # Search left first because we want
            # the smallest index
            left = findFirst(
                node * 2,
                l,
                mid,
                start,
                target
            )

            if left != -1:
                return left


            # If left failed, search right
            return findFirst(
                node * 2 + 1,
                mid + 1,
                r,
                start,
                target
            )


        ans = []

        for a, b in queries:

            # Make b the rightmost person
            if a > b:
                a, b = b, a


            # Already at same building
            if a == b:
                ans.append(a)
                continue


            # Bob can move to Alice's building
            # because Bob's building is taller
            if heights[b] > heights[a]:
                ans.append(b)
                continue


            # Need first building after b
            # taller than Alice
            ans.append(
                findFirst(
                    1,
                    0,
                    n - 1,
                    b + 1,
                    heights[a]
                )
            )

        return ans
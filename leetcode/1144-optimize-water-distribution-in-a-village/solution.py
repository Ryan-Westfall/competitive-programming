class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        edges = pipes[:]

        for i, cost in enumerate(wells):
            edges.append([0, i + 1, cost])

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(n + 1)

        ans = 0

        for u, v, cost in edges:
            if uf.union(u, v):
                ans += cost

        return ans


        
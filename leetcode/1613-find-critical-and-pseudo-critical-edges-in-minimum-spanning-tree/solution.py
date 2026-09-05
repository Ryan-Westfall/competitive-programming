class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.rank[pa] += self.rank[pb]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Save original indices
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        def kruskal(skip=-1, force=-1):
            uf = UnionFind(n)
            weight = 0
            used = 0

            # Force an edge first
            if force != -1:
                u, v, w, _ = edges[force]
                if uf.union(u, v):
                    weight += w
                    used += 1

            # Build MST
            for i, (u, v, w, _) in enumerate(edges):
                if i == skip:
                    continue

                if uf.union(u, v):
                    weight += w
                    used += 1

            return weight if used == n - 1 else float("inf")

        base = kruskal()

        critical = []
        pseudo = []

        for i in range(len(edges)):
            if kruskal(skip=i) > base:
                critical.append(edges[i][3])
            elif kruskal(force=i) == base:
                pseudo.append(edges[i][3])

        return [critical, pseudo]
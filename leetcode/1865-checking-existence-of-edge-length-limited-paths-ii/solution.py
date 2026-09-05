from typing import List
from collections import defaultdict
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):

        uf = UnionFind(n)

        edgeList.sort(key=lambda x: x[2])

        self.graph = defaultdict(list)

        # Build MST
        for u, v, w in edgeList:
            if uf.union(u, v):
                self.graph[u].append((v, w))
                self.graph[v].append((u, w))

        self.uf = uf

        LOG = math.ceil(math.log2(n)) + 1

        self.up = [[-1] * LOG for _ in range(n)]
        self.maxEdge = [[0] * LOG for _ in range(n)]
        self.depth = [0] * n
        visited = [False] * n

        def dfs(node, parent):

            visited[node] = True

            for nei, weight in self.graph[node]:

                if nei == parent:
                    continue

                self.depth[nei] = self.depth[node] + 1
                self.up[nei][0] = node
                self.maxEdge[nei][0] = weight

                dfs(nei, node)

        # Forest possible if graph disconnected
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        # Binary lifting preprocessing
        for j in range(1, LOG):
            for i in range(n):

                if self.up[i][j - 1] != -1:

                    ancestor = self.up[i][j - 1]

                    self.up[i][j] = self.up[ancestor][j - 1]

                    self.maxEdge[i][j] = max(
                        self.maxEdge[i][j - 1],
                        self.maxEdge[ancestor][j - 1]
                    )

    def query(self, p: int, q: int, limit: int) -> bool:

        if self.uf.find(p) != self.uf.find(q):
            return False

        maxWeight = 0

        if self.depth[p] < self.depth[q]:
            p, q = q, p

        LOG = len(self.up[0])

        # Lift p up to q's depth
        diff = self.depth[p] - self.depth[q]

        for j in range(LOG - 1, -1, -1):

            if diff & (1 << j):
                maxWeight = max(maxWeight, self.maxEdge[p][j])
                p = self.up[p][j]

        if p == q:
            return maxWeight < limit

        # Lift both together
        for j in range(LOG - 1, -1, -1):

            if self.up[p][j] != self.up[q][j]:

                maxWeight = max(maxWeight, self.maxEdge[p][j])
                maxWeight = max(maxWeight, self.maxEdge[q][j])

                p = self.up[p][j]
                q = self.up[q][j]

        # Last step to LCA
        maxWeight = max(maxWeight, self.maxEdge[p][0])
        maxWeight = max(maxWeight, self.maxEdge[q][0])

        return maxWeight < limit
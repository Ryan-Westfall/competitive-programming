from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = defaultdict(list)

        for src, dst, cost in edges:
            self.adj[src].append((dst, cost))

    def addEdge(self, edge: List[int]) -> None:
        src, dst, cost = edge
        self.adj[src].append((dst, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")] * self.n
        dist[node1] = 0

        minHeap = [(0, node1)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node == node2:
                return cost

            if cost > dist[node]:
                continue

            for nei, weight in self.adj[node]:
                newCost = cost + weight

                if newCost < dist[nei]:
                    dist[nei] = newCost
                    heapq.heappush(minHeap, (newCost, nei))

        return -1
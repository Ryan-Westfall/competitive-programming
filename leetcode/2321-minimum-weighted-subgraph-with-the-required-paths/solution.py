class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        graph = defaultdict(list)
        rev = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v,w))
            rev[v].append((u,w))


        def dijkstra(start, graph):
            dist = [float("inf")] * n
            dist[start] = 0

            heap = [(0,start)]

            while heap:
                d,node = heapq.heappop(heap)

                if d > dist[node]:
                    continue

                for nei,w in graph[node]:
                    nd = d+w

                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(heap,(nd,nei))

            return dist


        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        dist3 = dijkstra(dest, rev)


        ans = float("inf")

        for x in range(n):
            ans = min(
                ans,
                dist1[x] + dist2[x] + dist3[x]
            )


        return -1 if ans == float("inf") else ans
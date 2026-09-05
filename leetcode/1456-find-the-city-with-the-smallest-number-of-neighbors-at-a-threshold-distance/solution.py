class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = defaultdict(list)

        for src, dst, w in edges:
            adjList[src].append((dst, w))
            adjList[dst].append((src, w))

        ans = -1
        minCount = float('inf')

        for src in range(n):
            dist = [float('inf')] * n
            dist[src] = 0

            heap = [(0, src)]

            while heap:
                curDist, node = heapq.heappop(heap)

                # stale heap entry
                if curDist > dist[node]:
                    continue

                for nei, weight in adjList[node]:
                    newDist = curDist + weight

                    if newDist < dist[nei]:
                        dist[nei] = newDist
                        heapq.heappush(heap, (newDist, nei))

            count = 0
            for city in range(n):
                if city != src and dist[city] <= distanceThreshold:
                    count += 1

            if count <= minCount:
                minCount = count
                ans = src

        return ans
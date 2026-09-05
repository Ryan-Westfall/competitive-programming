class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, points[0])]
        visited = set()
        output = 0
        while len(visited) < len(points):
            w, (x1,y1) = heapq.heappop(minHeap)
            
            if (x1,y1) in visited:
                continue

            visited.add((x1,y1))
            output += w

            for x2,y2 in points:
                if (x2,y2) in visited:
                    continue
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (distance, [x2,y2]))

        return output

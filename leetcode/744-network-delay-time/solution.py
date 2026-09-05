class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for src, dst, weight in times:
            adjList[src].append((dst,weight))

        minHeap = [(0,k)]
        visited = set()
        output = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            output = max(output, time)
            visited.add(node)
            
            for nei, nTime in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + nTime, nei))
            
        return output if len(visited) == n else -1

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adjList[src], dst)

        output = deque([])

        def dfs(node):
            while adjList[node]:
                nextEdge = heapq.heappop(adjList[node])
                dfs(nextEdge)
            output.appendleft(node)

        dfs("JFK")

        return list(output)

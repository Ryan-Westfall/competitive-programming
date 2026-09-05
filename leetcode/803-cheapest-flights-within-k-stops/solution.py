class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for source, destination, price in flights:
            adjList[source].append((destination, price))

        # minToGetTo[node][steps] = cheapest cost to reach node
        # using exactly `steps` flights
        minToGetTo = defaultdict(lambda: defaultdict(lambda: float('inf')))

        queue = [(0, src, 0)]

        while queue:
            curCost, node, steps = heapq.heappop(queue)

            if node == dst:
                return curCost

            if steps == k + 1:
                continue

            for nei, cost in adjList[node]:
                newCost = curCost + cost
                newSteps = steps + 1

                if newCost < minToGetTo[nei][newSteps]:
                    minToGetTo[nei][newSteps] = newCost
                    heapq.heappush(queue, (newCost, nei, newSteps))

        return -1
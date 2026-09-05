class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adjList = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                adjList[stop].append(i)

        queue = deque([source])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()

                if stop == target:
                    return steps

                for routeIndex in adjList[stop]:
                    route = routes[routeIndex]

                    if route:
                        for nei in route:
                            if nei != stop:
                                queue.append(nei)

                        route.clear()

            steps += 1

        return -1
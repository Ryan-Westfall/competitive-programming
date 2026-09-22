class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stopToRoutes = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].append(i)

        # print(stopToRoutes)

        queue = deque(stopToRoutes[source])
        visited = set(queue)
        buses = 1

        while queue:
            for _ in range(len(queue)):
                route = queue.popleft()

                if target in routes[route]:
                    return buses

                for stop in routes[route]:
                    for nei in stopToRoutes[stop]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

            buses += 1

        return -1
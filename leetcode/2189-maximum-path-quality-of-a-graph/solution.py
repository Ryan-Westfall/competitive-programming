class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:

        n = len(values)

        graph = defaultdict(list)

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        seen = [0] * n
        self.answer = 0

        def dfs(node, time, quality):
            if node == 0:
                self.answer = max(self.answer, quality)

            seen[node] += 1
            for neighbor, cost in graph[node]:
                if time + cost <= maxTime:
                    add = 0
                    if seen[neighbor] == 0:
                        add = values[neighbor]

                    dfs(neighbor, time + cost, quality + add)

            seen[node] -= 1

        dfs(0, 0, values[0])

        return self.answer

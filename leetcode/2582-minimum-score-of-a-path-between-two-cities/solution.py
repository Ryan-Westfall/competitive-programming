class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited = set()
        self.minVisited = float('inf')
        adjList = defaultdict(list)

        for src, dst, distance in roads:
            adjList[src].append((dst,distance))
            adjList[dst].append((src,distance))


        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for dst, distance in adjList[node]:
                self.minVisited = min(self.minVisited, distance)
                if dst not in visited:
                    dfs(dst)
            
        dfs(1)

        return self.minVisited
        
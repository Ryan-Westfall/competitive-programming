class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        segments = []

        def dfs(node, seen, segment):
            if node in seen:
                return

            seen.add(node)
            segment.append(node)
            for edge in adjList[node]:
                dfs(edge,seen,segment)

        seen = set()
        for node in range(n):
            segment = []
            dfs(node, seen, segment)
            if segment:
                segments.append(segment)

        completedComponents = len(segments)
        for segment in segments:
            for node in segment:
                if len(adjList[node]) != len(segment) - 1:
                    completedComponents -= 1
                    break


        return completedComponents
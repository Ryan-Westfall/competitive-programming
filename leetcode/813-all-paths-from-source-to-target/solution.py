class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node,cur):
            if node == len(graph) - 1:
                paths.append(cur[:])
                return

            for nei in graph[node]:
                cur.append(nei)
                dfs(nei, cur)
                cur.pop()

        dfs(0, [0])

        return paths
        
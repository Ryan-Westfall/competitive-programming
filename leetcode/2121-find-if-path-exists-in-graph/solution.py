class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        seen  = set()

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(node):
            if node in seen:
                return False
            if node == destination:
                return True

            seen.add(node)
            for edge in adjList[node]:
                if dfs(edge):
                    return True

            return False

        return dfs(source)
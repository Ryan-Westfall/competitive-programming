class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)

        adjList = defaultdict(list)

        # Build every vertex and its k outgoing edges
        def build(node):
            if len(node) == n - 1:
                for digit in range(k):
                    adjList[node].append(
                        node[1:] + str(digit)
                    )
                return

            for digit in range(k):
                build(node + str(digit))

        build("")

        # Hierholzer
        result = []

        def dfs(node):
            while adjList[node]:
                nxt = adjList[node].pop()
                dfs(nxt)

            result.append(node)

        dfs(start)

        result.reverse()

        # Convert Eulerian path of vertices into the answer
        return result[0] + "".join(node[-1] for node in result[1:])
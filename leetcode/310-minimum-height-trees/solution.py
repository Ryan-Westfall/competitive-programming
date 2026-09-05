class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjList = defaultdict(list)

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        queue = deque()

        for node in adjList:
            if len(adjList[node]) == 1:
                queue.append(node)

        remaining = n

        while remaining > 2:
            levelSize = len(queue)
            remaining -= levelSize

            for _ in range(levelSize):
                node = queue.popleft()

                for nei in adjList[node]:
                    adjList[nei].remove(node)

                    if len(adjList[nei]) == 1:
                        queue.append(nei)

        return list(queue)
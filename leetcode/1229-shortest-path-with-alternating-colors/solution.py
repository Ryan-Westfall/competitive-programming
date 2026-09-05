class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adjBlue = defaultdict(list)
        for src, dst in blueEdges:
            adjBlue[src].append(dst)

        adjRed = defaultdict(list)
        for src, dst in redEdges:
            adjRed[src].append(dst)

        output = [-1 for _ in range(n)]
        for isRed in (True,False):
            queue = deque([0])
            visitedBlue = set([0])
            visitedRed = set([0])
            level = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    output[node] = min(output[node], level) if output[node] != -1 else level
                    if isRed:
                        for nei in adjRed[node]:
                            print(nei)
                            if nei not in visitedRed:
                                visitedRed.add(nei)
                                queue.append(nei)
                    else:
                        for nei in adjBlue[node]:
                            if nei not in visitedBlue:
                                visitedBlue.add(nei)
                                queue.append(nei)

                isRed = not isRed
                level += 1

        return output
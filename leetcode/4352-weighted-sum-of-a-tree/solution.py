class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        adjList = defaultdict(list)

        for node, parentNode in enumerate(parent):
            if node == 0:
                continue

            adjList[parentNode].append(node)


        queue = deque([0])
        depthList = [-1] * len(parent)
        output = 0
        height = 0

        depth = 0
        while queue:
            depth += 1
            height = max(height, depth)
            for _ in range(len(queue)):
                node = queue.popleft()
                depthList[node] = depth
                for nei in adjList[node]:
                    queue.append(nei)


        for node in range(len(parent)):
            output += nums[node] * (height - depthList[node] + 1)
        return output
            
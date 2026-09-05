class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjacencyList = {i: [] for i in range(1, n+1)}
        directedCount = {i: 0 for i in range(1, n+1)}

        for pre, course in relations:
            adjacencyList[pre].append(course)
            directedCount[course] += 1

        queue = deque([])
        for k,v in directedCount.items():
            if v == 0:
                queue.append(k)


        count = 0
        studiedCount = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                studiedCount += 1
                queueNode = queue.popleft()
                for nextNode in adjacencyList[queueNode]:
                    directedCount[nextNode] -= 1
                    if directedCount[nextNode] == 0:
                        queue.append(nextNode)

        return count if studiedCount == n else -1
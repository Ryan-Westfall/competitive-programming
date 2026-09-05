from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        visit = 0
        while queue:
            node = queue.popleft()
            visit += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return visit == numCourses

        


        
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(set)
        indegree = [0] * numCourses

        for prereq, course in prerequisites:
            adjList[prereq].add(course)
            indegree[course] += 1

        queue = [i for i in range(numCourses) if indegree[i] == 0]

        def buildIndirect(node):
            if node in memo:
                return memo[node]

            descendants = set()

            for nei in adjList[node]:
                descendants.add(nei)
                descendants |= buildIndirect(nei)

            memo[node] = descendants
            return descendants

        memo = {}

        for node in range(numCourses):
            adjList[node] |= buildIndirect(node)

        return [b in adjList[a] for a, b in queries]
from collections import deque
from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        # pre[i] = bitmask of prerequisites for course i
        pre = [0] * n

        for u, v in relations:
            pre[v - 1] |= 1 << (u - 1)

        target = (1 << n) - 1

        q = deque([(0, 0)])      # (completedMask, semesters)
        visited = {0}

        while q:
            mask, semesters = q.popleft()

            if mask == target:
                return semesters

            # Build bitmask of currently available courses
            available = 0

            for course in range(n):

                # already completed
                if mask & (1 << course):
                    continue

                # prerequisites satisfied
                if (pre[course] & mask) == pre[course]:
                    available |= 1 << course

            # Count available courses
            if available.bit_count() <= k:
                newMask = mask | available

                if newMask not in visited:
                    visited.add(newMask)
                    q.append((newMask, semesters + 1))

            else:
                # Convert available bitmask -> list of course indices
                courses = []

                for i in range(n):
                    if available & (1 << i):
                        courses.append(i)

                # Try every choice of k courses
                for subset in combinations(courses, k):

                    newMask = mask

                    for c in subset:
                        newMask |= 1 << c

                    if newMask not in visited:
                        visited.add(newMask)
                        q.append((newMask, semesters + 1))
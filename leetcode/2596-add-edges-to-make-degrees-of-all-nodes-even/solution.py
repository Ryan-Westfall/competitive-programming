from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)

        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        odds = set()
        evens = set()

        # Include isolated vertices
        for node in range(1, n + 1):
            if len(adjList[node]) % 2 == 0:
                evens.add(node)
            else:
                odds.add(node)

        if len(odds) == 0:
            return True

        if len(odds) == 2:
            odd1, odd2 = tuple(odds)

            # Can connect them directly
            if odd2 not in adjList[odd1]:
                return True

            # Otherwise need an even vertex connected to neither
            for even in evens:
                if (
                    even not in adjList[odd1]
                    and even not in adjList[odd2]
                ):
                    return True

            return False

        if len(odds) == 4:
            first = odds.pop()

            for second in odds:
                remaining = odds - {second}
                third, fourth = tuple(remaining)

                if (
                    second not in adjList[first]
                    and fourth not in adjList[third]
                ):
                    return True

            return False

        return False
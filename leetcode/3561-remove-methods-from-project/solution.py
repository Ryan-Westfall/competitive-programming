from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dst in invocations:
            adj[src].append(dst)

        sus = set()

        def dfs(node):
            if node in sus:
                return
            sus.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(k)

        # If any non-suspicious method invokes a suspicious one,
        # we cannot remove the suspicious methods.
        for src, dst in invocations:
            if src not in sus and dst in sus:
                return list(range(n))

        return [i for i in range(n) if i not in sus]
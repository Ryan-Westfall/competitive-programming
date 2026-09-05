class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        memoTime = {i: 0 for i in range(1, n+ 1)}
        for src, dst in relations:
            adj[src].append(dst)
        
        
        def dfs(node):
            if memoTime[node]:
                return memoTime[node]

            timeCount = time[node - 1]
            for dst in adj[node]:
                timeCount = max(timeCount, time[node - 1] + dfs(dst))
                
            memoTime[node] = timeCount
            return timeCount

        timeNeeded = 0
        for i in range(1, n+1):
            timeNeeded = max(dfs(i), timeNeeded)

        return timeNeeded
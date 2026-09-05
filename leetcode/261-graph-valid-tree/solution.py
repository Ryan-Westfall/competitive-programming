class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create Adjacency List
        preMap = {i:[] for i in range(n)}
        for i, j in edges:
            preMap[i].append(j)
            preMap[j].append(i)

        # print(preMap)

        visit = set([])

        def dfs(cur, prev):
            if cur in visit:
                return False
                    
            visit.add(cur)
            for nxt in preMap[cur]:
                if nxt == prev:
                    continue
                if not dfs(nxt, cur): return False
            return True

        # return dfs(0, -1)

        return dfs(0, -1) and len(visit) == n

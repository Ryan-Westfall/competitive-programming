class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        seen = defaultdict(set)
        
        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            if px != py:
                parent[px] = py

        output = [True for _ in range(len(requests))]
        for i, v in enumerate(requests):
            x, y = v
            px = find(x)
            py = find(y)
            if px == py:
                continue
            for xr, xy in restrictions:
                prx = find(xr)
                pry = find(xy)
                if (prx == px or prx == py) and (pry == px or pry == py):
                    output[i] = False
                    break
            if output[i]:
                union(x,y)

        return output

        
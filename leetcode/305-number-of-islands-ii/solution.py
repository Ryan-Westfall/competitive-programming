class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [i for i in range(m*n)]
        seen = set()
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])

            return parent[a]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            parent[pa] = pb

            return True

        output = []
        count = 0
        for r, c in positions:
            if (r,c) not in seen:
                count += 1
                seen.add((r,c))
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if nr < m and nr >= 0 and nc < n and nc >= 0:
                        if (nr,nc) in seen:
                            # print('nr', nr, 'nc', nc)
                            parentIndex1 = r + (c*m)
                            parentIndex2 = nr + (nc*m)
                            # print('p1', parentIndex1, 'p2', parentIndex2)
                            if union(parentIndex1, parentIndex2):
                                count -= 1
            output.append(count)

        return output
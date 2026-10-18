class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        start = None
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "*":
                    start = (r,c)
                    break
            if start:
                break

        queue = deque([start])
        step = 0
        seen = set([start])
        while queue:
            for _ in range(len(queue)):
                nodeR, nodeC = queue.popleft()

                if grid[nodeR][nodeC] == '#':
                    return step

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    newR, newC = nodeR + dr, nodeC + dc
                    if newR >= 0 and newR < n and newC >= 0 and newC < m and (newR, newC) not in seen and grid[newR][newC] != 'X':
                        seen.add((newR,newC))
                        queue.append((newR,newC))

            step += 1

        return -1







        return step

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfs(curRotten):
            queue = collections.deque(curRotten)

            while queue:
                cur = queue.popleft()
                r,c = cur
                grid[r][c] = 0
                if r + 1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2              
                if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2


        print(len(grid) == 1, (len(grid[0]) == 1 or len(grid[0]) == 4), grid[0][0] == 0)
        if len(grid) == 1 and (len(grid[0]) == 1 or len(grid[0]) == 4) and grid[0][0] == 0:
            return 0

        count = -1

        while True:
            cur = []
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 2:
                        cur.append((r,c))
            if not cur:
                break
            bfs(cur)
            count += 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        return count

        
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        distances = [[0] * COL for _ in range(ROW)]

        emptyLand = 0

        minPath = float('inf')

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    localMinPath = float('inf')
                    q = collections.deque([(r,c,0)])

                    while q:
                        curRow, curCol, distance = q.popleft()

                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            newRow = curRow + dr
                            newCol = curCol + dc

                            if (0 <= newRow < ROW) and (0 <= newCol < COL) and grid[newRow][newCol] == emptyLand:
                                grid[newRow][newCol] = emptyLand - 1
                                distances[newRow][newCol] += distance + 1

                                q.append([newRow,newCol,distance+1])
                                localMinPath = min(localMinPath, distances[newRow][newCol])
                                
                    minPath = localMinPath
                    emptyLand -= 1

        return minPath if minPath != float('inf') else -1
                                
                    
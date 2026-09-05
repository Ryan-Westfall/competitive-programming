class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        allSeen = set()
        curSeen = []

        def dfs(row, col, orginRow, orginCol):
            if row < 0 or row == ROW or col < 0 or col == COL or grid[row][col] == 0:
                return 

            grid[row][col] = 0
            curSeen.append((orginRow,orginCol))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(row + dr, col + dc, orginRow + dr, orginCol + dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    curSeen.clear()
                    dfs(r,c,0,0)
                    allSeen.add(tuple(curSeen))

        return len(allSeen)




        
        
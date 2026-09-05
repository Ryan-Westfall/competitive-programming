class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0:
                return 1
            
            total = 0
            seen.add((row,col))
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                if (row + dr, col + dc) not in seen:
                    total += dfs(row + dr, col + dc)

            return total

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row,col)
                

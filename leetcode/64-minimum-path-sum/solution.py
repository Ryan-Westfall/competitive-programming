class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def minPath(r,c):
            if r > len(grid) - 1 or c > len(grid[0]) - 1:
                return float('inf')
            if len(grid) - 1 == r and len(grid[0]) - 1 == c:
                return grid[-1][-1]

            down = minPath(r + 1, c)
            right = minPath(r, c + 1)

            return grid[r][c] + min(down, right)

        return minPath(0,0)
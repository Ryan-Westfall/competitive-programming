class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) - 1
        m = len(obstacleGrid[0]) - 1

        @cache
        def unique(r,c):
            if r > n or c > m or obstacleGrid[r][c] == 1:
                return 0
            if r == n and c == m:
                return 1

            down = unique(r + 1, c)
            right = unique(r, c + 1)

            return down + right

        return unique(0,0)
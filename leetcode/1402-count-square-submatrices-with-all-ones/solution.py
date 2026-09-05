class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for col in range(m + 1)] for row in range(n + 1)]

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 1:
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1


        total = 0
        for row in dp:
            for col in row:
                total += col

        return total

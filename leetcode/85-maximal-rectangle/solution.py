class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        @cache
        def right(row, col):
            if row >= n or col >= m or matrix[row][col] == '0':
                return 0

            return 1 + right(row, col + 1)

        @cache
        def maxRectangleSeen(row, col):
            if row >= n or col >= m:
                return 0

            if matrix[row][col] == '0':
                return 0

            best = 0
            width = float('inf')

            for r in range(row, n):
                width = min(width, right(r, col))

                if width == 0:
                    break

                height = r - row + 1
                best = max(best, width * height)

            return best

        return max(
            maxRectangleSeen(row, col)
            for row in range(n)
            for col in range(m)
        )
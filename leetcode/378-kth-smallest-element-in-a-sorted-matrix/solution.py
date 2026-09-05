class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)

        def count(x):
            total = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    # Everything above this element in this column
                    # is also <= x.
                    total += row + 1
                    col += 1
                else:
                    # Everything below this element is > x.
                    row -= 1

            return total

        l = matrix[0][0]
        r = matrix[n - 1][n - 1]

        while l < r:
            mid = (l + r) // 2

            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
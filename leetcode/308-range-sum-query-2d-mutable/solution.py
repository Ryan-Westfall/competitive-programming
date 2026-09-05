class BIT2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.bit = [[0] * (m + 1) for _ in range(n + 1)]

    def update(self, r, c, delta):
        i = r
        while i <= self.n:
            j = c
            while j <= self.m:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i

    def query(self, r, c):
        res = 0
        i = r

        while i > 0:
            j = c
            while j > 0:
                res += self.bit[i][j]
                j -= j & -j
            i -= i & -i

        return res


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        self.matrix = matrix
        self.BIT = BIT2D(n, m)

        for r in range(n):
            for c in range(m):
                self.BIT.update(r + 1, c + 1, matrix[r][c])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]

        self.matrix[row][col] = val
        self.BIT.update(row + 1, col + 1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        return (
            self.BIT.query(r2, c2)
            - self.BIT.query(r1 - 1, c2)
            - self.BIT.query(r2, c1 - 1)
            + self.BIT.query(r1 - 1, c1 - 1)
        )
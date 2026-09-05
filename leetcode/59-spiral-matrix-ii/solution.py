class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n
        spiral = [[0] * m for _ in range(n)]
        total = m*n

        def perimeter(r,c,val):
            spiral[r][c] = val

            if val == total:
                return

            newVal = val + 1
            if c + 1 < m and spiral[r][c+1] == 0 and (r == 0 or spiral[r-1][c] != 0):
                perimeter(r,c+1, newVal)
            elif r + 1 < n and spiral[r+1][c] == 0:
                perimeter(r+1, c, newVal)
            elif c - 1 >= 0 and spiral[r][c-1] == 0:
                perimeter(r,c-1, newVal)
            elif r - 1 >= 0 and spiral[r-1][c] == 0:
                perimeter(r-1,c, newVal)     

        perimeter(0,0,1)

        return spiral
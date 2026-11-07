
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n = len(picture)
        m = len(picture[0])

        rowCount = [0] * n
        colCount = [0] * m

        for r in range(n):
            for c in range(m):
                if picture[r][c] == 'B':
                    rowCount[r] += 1
                    colCount[c] += 1

        res = 0

        for r in range(n):
            for c in range(m):
                if picture[r][c] == 'B':
                    if rowCount[r] == 1 and colCount[c] == 1:
                        res += 1

        return res

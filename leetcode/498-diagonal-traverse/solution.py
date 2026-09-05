class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []

        goUp = True
        cur_row = cur_col = 0

        while len(mat) * len(mat[0]) != len(res):
            if goUp:
                while cur_col < len(mat[0]) and cur_row >= 0:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1

                if cur_col == len(mat[0]):
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row += 1

                goUp = False

            else:
                while cur_col >= 0 and cur_row < len(mat):
                    res.append(mat[cur_row][cur_col])
                    cur_col -= 1
                    cur_row += 1

                if cur_row == len(mat):
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1

                goUp = True

        return res
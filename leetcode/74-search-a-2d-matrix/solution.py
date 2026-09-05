class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def inRow(index):
            if target >= matrix[index][0] and target <= matrix[index][-1]:
                return 0
            elif target > matrix[index][-1]:
                return 1
            else: 
                return -1

        def bs(row):
            l,r = 0, len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if target > row[m]:
                    l = m + 1
                elif target < row[m]:
                    r = m - 1
                else:
                    return True
            return False

        rowL, rowR = 0, len(matrix) - 1
        while rowL <= rowR:
            rowM = (rowL + rowR) // 2
            print(rowM)
            cal = inRow(rowM)
            print(cal)
            if cal == 0:
                return bs(matrix[rowM])
            elif cal == 1:
                rowL = rowM + 1
            else:
                rowR = rowM - 1

        return False


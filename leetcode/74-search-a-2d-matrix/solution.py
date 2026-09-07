class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        rowLeft = 0
        colLeft = 0
        rowRight = n - 1
        colRight = m - 1

        while rowLeft <= rowRight or colLeft <= colRight:
            midRow = (rowRight+rowLeft) // 2
            midCol = (colRight+colLeft) // 2

            print(rowRight, colRight, rowLeft, colLeft, 'midRow', midRow, 'midCol', midCol, matrix[midRow][midCol])

            if target == matrix[midRow][midCol]:
                return True
            elif target < matrix[midRow][midCol]:
                print('cat')
                tempRowLeft = 0
                tempRowRight = midRow - 1
                while tempRowLeft <= tempRowRight:
                    tempRowMid = (tempRowLeft + tempRowRight) // 2
                    if matrix[tempRowMid][midCol] == target:
                        return True
                    elif target > matrix[tempRowMid][midCol]:
                        tempRowLeft = tempRowMid + 1
                    elif target < matrix[tempRowMid][midCol]:
                        tempRowRight = tempRowMid - 1
                tempColLeft = 0
                tempColRight = midCol - 1
                while tempColLeft <= tempColRight:
                    tempColMid = (tempColLeft + tempColRight) // 2
                    if matrix[midRow][tempColMid] == target:
                        return True
                    elif target > matrix[midRow][tempColMid]:
                        tempColLeft = tempColMid + 1
                    elif target < matrix[midRow][tempColMid]:
                        tempColRight = tempColMid - 1
                rowRight = midRow - 1
                colRight = midCol - 1
            elif target > matrix[midRow][midCol]:
                tempRowLeft = midRow + 1
                tempRowRight = n - 1
                while tempRowLeft <= tempRowRight:
                    tempRowMid = (tempRowLeft + tempRowRight) // 2
                    if matrix[tempRowMid][midCol] == target:
                        return True
                    elif target > matrix[tempRowMid][midCol]:
                        tempRowLeft = tempRowMid + 1
                    elif target < matrix[tempRowMid][midCol]:
                        tempRowRight = tempRowMid - 1
                tempColLeft = midCol + 1
                tempColRight = m - 1
                while tempColLeft <= tempColRight:
                    tempColMid = (tempColLeft + tempColRight) // 2
                    if matrix[midRow][tempColMid] == target:
                        return True
                    elif target > matrix[midRow][tempColMid]:
                        tempColLeft = tempColMid + 1
                    elif target < matrix[midRow][tempColMid]:
                        tempColRight = tempColMid - 1
                print('hi')
                rowLeft = midRow + 1
                colLeft = midCol + 1
            

        return False

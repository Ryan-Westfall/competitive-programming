class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        def toeplitz(r,c):
            compare = matrix[r][c]
            r += 1
            c += 1
            while r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
                if matrix[r][c] != compare:
                    return False

                r += 1
                c += 1
            
            return True
        
        for r in range(len(matrix)):
            if not toeplitz(r, 0):
                return False
            
        for c in range(len(matrix[0])):
            if not toeplitz(0, c):
                return False

        return True

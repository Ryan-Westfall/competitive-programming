class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROW, COL = len(matrix), len(matrix[0])
        visited = set()
        
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0 and (r,c) not in visited:
                    
                    for r2 in range(ROW):
                        # print("row",matrix)
                        if matrix[r2][c] != 0:
                            visited.add((r2,c))
                        matrix[r2][c] = 0
                        
                    for c2 in range(COL):
                        # print("col",matrix)
                        if matrix[r][c2] != 0:
                            visited.add((r,c2))
                        matrix[r][c2] = 0
                        
        return matrix
        
        
            
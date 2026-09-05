class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        regions = set([])
        def dfs(r,c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return False
            if board[r][c] == 'X' or (r,c) in regions:
                return True
            regions.add((r,c))

            return dfs(r+1,c) and dfs(r-1,c) and dfs(r,c+1) and dfs(r,c-1)


    
        for r in range(ROWS):
            for c in range(COLS):
                if not dfs(r,c):
                    regions.clear()
                if regions:
                    for i,j in regions:
                        board[i][j] = 'X'
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        col = set()
        negD = set()
        posD = set()
        board = [['.'] * n for i in range(n)]
        def backtracking(r):
            if r == n:
                copy = [''.join(board[i]) for i in range(n)]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r-c) in negD or (r+c) in posD:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                negD.add(r-c)
                posD.add(r+c)
                backtracking(r+1)
                board[r][c] = '.'
                col.remove(c)
                negD.remove(r-c)
                posD.remove(r+c)


        backtracking(0)
        return res
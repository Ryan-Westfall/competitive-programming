class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        squareSet = [[set() for _ in range(3)] for _ in range(3)]
        rowSet = [set() for _ in range(9)] 
        colSet = [set() for _ in range(9)]

        self.count = 0
        answer = None

        toProcess = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    toProcess.append((r,c))
                    continue
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[r // 3][c // 3].add(board[r][c])

        self.maxSeen = 0

        def solve(i):
            if i == len(toProcess):
                return True
            r, c = toProcess[i]
            possibles = {'1','2','3','4','5','6','7','8','9'} - (squareSet[r // 3][c // 3] | rowSet[r] | colSet[c])
            for possible in possibles:
                board[r][c] = possible
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[r // 3][c // 3].add(board[r][c])
                self.count += 1

                if solve(i+1):
                    return True

                rowSet[r].remove(board[r][c])
                colSet[c].remove(board[r][c])
                squareSet[r // 3][c // 3].remove(board[r][c])
                self.count -= 1
                board[r][c] = '.'

            return False

        solve(0)
  
        return answer


        
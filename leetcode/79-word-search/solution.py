class Solution:
    output = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                self.output = True
                return
            if r >= len(board) or r < 0 or c >= len(board[r]) or c < 0 or word[i] != board[r][c] or board[r][c] == '#':
                return
            
            board[r][c] = '#'
            dfs(r + 1, c, i + 1)
            dfs(r - 1, c, i + 1)
            dfs(r, c + 1, i + 1)
            dfs(r, c - 1, i + 1)
            board[r][c] = word[i]
            return

        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r,c,0)

        return self.output
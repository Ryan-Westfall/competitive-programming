class TicTacToe:

    def __init__(self, n: int):
        self.board = [[ 0 for i in range(n)] for j in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        def check_rows(col, player):
            for row_index in range(self.n):
                if self.board[row_index][col] != player:
                    return False
            return True
        
        def check_cols(row, player):
            for col_index in range(self.n):
                if self.board[row][col_index] != player:
                    return False
            return True
        
        def check_diagnol(player):
            for shared_index in range(self.n):
                if self.board[shared_index][shared_index] != player:
                    return False
            return True
        
        def check_reverse_diagnol(player):
            for shared_index in range(self.n):
                    if self.board[shared_index][(self.n - 1) - shared_index] != player:
                        return False
            return True

        self.board[row][col] = player
        if check_rows(col,player) or check_cols(row, player) or check_diagnol(player) or check_reverse_diagnol(player):
            return player
        
        # print(check_rows(col,player), check_cols(row, player), check_diagnol(player), check_reverse_diagnol(player) )
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
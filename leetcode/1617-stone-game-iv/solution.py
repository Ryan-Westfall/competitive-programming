class Solution:
    def winnerSquareGame(self, n: int) -> bool:


        @cache
        def bestMove(i):
            if i >= n:
                return False
            
            for take in range(1, int((n - i) ** .5) + 1):
                power = take * take
                if not bestMove(i + power):
                    return True

            return False


        return bestMove(0)



        
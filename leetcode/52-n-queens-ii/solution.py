class Solution:
    def totalNQueens(self, n: int) -> int:
        Qcols = [0] * n
        diagPos = [0] * (n + n - 1)
        diagNeg = [0] * (n + n - 1)

        self.valid = 0

        def backtrack(count):
            if count == n:
                self.valid += 1
                return

            for i in range(n):
                if Qcols[i] != 1 and diagPos[i+count] != 1 and diagNeg[count-i] != 1: 
                    Qcols[i] = 1
                    diagPos[i+count] = 1 
                    diagNeg[count-i] = 1
                    backtrack(count + 1)
                    Qcols[i] = 0
                    diagPos[i+count] = 0
                    diagNeg[count-i] = 0

        backtrack(0)

        return self.valid





        
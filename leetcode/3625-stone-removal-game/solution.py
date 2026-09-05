class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        stonesRemover = 10
        alice = True
        while n and stonesRemover:
            if stonesRemover > n:
                return not alice
            n -= stonesRemover
            stonesRemover -= 1
            alice = not alice

        return not alice

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + stoneValue[i]

        
        @cache
        def optimalMove(i):
            if i >= n + 1:
                return 0

            bestMove = float('-inf')
            for take in [1,2,3]:
                curVal = prefixSum[min(i+take,n)] - prefixSum[i]
                curOptimialMove = optimalMove(i+take)
                bestMove = max(bestMove, curVal - curOptimialMove)
            return bestMove

        bal = optimalMove(0)
        print(bal)

        if bal > 0:
            return "Alice"
        elif bal < 0:
            return "Bob"
        else:
            return "Tie"
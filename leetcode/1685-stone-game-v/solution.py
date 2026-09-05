class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # prefix
        prefixSum = [0] * (n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + stoneValue[i]
 
        @lru_cache(None)
        def maxScore(l,r):
            if l == r:
                return 0

            bestScore = leftSum =0
            total = prefixSum[r+1] - prefixSum[l]
            for mid in range(l, r):
                leftSum += stoneValue[mid]
                rightSum = total - leftSum
                if leftSum > rightSum:
                    right = maxScore(mid + 1, r)
                    bestScore = max(bestScore, rightSum + right)
                elif rightSum > leftSum:
                    left = maxScore(l, mid)
                    bestScore = max(bestScore, leftSum + left)
                else:
                    left = maxScore(l, mid)
                    right = maxScore(mid + 1, r)
                    bestScore = max(bestScore, rightSum + left, leftSum + right)   

            return bestScore

        return maxScore(0, n-1)
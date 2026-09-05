class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def maximizeGame(l, r):
            if l == r:
                return piles[l]

            curL = piles[l]
            left = maximizeGame(l + 1, r)

            curR = piles[r]
            right = maximizeGame(l, r - 1)

            return max(curL - left, curR - right)

        return maximizeGame(0, len(piles) - 1) > 0
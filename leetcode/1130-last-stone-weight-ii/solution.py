class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        target = sum(stones) // 2
        n = len(stones)
        
        @cache
        def dp(i, weight):
            if i == n:
                return weight

            # Take
            take = dp(i+1, weight + stones[i])

            # NoTake
            noTake = dp(i+1, weight)

            if abs(target - take) < abs(target - noTake):
                return take
            else:
                return noTake


        return abs(sum(stones) - dp(0, 0) - dp(0,0))


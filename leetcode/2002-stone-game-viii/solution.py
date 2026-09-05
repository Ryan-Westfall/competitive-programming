class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        @cache
        def move(i):
            if i == n - 1:
                return prefix[i]

            # Take the prefix ending at i
            take = prefix[i]

            # Opponent can then make the optimal move
            future = move(i + 1)

            # Either:
            # 1. Take prefix[i]
            # 2. Don't make this the optimal stopping point
            return max(take - future, move(i + 1))





        return move(1)
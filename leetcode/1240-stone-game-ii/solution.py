class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + piles[i]

        @cache
        def mostStones(i, m):
            if i >= n:
                return 0

            total = prefix[n] - prefix[i]
            best = 0

            for take in range(1, 2 * m + 1):
                if i + take > n:
                    break

                opponent = mostStones(i + take, max(m, take))
                best = max(best, total - opponent)

            return best

        return mostStones(0, 1)
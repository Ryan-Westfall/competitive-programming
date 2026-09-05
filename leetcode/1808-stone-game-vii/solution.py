class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[l][r] = maximum score difference for stones[l:r+1]
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total = prefix[r + 1] - prefix[l]

                # Remove left stone
                remove_left = total - stones[l] - dp[l + 1][r]

                # Remove right stone
                remove_right = total - stones[r] - dp[l][r - 1]

                dp[l][r] = max(remove_left, remove_right)

        return dp[0][n - 1]
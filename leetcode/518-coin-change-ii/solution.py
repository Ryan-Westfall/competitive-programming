from collections import defaultdict

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)

        # dp[i][curAmount] =
        # number of ways to make curAmount using coins[0...i]
        dp = [defaultdict(int) for _ in range(n)]

        # Base case: using only coins[0]
        curVal = 0
        while curVal <= amount:
            dp[0][curVal] = 1
            curVal += coins[0]

        for i in range(1, n):
            coin = coins[i]

            for curAmount in range(amount + 1):
                # Don't take coin
                dp[i][curAmount] = dp[i - 1][curAmount]

                # Take coin
                if curAmount >= coin:
                    dp[i][curAmount] += dp[i][curAmount - coin]

        return dp[n - 1][amount]
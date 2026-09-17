class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @cache
        def dp(i, t):
            if i == n or t == 0:
                return 0

            if t % 2 == 0:
                take = dp(i+1, t-1) - prices[i]
            else:
                take = dp(i+1, t-1) + prices[i]

            noTake = dp(i+1, t)


            return max(take, noTake)

        return dp(0, 4) 
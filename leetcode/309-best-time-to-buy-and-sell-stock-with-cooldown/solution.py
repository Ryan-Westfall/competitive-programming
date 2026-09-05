class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def maxMoney(i: int, holding: bool) -> int:
            if i >= n:
                return 0

            if holding:
                return max(
                    maxMoney(i + 1, True),              # hold
                    maxMoney(i + 2, False) + prices[i]  # sell
                )

            return max(
                maxMoney(i + 1, False),                 # skip
                maxMoney(i + 1, True) - prices[i]       # buy
            )

        return maxMoney(0, False)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        l = 0
        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                total += prices[r] - prices[l]
                l = r

        return total
        
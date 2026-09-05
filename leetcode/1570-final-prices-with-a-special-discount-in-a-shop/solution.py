class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and price <= stack[-1][0]:
                _, index = stack.pop()
                prices[index] -= price
            stack.append((price,i))
        return prices
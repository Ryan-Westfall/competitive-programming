class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:

        output = 0
        prices.sort(reverse=True)
        discounts.sort()

        for price in prices:
            discount = 0
            if discounts:
                discount = discounts.pop()

            output += price * (100 - discount) / 100

        return output
        
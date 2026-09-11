class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        total = 0

        for num in nums:
            width = num % 10
            d = str(num // 10)

            base = int(d[:width])
            exponent = int(d[width:])

            total += pow(base, exponent, MOD)

        return total % MOD
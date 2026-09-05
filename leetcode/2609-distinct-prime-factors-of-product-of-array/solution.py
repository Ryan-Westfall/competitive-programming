class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactors = set()

        for num in nums:
            for p in range(2, isqrt(num) + 1):
                while num % p == 0:
                    primeFactors.add(p)
                    num //= p
            if num > 1:
                primeFactors.add(num)

        return len(primeFactors)
from math import isqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for p in range(2, isqrt(n) + 1):
            if isPrime[p]:
                for multiple in range(p * p, n, p):
                    isPrime[multiple] = False

        return sum(isPrime)
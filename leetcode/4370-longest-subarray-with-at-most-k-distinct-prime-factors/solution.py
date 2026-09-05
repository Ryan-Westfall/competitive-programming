import math
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        numToPrimeFactorCount = defaultdict(set)
        
        def getPrimeNumsCount(n):
            factors = set()
            d = 2
            while d * d <= n:
                if n % d == 0:
                    factors.add(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        for num in nums:
            numToPrimeFactorCount[num] = getPrimeNumsCount(num)
            
        maxRange = 0
        l = 0
        curSet = set()
        prime_counts = defaultdict(int)
        
        for r in range(len(nums)):
            for prime in numToPrimeFactorCount[nums[r]]:
                prime_counts[prime] += 1
                curSet.add(prime)
                
            while len(curSet) > k:
                for prime in numToPrimeFactorCount[nums[l]]:
                    prime_counts[prime] -= 1
                    if prime_counts[prime] == 0:
                        curSet.remove(prime)
                l += 1
                
            maxRange = max(r - l + 1, maxRange)
            
        return maxRange

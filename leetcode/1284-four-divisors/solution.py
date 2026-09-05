class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            count = 0
            curSum = 0
            for i in range(1, isqrt(num) + 1):
                if num % i == 0:
                    count += 1
                    curSum += i
                    if num // i != i:
                        count += 1
                        curSum += num // i

            if count == 4:
                total += curSum

        return total


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm(a, b)

        def validMagical(x):
            count = x // a + x // b - x // lcm
            return count >= n

        left = 1
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2

            if validMagical(mid):
                right = mid
            else:
                left = mid + 1

        return left % (10 ** 9 + 7)
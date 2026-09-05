class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        l = 0
        r = n

        while l <= r:
            target = l**2 + r**2

            if target == c:
                return True
            elif target < c:
                l += 1
            else:
                r -= 1

        return False


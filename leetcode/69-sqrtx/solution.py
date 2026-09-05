class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x
        close = 0
        while l <= r:
            m = (l + r) // 2
            if m * m < x:
                close = m
                l = m + 1
            if m * m > x:
                r = m - 1
            if m * m == x:
                return m

        return close

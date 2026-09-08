class Solution:
    def countCommas(self, n: int) -> int:
        nLen = len(str(n))
        total = ((nLen-1) // 3) * n
        cur = 1
        prev = 0
        minusCount = (nLen-1) // 3
        while cur < n:
            cur *= 1000
            total -= ((cur-1) - prev) * minusCount
            minusCount -= 1
            prev = cur - 1

        return total

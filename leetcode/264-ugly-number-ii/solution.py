class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        while len(ugly) != n:
            nextVal = min(ugly[i2] * 2,ugly[i3] * 3,ugly[i5] * 5)
            ugly.append(nextVal)

            if ugly[i2] * 2 == nextVal:
                i2 += 1

            if ugly[i3] * 3 == nextVal:
                i3 += 1

            if ugly[i5] * 5 == nextVal:
                i5 += 1

        return ugly[-1]

    
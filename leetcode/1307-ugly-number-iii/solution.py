class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a,b)
        ac = math.lcm(a,c)
        bc = math.lcm(b,c)
        abc = math.lcm(a,b,c)

        def validUgly(x):
            # print(x)
            total = 0

            total += x // a
            total += x // b
            total += x // c

            # print("total",total)

            total -= x // ab
            total -= x // ac
            total -= x // bc
            # print("total",total)

            total += x // abc

            # print("total",total)

            print(total >= n)

            return total >= n


        # print(validUgly(7))
        l = 1
        r = n * min(a,b,c)
        while l < r:

            mid = (l + r) // 2
            if validUgly(mid):
                r = mid
            else:
                l = mid + 1

        return l



        


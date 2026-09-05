class Solution:
    def magicalString(self, n: int) -> int:
        magical = "122"
        i = len(magical) - 1
        prev = '1'

        while i < n:
            multiplier = magical[i]
            magical += (prev * int(multiplier))
            i += 1

            if prev == '1':
                prev = '2'
            else:
                prev = '1'


        return magical[:n].count('1')
        
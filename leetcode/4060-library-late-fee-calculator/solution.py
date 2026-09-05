class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        res = 0
        for late in daysLate:
            if late == 1:
                res += 1
            elif late >= 2 and late <= 5:
                res += 2 * late
            else:
                res += 3 * late

        return res
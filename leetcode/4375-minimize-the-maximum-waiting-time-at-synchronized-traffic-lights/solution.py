class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxLight = max(lights)

        def can(P):
            for t in arrivalTime:
                r = t % period
                wait = period - r

                if wait > P and maxLight <= r:
                    return False

            return True

        lo, hi = 0, period

        while lo < hi:
            mid = (lo + hi) // 2

            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
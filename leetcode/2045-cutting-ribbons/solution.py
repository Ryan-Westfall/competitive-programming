class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def canCut(toCut):
            cut = 0

            for ribbon in ribbons:
                cut += ribbon // toCut

            return cut >= k

        l = 1
        r = sum(ribbons) // k

        while l <= r:
            mid = (l + r) // 2

            if canCut(mid):
                l = mid + 1
            else:
                r = mid - 1


        return r
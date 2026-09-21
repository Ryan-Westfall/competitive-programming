class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def can_make(k):
            if k == 1:
                flips0 = flips1 = 0

                for i, c in enumerate(s):
                    expected0 = str(i % 2)
                    expected1 = str(1 - i % 2)

                    flips0 += c != expected0
                    flips1 += c != expected1

                return min(flips0, flips1) <= numOps

            flips = 0
            i = 0

            while i < n:
                j = i

                while j < n and s[j] == s[i]:
                    j += 1

                length = j - i
                flips += length // (k + 1)

                if flips > numOps:
                    return False

                i = j

            return True

        lo, hi = 1, n

        while lo < hi:
            mid = (lo + hi) // 2

            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
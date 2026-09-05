class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        def isBloomDay(day):
            flowers = 0
            group = 0

            for bloom in bloomDay:
                if day >= bloom:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    group += 1
                    flowers = 0

            return group >= m

        l = min(bloomDay)
        r = max(bloomDay)

        while l < r:
            mid = (l + r) // 2

            if isBloomDay(mid):
                r = mid
            else:
                l = mid + 1

        return l
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        n = len(sweetness)

        def isValid(x):
            pieces = 0
            curSum = 0

            for num in sweetness:
                curSum += num

                if curSum >= x:
                    pieces += 1
                    curSum = 0

            return pieces >= k + 1

        l = min(sweetness)
        r = sum(sweetness)

        while l < r:
            mid = math.ceil(l + (r - l) / 2)
            if isValid(mid):
                l = mid
            else:
                r = mid - 1

        return l
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def minWeightToShip(x):
            curDay = 1
            curSum = 0
            for weight in weights:
                curSum += weight
                if curSum > x:
                    curDay += 1
                    curSum = weight
                     
                if curDay > days:
                    return False

            return True

        l=max(weights)
        r=sum(weights)

        while l < r:
            mid = (l+r) // 2
            if minWeightToShip(mid):
                r = mid
            else:
                l = mid + 1

        return r
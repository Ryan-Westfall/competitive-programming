class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def validK(k):

            curH = 0
            for pile in piles: 
                curH += int(math.ceil(pile/k))
                if curH > h:
                    return False

            return True

        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r) // 2
            if validK(mid):
                r = mid
            else:
                l = mid + 1

        return r
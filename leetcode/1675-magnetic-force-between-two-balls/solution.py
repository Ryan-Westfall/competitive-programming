class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0] + 1

        def invalidForce(x):
            last = position[0]
            balls = 1

            for p in position[1:]:
                if p - last >= x:
                    last = p
                    balls += 1

                    if balls == m:
                        return False

            return True

        while l < r:
            mid = (l+r) // 2
            if invalidForce(mid):
                r = mid
            else:
                l = mid + 1

        return r-1
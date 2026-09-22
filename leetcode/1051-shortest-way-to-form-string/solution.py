class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        targetI = 0
        prevI = -1
        ans = 0
        while targetI < len(target):
            if targetI == prevI:
                return -1

            prevI = targetI

            for c in source:
                if targetI < len(target) and target[targetI] == c:
                    targetI += 1

            ans += 1

        return ans


        
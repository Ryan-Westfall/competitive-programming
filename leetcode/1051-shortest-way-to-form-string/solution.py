class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        targetI = 0
        ans = 0
        while targetI < len(target):
            prev = targetI

            for c in source:
                if targetI < len(target) and target[targetI] == c:
                    targetI += 1

            if prev == targetI:
                return -1

            ans += 1

        return ans


        
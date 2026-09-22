from functools import cache

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n = len(source)

        @cache
        def dp(i, c):
            if i == n:
                return -1

            if source[i] == c:
                return i

            return dp(i + 1, c)

        ans = 1
        i = 0

        for c in target:
            pos = dp(i, c)

            if pos == -1:
                if dp(0, c) == -1:
                    return -1

                ans += 1
                i = dp(0, c)
            else:
                i = pos

            i += 1

        return ans
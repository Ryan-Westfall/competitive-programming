class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def numOfWays(i):
            if i >= n:
                return 1

            ways = 0
            # Can Take 2
            if (i + 1 < n) and ((s[i] == '1') or (s[i] == '2' and s[i+1] in {'0','1','2','3','4','5','6'})):
                ways += numOfWays(i + 2) + numOfWays(i+1)
            # Take 1
            elif s[i] != '0':
                ways += numOfWays(i+1)

            return ways

        return numOfWays(0)
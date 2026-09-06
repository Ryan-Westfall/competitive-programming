class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dp(sI, tI):
            if tI == len(t):
                return 1

            if sI == len(s):
                return 0

            ways = 0
            if s[sI] == t[tI]:
                ways += dp(sI + 1, tI + 1)

            ways += dp(sI + 1, tI)

            return ways
            

        return dp(0,0)
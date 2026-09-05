class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            firstMatches = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # zero occurrences, or eat one char and stay on the same '*'
                return dp(i, j + 2) or (firstMatches and dp(i + 1, j))

            return firstMatches and dp(i + 1, j + 1)

        result = dp(0, 0)
        return result
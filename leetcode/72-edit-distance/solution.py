class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def dp(i, j):
            if i == n and j == m:
                return 0

            if i == n:
                return m - j

            if j == m:
                return n - i

            if word1[i] == word2[j]:
                return dp(i+1, j+1)

            return min(
                dp(i+1, j) + 1,       # delete
                dp(i, j+1) + 1,       # insert
                dp(i+1, j+1) + 1      # replace
            )


        return dp(0,0)
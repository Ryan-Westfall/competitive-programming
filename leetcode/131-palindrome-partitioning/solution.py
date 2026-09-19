class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        # pal[l][r] = s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length == 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        ans = []

        def dfs(i):
            if i == n:
                ans.append(cur[:])
                return

            for r in range(i, n):
                if pal[i][r]:
                    cur.append(s[i:r + 1])
                    dfs(r + 1)
                    cur.pop()

        cur = []
        dfs(0)

        return ans
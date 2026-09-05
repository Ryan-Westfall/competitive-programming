class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        dp = [[0] * m for _ in range(n)]
        counter = defaultdict(list)
        mostSeen = 0

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(
                            dp[r - 1][c],
                            dp[r][c - 1],
                            dp[r - 1][c - 1]
                        )

                    counter[dp[r][c]].append((r, c))
                    mostSeen = max(mostSeen, dp[r][c])

        # Coordinates with dp >= k
        min_r = n
        max_r = -1
        min_c = m
        max_c = -1

        for k in range(mostSeen, 0, -1):

            # Add all coordinates whose dp == k.
            # These can be used for every smaller square too.
            for r, c in counter[k]:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)

            # If bottom-right corners are k rows apart,
            # the squares cannot overlap.
            if max_r - min_r >= k or max_c - min_c >= k:
                return k * k

        return 0
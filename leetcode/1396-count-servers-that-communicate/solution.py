class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        freqR = defaultdict(int)
        freqC = defaultdict(int)

        n = len(grid)
        m = len(grid[0])
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    freqR[r] += 1
                    freqC[c] += 1
                    count += 1

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    if freqR[r] == 1 and freqC[c] == 1:
                        count -= 1

        return count

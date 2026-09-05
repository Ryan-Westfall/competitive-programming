class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort(reverse=True)
        n = len(blocks)

        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def minTime(curDone, workers):
            if curDone == n:
                return 0
            if workers == 0:
                return float('inf')
            if curDone + workers >= n:
                return blocks[curDone]

            if dp[curDone][workers] != -1:
                return dp[curDone][workers]

            workHere = max(
                blocks[curDone],
                minTime(curDone + 1, workers - 1)
            )

            splitHere = split + minTime(
                curDone,
                min(2 * workers, n - curDone)
            )

            dp[curDone][workers] = min(workHere, splitHere)
            return dp[curDone][workers]

        return minTime(0, 1)
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            memo = {}

            def dfs(i):
                if i == 0:
                    return max(0, nums[0])

                if i in memo:
                    return memo[i]

                memo[i] = max(
                    0,
                    nums[i],
                    nums[i] + dfs(i - 1)
                )

                return memo[i]

            return max(dfs(i) for i in range(len(nums)))

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        best = kadane(arr * 2)

        if total > 0:
            best += (k - 2) * total

        return best % MOD
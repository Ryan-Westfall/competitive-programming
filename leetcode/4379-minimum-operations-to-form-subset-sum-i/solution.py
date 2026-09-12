from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n = len(nums)

        indexValidNums = defaultdict(dict)

        for i in range(n):
            cur = nums[i]
            multOps = 0

            while cur <= sum:
                divCur = cur
                divOps = 0

                while divCur > 0:
                    indexValidNums[i][divCur] = min(
                        indexValidNums[i].get(divCur, float('inf')),
                        multOps + divOps
                    )

                    divCur //= 2
                    divOps += 1

                cur *= 2
                multOps += 1

            divCur = nums[i]
            divOps = 0

            while divCur > 0:
                indexValidNums[i][divCur] = min(
                    indexValidNums[i].get(divCur, float('inf')),
                    divOps
                )

                divCur //= 2
                divOps += 1

        # dp[remaining] = minimum operations to form remaining
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0

        for i in range(n):
            # Copy so nums[i] can only be used once
            newDp = dp.copy()

            for remaining in range(sum + 1):
                if dp[remaining] == float('inf'):
                    continue

                for num, moves in indexValidNums[i].items():
                    if remaining + num <= sum:
                        newDp[remaining + num] = min(
                            newDp[remaining + num],
                            dp[remaining] + moves
                        )

            dp = newDp

        return -1 if dp[sum] == float('inf') else dp[sum]
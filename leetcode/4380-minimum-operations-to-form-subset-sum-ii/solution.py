from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n = len(nums)

        indexValidNums = defaultdict(dict)

        for i in range(n):
            start = nums[i]

            queue = deque([(start, 0)])
            visit = {start}

            while queue:
                curNode, steps = queue.popleft()

                if curNode <= sum:
                    indexValidNums[i][curNode] = steps

                # mult2
                multNode = curNode * 2
                if multNode <= 2 * sum and multNode not in visit:
                    visit.add(multNode)
                    queue.append((multNode, steps + 1))

                # div2
                divNode = curNode // 2
                if divNode not in visit:
                    visit.add(divNode)
                    queue.append((divNode, steps + 1))



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
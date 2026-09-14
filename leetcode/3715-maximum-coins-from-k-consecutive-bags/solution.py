from typing import List
from bisect import bisect_right


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:

        def solve(coins):
            coins.sort()

            n = len(coins)

            # prefix[i] = total coins in intervals [0, i)
            prefix = [0] * (n + 1)

            for i, (l, r, c) in enumerate(coins):
                prefix[i + 1] = prefix[i] + (r - l + 1) * c

            # Used to find the last interval completely inside our window
            rights = [r for l, r, c in coins]

            ans = 0

            for i in range(n):
                l, r, c = coins[i]

                # Try a window of length k starting at l
                end = l + k - 1

                # Last interval whose right endpoint <= end
                j = bisect_right(rights, end) - 1

                # Sum all completely covered intervals from i through j
                total = prefix[j + 1] - prefix[i]

                # There may be one partially covered interval after j
                if j + 1 < n:
                    next_l, next_r, next_c = coins[j + 1]

                    if next_l <= end:
                        total += (end - next_l + 1) * next_c

                ans = max(ans, total)

            return ans

        # Check windows whose LEFT edge is an interval boundary
        ans = solve(coins)

        # Now check windows whose RIGHT edge is an interval boundary.
        # Flip the coordinates so this becomes the same problem.
        flipped = [
            [-r, -l, c]
            for l, r, c in coins
        ]

        ans = max(ans, solve(flipped))

        return ans
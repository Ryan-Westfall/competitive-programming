class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")

        # best[i] = shortest target-sum subarray entirely in arr[0:i]
        best = [INF] * (n + 1)

        ans = INF
        left = 0
        cur = 0

        for right in range(n):
            cur += arr[right]

            while cur > target:
                cur -= arr[left]
                left += 1

            best[right + 1] = best[right]

            if cur == target:
                length = right - left + 1

                # Previous non-overlapping subarray must end before `left`
                if best[left] != INF:
                    ans = min(ans, length + best[left])

                best[right + 1] = min(best[right + 1], length)

        return -1 if ans == INF else ans
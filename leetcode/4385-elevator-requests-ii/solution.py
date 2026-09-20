class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        requests.append(start)
        requests.sort()
        n = len(requests)

        @lru_cache(maxsize=10000)
        def dp(l, r, side):
            if l == 0 and r == n - 1:
                return 0

            waiting = n - (r - l + 1)
            pos = requests[l] if side == 0 else requests[r]

            ans = float('inf')

            # Serve next request on the left
            if l > 0:
                ans = min(
                    ans,
                    waiting * (pos - requests[l - 1])
                    + dp(l - 1, r, 0)
                )

            # Serve next request on the right
            if r + 1 < n:
                ans = min(
                    ans,
                    waiting * (requests[r + 1] - pos)
                    + dp(l, r + 1, 1)
                )

            return ans

        start_idx = requests.index(start)
        return dp(start_idx, start_idx, 0)
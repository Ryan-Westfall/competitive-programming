class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        full = (1 << m) - 1

        @cache
        def dp(last, mask):
            # Earliest time to have served exactly `mask`, ending at request `last`.
            if mask == (1 << last):
                arrive, floor = requests[last]
                return max(arrive, abs(start - floor))

            arrive, floor = requests[last]
            prev_mask = mask ^ (1 << last)
            best = float("inf")
            for p in range(m):
                if prev_mask & (1 << p):
                    t = dp(p, prev_mask) + abs(requests[p][1] - floor)
                    if t < arrive:
                        t = arrive
                    if t < best:
                        best = t
            return best

        return min(dp(i, full) for i in range(m))
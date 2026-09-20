class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        requests.append(start)
        requests.sort()
        n = len(requests)

        @lru_cache(maxsize=10000)
        def dp(l, r, side):
            if l == 0 and r == n-1:
                return 0

            if side == 1: # On Right Side
                # GoRight
                if r < n-1:
                    distance = requests[r+1] - requests[r]
                    cost = ((n - (r-l+1)) * distance)
                    right = cost + dp(l, r+1, 1)
                else:
                    right = float('inf')

                # GoLeft
                if l > 0:
                    distance = requests[r] - requests[l-1]
                    cost = ((n - (r-l+1)) * distance)
                    left = cost + dp(l-1, r, 0)
                else:
                    left = float('inf')

                return min(right, left)

            else: # On Left Side
                # GoRight
                if r < n-1:
                    distance = requests[r+1] - requests[l]
                    cost = ((n - (r-l+1)) * distance)
                    right = cost + dp(l, r+1, 1)
                else:
                    right = float('inf')

                # GoLeft
                if l > 0:
                    distance = requests[l] - requests[l-1]
                    cost = ((n - (r-l+1)) * distance)
                    left = cost + dp(l-1, r, 0)
                else:
                    left = float('inf')

                # print('l',l,'r',r,'left',left,'right',right)

                return min(right, left)

        s = requests.index(start)
        return dp(s, s, 0)

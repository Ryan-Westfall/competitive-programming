class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        # Precompute (LCM of subset, parity of subset size)
        subsets = []

        for mask in range(1, 1 << n):
            curr_lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    curr_lcm = math.lcm(curr_lcm, coins[i])
                    bits += 1

            subsets.append((curr_lcm, bits))

        # Given x, how many distinct valid amounts <= x?
        def count(x):
            ans = 0

            for curr_lcm, bits in subsets:
                if curr_lcm > x:
                    continue

                if bits % 2 == 1:
                    ans += x // curr_lcm
                else:
                    ans -= x // curr_lcm

            return ans

        # Binary search for the smallest x with count(x) >= k
        l = k
        r = min(coins) * k

        while l < r:
            mid = (l + r) // 2

            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
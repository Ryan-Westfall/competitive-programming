class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count(prefix):
            curr = prefix
            next_prefix = prefix + 1
            total = 0

            while curr <= n:
                total += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10

            return total

        curr = 1
        k -= 1

        while k > 0:
            steps = count(curr)

            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
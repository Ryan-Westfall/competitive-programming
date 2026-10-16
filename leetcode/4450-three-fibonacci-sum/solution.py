class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        prev, curr = 0, 1

        while curr < n:
            nxt = prev + curr

            if prev + curr + nxt == n:
                return True

            prev, curr = curr, nxt

        return False
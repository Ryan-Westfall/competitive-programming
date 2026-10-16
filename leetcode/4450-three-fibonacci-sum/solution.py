class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        dp = [0,1]
        while dp[-1] < n:
            nextVal = dp[-1] + dp[-2]
            if dp[-1] + dp[-2] + nextVal == n:
                return True

            dp.append(nextVal)

        return False

        
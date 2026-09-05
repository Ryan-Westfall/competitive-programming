class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = {}
        def helper(count, paste):
            if n == count:
                return 0
            if count > n:
                return 1000

            if (count, paste) in memo:
                return memo[(count,paste)]

            # Paste
            res1 = 1 + helper(count + paste, paste)

            # Copy and Paste
            res2 = 2 + helper(count + count, count)

            memo[(count,paste)] = min(res1, res2)
            return memo[(count,paste)]



        if n == 1:
            return 0
        return 1 + helper(1,1)
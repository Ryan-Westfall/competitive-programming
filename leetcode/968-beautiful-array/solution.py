class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {}

        def dfs(size):
            if size == 1:
                return [1]

            if size in memo:
                return memo[size]

            odds = dfs((size + 1) // 2)
            evens = dfs(size // 2)

            ans = []

            for x in odds:
                ans.append(2 * x - 1)

            for x in evens:
                ans.append(2 * x)

            memo[size] = ans
            return ans

        return dfs(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dfs(m, n, memo):
            key = str(m) + ',' + str(n)
            if key in memo:
                return memo[key]
            
            if m == 1 or n == 1:
                return 1

            memo[key] = dfs(m-1,n,memo) + dfs(m,n-1,memo)
            return memo[key]
        
        return dfs(m,n,memo)
                
                
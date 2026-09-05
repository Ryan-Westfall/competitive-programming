class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(index, curAmount):
            if index == len(coins):
                return 1 if curAmount == 0 else 0 

            take = 0
            if coins[index] <= curAmount:
                take = dfs(index, curAmount - coins[index])
            skip = dfs(index + 1, curAmount)

            return take + skip



        return dfs(0, amount)
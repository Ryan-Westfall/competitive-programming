class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        
        def dfs(index):
            if index >= len(nums):
                return 0

            if (index) in self.memo:
                return self.memo[(index)]

            skip = dfs(index + 1)
            rob =  nums[index] + dfs(index + 2)
            self.memo[(index)] = max(skip,rob)
            return max(skip,rob)

        return dfs(0)
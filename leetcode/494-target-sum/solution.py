class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        
        def dfs(index, curSum):
            if index == len(nums):
                return 1 if curSum == target else 0

            if (index, curSum) in self.memo:
                return self.memo[(index, curSum)]

            res = dfs(index + 1, curSum + (nums[index])) + dfs(index + 1, curSum + (-nums[index]))
            self.memo[(index, curSum)] = res
            return res

        return dfs(0, 0)
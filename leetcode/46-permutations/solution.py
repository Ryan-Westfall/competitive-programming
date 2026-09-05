class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(curArr):
            if len(curArr) == len(nums):
                output.append(curArr.copy())
                return

            for i in nums:
                if i not in curArr:
                    curArr.append(i)
                    dfs(curArr)
                    curArr.pop()

        dfs([])
        return output
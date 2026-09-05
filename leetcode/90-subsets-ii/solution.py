class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        def dfs(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return

            # All subsets that include nums[inded]
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, subset)



        dfs(0, [])
        return result
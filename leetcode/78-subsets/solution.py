class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        
        def backtrack(cur, i):
            if i == n:
                return [cur[:]]

            # noTake
            noTake = backtrack(cur, i+1)
            
            # take
            cur.append(nums[i])
            take = backtrack(cur, i+1)
            cur.pop()

            return noTake + take

        return backtrack([], 0)

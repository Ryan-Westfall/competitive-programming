class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def minJumps(i):
            if i + nums[i] >= n - 1:
                return 1

            minJump = float('inf')
            for jump in range(1, nums[i]+1):
                minJump = min(minJump, minJumps(i+jump) + 1)

            return minJump

        if len(nums) == 1:
            return 0

        return minJumps(0)



class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def dp(left, right):
            if left + 1 == right:
                return 0
            best = 0
            for i in range(left + 1, right):
                best = max(best,
                    nums[left] * nums[i] * nums[right]
                    + dp(left, i) + dp(i, right))
            return best

        return dp(0, n - 1)
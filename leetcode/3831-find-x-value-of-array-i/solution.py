class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        @cache
        def dp(i, r):
            if i == n:
                return 0

            # Start with [nums[i]]
            count = 1 if nums[i] % k == r else 0

            # Extend a subarray starting at i+1
            for next_r in range(k):
                if (nums[i] * next_r) % k == r:
                    count += dp(i + 1, next_r)

            return count

        ans = [0] * k

        for i in range(n):
            for r in range(k):
                ans[r] += dp(i, r)

        return ans
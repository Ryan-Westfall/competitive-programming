class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for d in range(-1, n):
            if d == -1:
                arr = nums
            else:
                arr = nums[:d] + nums[d + 1:]

            m = len(arr)

            if m < 2:
                continue

            prefix = [0] * m
            prefix[0] = arr[0]

            for i in range(1, m):
                prefix[i] = math.gcd(prefix[i - 1], arr[i])

            suffix = [0] * m
            suffix[m - 1] = arr[m - 1]

            for i in range(m - 2, -1, -1):
                suffix[i] = math.gcd(suffix[i + 1], arr[i])

            score = 0

            for i in range(m - 1):
                if prefix[i] == suffix[i + 1]:
                    score += 1

            ans = max(ans, score)

        return ans
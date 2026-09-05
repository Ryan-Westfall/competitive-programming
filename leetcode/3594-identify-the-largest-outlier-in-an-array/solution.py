class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = sum(nums)

        ans = float("-inf")

        for x in count:
            count[x] -= 1

            remaining = total - x

            if remaining % 2 == 0 and count[remaining // 2] > 0:
                ans = max(ans, x)

            count[x] += 1

        return ans
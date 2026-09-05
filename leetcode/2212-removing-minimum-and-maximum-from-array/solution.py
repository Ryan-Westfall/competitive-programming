class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIndex = 0
        maxIndex = 0

        for i in range(n):
            if nums[i] < nums[minIndex]:
                minIndex = i

            if nums[i] > nums[maxIndex]:
                maxIndex = i

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        return min(
            right + 1,          # remove both from left
            n - left,           # remove both from right
            left + 1 + n - right # remove one from each
        )
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        left = 0
        maxSub = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1
            maxSub = max(maxSub, right - left + 1)

        return maxSub

        
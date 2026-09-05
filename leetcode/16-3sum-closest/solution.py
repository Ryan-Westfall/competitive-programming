class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        result = 0

        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                delta = target - (nums[i] + nums[l] + nums[r])
                # print(nums[i], nums[l], nums[r])
                # print(delta, nums[i] + nums[l] + nums[r])
                if abs(delta) < closest:
                    closest = abs(delta)
                    result = nums[i] + nums[l] + nums[r]
                if delta > 0:
                    l += 1
                else:
                    r -= 1

        return result
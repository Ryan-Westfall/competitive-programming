class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        output = 0
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            output += len(stack)

        return output
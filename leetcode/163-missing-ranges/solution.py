class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        curLower = lower
        nums.append(upper + 1)
        result = []
        for num in nums:
            if num - curLower >= 1:
                result.append([curLower, num - 1])

            curLower = num + 1

        return result

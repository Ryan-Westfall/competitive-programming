class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.append(lower - 1)
        nums.append(upper + 1)
        nums.sort()
        

        missingRanges = []
        for num1, num2 in pairwise(nums):
            if num2 - num1 > 1:
                missingRanges.append([num1+1, num2-1])

        output = []
        
        for x1, x2 in missingRanges:
            if x1 < lower and x2 >= lower:
                output.append([lower,x2])
            elif x1 >= lower and x2 <= upper:
                output.append([x1,x2])
            elif x1 < upper and x2 >= upper:
                output.append([x1,upper])
                
        return output
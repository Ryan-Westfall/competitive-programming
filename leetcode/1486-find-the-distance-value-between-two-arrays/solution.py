class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        passing = 0
        for num1 in arr1:
            passed = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    passed = False
                    break
            if passed:
                passing += 1


        return passing
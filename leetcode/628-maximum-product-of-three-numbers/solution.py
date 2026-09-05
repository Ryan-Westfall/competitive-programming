class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        smallest = float('inf')
        small = float('inf')

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

            if num < smallest:
                small = smallest
                smallest = num
            elif num < small:
                small = num

        return max(first * second * third, first * small * smallest)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        large = 0

        for num in nums:
            if num > largest:
                large = largest
                largest = num
            elif num > large:
                large = num

        return (large - 1) * (largest - 1)
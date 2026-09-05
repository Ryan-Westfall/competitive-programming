class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        # Create prefix sum arrays of size n + 1 padded with a leading 0
        evenPreSum = [0] * (n + 1)
        oddPreSum = [0] * (n + 1)

        # Build the prefix sums
        for i, num in enumerate(nums):
            # Carry over the previous sums
            evenPreSum[i + 1] = evenPreSum[i]
            oddPreSum[i + 1] = oddPreSum[i]
            
            # Add the current number to the appropriate prefix sum
            if i % 2 == 0:
                evenPreSum[i + 1] += num
            else:
                oddPreSum[i + 1] += num

        fairNumbers = 0
        
        # Iterate through the array using 0-based indexing for the element to remove
        for i in range(n):
            # Sums BEFORE the removed element remain unchanged
            # Sums AFTER the removed element swap categories (evens become odds, odds become evens)
            
            evenSum = evenPreSum[i] + (oddPreSum[n] - oddPreSum[i + 1])
            oddSum = oddPreSum[i] + (evenPreSum[n] - evenPreSum[i + 1])

            if evenSum == oddSum:
                fairNumbers += 1

        return fairNumbers
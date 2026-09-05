class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def increasingSubarray(arr):
            return len(arr) == k and all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

        for i in range(len(nums)):
            if increasingSubarray(nums[i:i+k]) and increasingSubarray(nums[i+k:i+k+k]):
                return True
                    
        return False       
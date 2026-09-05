class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(n):
            if n < 2:
                return False

            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False

            return True

        left = 0
        while left < len(nums):
            if isPrime(nums[left]):
                break
            left += 1

        right = len(nums) - 1
        while right >= 0:
            if isPrime(nums[right]):
                break
            right -= 1

        return right - left

            
        
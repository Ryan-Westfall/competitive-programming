class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # k % sums == 0'

        hashmap = {0 : -1} # remainder: index
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in hashmap:
                hashmap[r] = i
            elif i - hashmap[r] > 1:
                return True

        return False

        
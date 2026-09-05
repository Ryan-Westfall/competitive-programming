class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        prefixSum = 0
        result = 0

        for i, v in enumerate(nums):
            prefixSum += v

            if prefixSum - k in hashmap:
                result += hashmap[prefixSum - k]
            
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1

        return result

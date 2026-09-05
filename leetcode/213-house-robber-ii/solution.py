class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHouse(nums):
            rob1,rob2 = 0,0
            for i in nums:
                newRob = max(rob1+i, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        
        return max(robHouse(nums[1:]), robHouse(nums[:-1]), nums[0])
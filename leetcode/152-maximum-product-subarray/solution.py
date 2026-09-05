class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1: return 0
        _max = cur_max = cur_min = nums[0]
        
        for n in nums[1:]:
            tmp = cur_max
            cur_max = max(cur_max*n, cur_min*n,n)
            cur_min = min(tmp*n, cur_min*n,n)
            _max = max(_max, cur_max)
            
        return _max
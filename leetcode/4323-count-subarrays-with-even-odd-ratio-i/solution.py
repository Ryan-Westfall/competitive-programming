class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        ans = 0 

        for l in range(len(nums)):
            even = 0
            odd = 0

            for r in range(l, len(nums)):
                if nums[r] % 2 == 0:
                    even += 1
                else:
                    odd += 1

                if odd > 0 and even * b <= odd * a:
                    ans += 1

            
        return ans
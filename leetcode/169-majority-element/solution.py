class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res
        


        # n = len(nums)
        # counter = defaultdict(int)

        # for num in nums:
        #     counter[num] += 1
        #     if counter[num] > n//2:
        #         return num
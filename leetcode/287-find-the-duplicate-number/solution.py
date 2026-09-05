class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0

        while f == 0 or f != s:
            f = nums[nums[f]]
            s = nums[s]
            # print(f,s)
        # print(f, s)
        
        newS = 0
        while newS != s:
            newS = nums[newS]
            s = nums[s]
            # print(newS,s)


        return s
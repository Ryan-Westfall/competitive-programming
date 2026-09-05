class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        totalSum = 0

        # def traverseLeftAndRight(index):
        #     # Go Left
        #     copiedList = list(nums)
        #     curr = index
        #     direction = 'left'
        #     while curr >= 0 and curr <= len(nums) - 1:
        #         curr -= 1 if direction == 'left' else curr += 1
        #         if nums[curr] == 0:
        #             pass
        #         else:
        #             nums[curr] -= 1
        #             direction = 'right'

        #     # Go Right
        #     copiedList = list(nums)
        #     curr = index
        #     direction = 'right'
        #     while curr >= 0 and curr <= len(nums) - 1:
        #         curr -= 1 if direction == 'left' else curr += 1
        #         if nums[curr] == 0:
        #             pass
        #         else:
        #             nums[curr] -= 1
        #             direction = 'right'


        # if left == right return 2
        # if left + 1 == right return 1
        # if left == right + 1 return 1
        # else return 0

        for i in range(len(nums)):
            if nums[i] == 0:
                left = sum(nums[:i])
                right = sum(nums[i:])
                if left == right:
                    totalSum += 2
                elif left + 1 == right:
                    totalSum += 1
                elif left == right + 1:
                    totalSum += 1
                    
        return totalSum

        

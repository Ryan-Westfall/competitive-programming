class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            newIndex = abs(nums[i]) - 1
            if nums[newIndex] > 0:
                nums[newIndex] *= -1

        output = []
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i + 1)


        return output






        # Approach 2 Counting
        
        # count = [0] * len(nums)

        # for num in nums:
        #     count[num - 1] += 1

        # # print(count)

        # output = []
        # for i in range(len(count)):
        #     if count[i] == 0:
        #         output.append(i + 1)

        # return output


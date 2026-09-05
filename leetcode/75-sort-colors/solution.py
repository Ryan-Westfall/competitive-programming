class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        index = 0
        for i in range(3):
            for j in range(hashmap[i]):
                nums[index] = i
                index += 1



        # def quicksort(left, right):
        #     if left < right:
        #         index = partition(left,right)
        #         quicksort(left, index - 1)
        #         quicksort(index + 1, right)

        # def partition(left, right):
        #     pivot = nums[right]
        #     i = left
        #     j = right - 1

        #     while i < j:
        #         while i < right and nums[i] < pivot:
        #             i += 1
        #         while j > left and nums[j] >= pivot:
        #             j -= 1
        #         if i < j:
        #             nums[i], nums[j] = nums[j], nums[i]
            
        #     if nums[i] > pivot:
        #         nums[i], nums[right] = nums[right], nums[i]

        #     return i

        # quicksort(0, len(nums) - 1)
        # return nums

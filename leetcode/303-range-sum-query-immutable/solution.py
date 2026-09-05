class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0]

        curSum = 0
        for num in nums:
            curSum += num
            self.preSum.append(curSum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
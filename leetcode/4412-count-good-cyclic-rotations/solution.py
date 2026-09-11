class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        leftQueue = deque(nums[:len(nums)//2])
        rightQueue = deque(nums[len(nums)//2:])

        leftSum = sum(leftQueue)
        rightSum = sum(rightQueue)

        res = 0
        for i in range(len(nums)):
            if leftSum > rightSum:
                res += 1

            leftPop = leftQueue.popleft()
            leftSum -= leftPop
            rightQueue.append(leftPop)
            rightSum += leftPop

            rightPop = rightQueue.popleft()
            rightSum -= rightPop
            leftQueue.append(rightPop)
            leftSum += rightPop



        return res
            
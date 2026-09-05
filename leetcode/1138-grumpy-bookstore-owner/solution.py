class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curSum = 0
        l = 0
        n = len(customers)

        maxL = -1
        maxR = -1
        maxSum = -1
        
        for r in range(n):
            curSum += customers[r] if grumpy[r] == 1 else 0
            if (r - l) + 1 == minutes:
                if curSum > maxSum:
                    maxSum = curSum
                    maxL = l
                    maxR = r
                curSum -= customers[l] if grumpy[l] == 1 else 0
                l += 1

        output = 0
        for i in range(n):
            if not grumpy[i] or (i >= maxL and i <= maxR):
                output += customers[i]

        return output
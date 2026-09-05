class Solution:

    def __init__(self, w: List[int]):
        self.preSum = []
        curTotal = 0

        for i in w:
            curTotal += i
            self.preSum.append(curTotal)
        self.total = curTotal
        
    def pickIndex(self) -> int:
        randomValue = random.randint(1,self.total)

        l = 0
        r = len(self.preSum) - 1

        while l < r:
            m = (l+r) // 2

            if randomValue > self.preSum[m]:
                l = m + 1
            else:
                r = m

        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque([])
        self.size = size
        self.preSum = 0
        

    def next(self, val: int) -> float:
        if len(self.q) + 1 > self.size:
            self.preSum -= self.q.popleft()
        self.q.append(val)
        self.preSum += val

        return self.preSum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
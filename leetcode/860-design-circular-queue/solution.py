class MyCircularQueue:

    def __init__(self, k: int):
        self.space = [-1] * (k + 1)
        self.k = k + 1
        self.head = 0
        self.tail = 0
        self.n = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.space[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.n += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.space[self.head] = -1
        self.head = (self.head + 1) % self.k
        self.n -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.space[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.space[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k - 1
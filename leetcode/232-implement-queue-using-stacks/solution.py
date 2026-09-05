class MyQueue:

    def __init__(self):
        self.inbound = []
        self.outbound = []

    def push(self, x: int) -> None:
        self.inbound.append(x)

    def pop(self) -> int:
        if not self.outbound:
            for item in self.inbound[::-1]:
                self.outbound.append(item)
            self.inbound.clear()
            return self.outbound.pop()
        else:
            return self.outbound.pop()
        

    def peek(self) -> int:
        if self.outbound:
            return self.outbound[-1]
        else:
            return self.inbound[0]
        
    def empty(self) -> bool:
        return not self.inbound and not self.outbound     


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
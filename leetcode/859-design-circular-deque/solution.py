class ListNode():
    def __init__(self, val=None, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.dummyLeft = ListNode()
        self.dummyRight = ListNode()

        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        nxt = self.dummyLeft.next
        self.dummyLeft.next = ListNode(value, nxt, self.dummyLeft)
        nxt.prev = self.dummyLeft.next
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        prev = self.dummyRight.prev
        self.dummyRight.prev = ListNode(value, self.dummyRight, prev)
        prev.next = self.dummyRight.prev
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        newNode = self.dummyLeft.next.next
        self.dummyLeft.next = newNode
        newNode.prev = self.dummyLeft

        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        newNode = self.dummyRight.prev.prev
        self.dummyRight.prev = newNode
        newNode.next = self.dummyRight


        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.dummyLeft.next.val
        else:
            return -1
        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.dummyRight.prev.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
from collections import defaultdict


class ListNode:

    def __init__(self, val=None, nxt=None, prev=None, freq=0, key=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.freq = freq
        self.key = key


class DLinkedList:
    def __init__(self):
        self.dummyLeft = ListNode()
        self.dummyRight = ListNode()
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
        self.size = 0

    def appendRight(self, node):
        prev = self.dummyRight.prev
        prev.next = node
        node.prev = prev
        node.next = self.dummyRight
        self.dummyRight.prev = node
        self.size += 1

    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def popLeft(self):
        node = self.dummyLeft.next
        self.unlink(node)
        return node

    def __len__(self):
        return self.size


class LFUCache:
    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.cache = {}                          # key -> ListNode
        self.buckets = defaultdict(DLinkedList)  # freq -> nodes, LRU first
        self.minFreq = 0

    def increaseFreq(self, node):
        f = node.freq
        bucket = self.buckets[f]
        bucket.unlink(node)
        if not bucket:
            del self.buckets[f]
            if self.minFreq == f:
                self.minFreq = f + 1

        node.freq = f + 1
        self.buckets[f + 1].appendRight(node)

    def evictNode(self):
        bucket = self.buckets[self.minFreq]
        evict = bucket.popLeft()
        if not bucket:
            del self.buckets[self.minFreq]
        return evict.key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.increaseFreq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.maxSize == 0:          # optional guard: capacity 0 is legal input
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.increaseFreq(node)
            return

        if len(self.cache) == self.maxSize:
            del self.cache[self.evictNode()]

        newNode = ListNode(val=value, key=key, freq=1)
        self.cache[key] = newNode
        self.buckets[1].appendRight(newNode)
        self.minFreq = 1
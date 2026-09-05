class LinkNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> (Node)

        # Dummy Node Setup
        self.nodeLRU = LinkNode(0,0)
        self.nodeRU = LinkNode(0,0)
        self.nodeLRU.left = None
        self.nodeRU.right = None
        self.nodeLRU.right = self.nodeRU
        self.nodeRU.left = self.nodeLRU


    def insertNode(self, node):
        oldNode = self.nodeRU.left
        node.left = oldNode
        oldNode.right = node
        node.right = self.nodeRU
        self.nodeRU.left = node

    def removeNode(self, node):
        prev = node.left
        next_node = node.right
        prev.right = next_node
        next_node.left = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # Logic to say it was recently used
            node = self.cache[key]
            self.removeNode(node)
            self.insertNode(node)
            return node.val


        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = LinkNode(key,value)
        self.insertNode(self.cache[key])

        if self.capacity < len(self.cache):
            lru_node = self.nodeLRU.right
            del self.cache[lru_node.key]
            self.removeNode(lru_node)


        # if key in self.cache:
        #     node = self.cache[key]
        #     node.val = value
        #     self.removeNode(node)
        #     self.insertNode(node)
        # else:
        #     if len(self.cache) >= self.capacity:
        #         lru_node = self.nodeLRU.right
        #         del self.cache[lru_node.key]
        #         self.removeNode(lru_node)
        #     new_node = LinkNode(key, value)
        #     self.cache[key] = new_node
        #     self.insertNode(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
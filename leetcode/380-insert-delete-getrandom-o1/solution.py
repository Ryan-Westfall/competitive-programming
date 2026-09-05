import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.hash = collections.defaultdict(int)
        
    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False

        self.hash[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False

        index = self.hash[val]
        self.array[index] = self.array[-1]
        self.hash[self.array[-1]] = index

        del self.hash[val]
        self.array.pop()


        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called

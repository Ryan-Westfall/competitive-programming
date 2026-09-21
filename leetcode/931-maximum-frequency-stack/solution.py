import collections
class FreqStack:

    def __init__(self):
        self.count = collections.Counter()
        self.freqBucket = defaultdict(list)
        self.maxFreqSeen = 0

    def push(self, val: int) -> None:
        freq = self.count[val] + 1
        self.count[val] = freq
        if freq > self.maxFreqSeen:
            self.maxFreqSeen = freq
        self.freqBucket[freq].append(val)

    def pop(self) -> int:
        bucketList = self.freqBucket[self.maxFreqSeen]
        poppedVal = bucketList.pop()
        self.count[poppedVal] -= 1
        if len(bucketList) == 0:
            self.maxFreqSeen -= 1

        return poppedVal

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
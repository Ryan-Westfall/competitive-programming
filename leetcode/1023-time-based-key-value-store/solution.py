class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        orderedList = self.map[key]
        i = bisect.bisect(orderedList, timestamp, key=lambda x: x[0])
        if i == 0:
            return ""
        return str(orderedList[i-1][1])
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
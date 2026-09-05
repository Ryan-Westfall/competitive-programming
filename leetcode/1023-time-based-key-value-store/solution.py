class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        valuesList = self.cache[key]
        res = ""

        l,r = 0, len(valuesList) - 1
        while l <= r:
            m = (l + r) // 2
            if valuesList[m][1] > timestamp:
                r = m - 1
            else:
                res = valuesList[m][0]
                l = m + 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
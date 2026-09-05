class Solution:
    def firstUniqChar(self, s: str) -> int:
        thing = {};
        for i in s:
            thing[i] = thing.setdefault(i,0) + 1;
        for index, i in enumerate(s):
            if thing[i] == 1:
                return index;
        return -1;
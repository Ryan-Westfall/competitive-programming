class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)


        for word in strings:
            if len(word) == 1:
                hashmap[(-1)].append(word)
            else:
                i = 1
                curKey = []
                while i < len(word):
                    curKey.append((ord(word[i]) - ord(word[i-1])) % 26)
                    i += 1
                hashmap[tuple(curKey)].append(word)

        return list(hashmap.values())
        
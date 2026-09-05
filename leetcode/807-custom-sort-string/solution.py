class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # result = []
        # seen = collections.Counter(s)

        # i = 0
        # for o in order:
        #     while o in seen:
        #         result.append(o)
        #         seen[o] -= 1
        #         if seen[o] == 0:
        #             del seen[o]
            
        # for k, v in seen.items():
        #     for _ in range(v):
        #         result.append(k)

        # return "".join(result)

        # Using list instead of hashmap to avoid collisions.
        result = []
        seen = [0] * 26

        for c in s:
            seen[ord(c) - ord('a')] += 1

        i = 0
        for o in order:
            index = ord(o) - ord('a')
            result.append(o * seen[index])
            seen[index] = 0
            
        for i, freq in enumerate(seen):
            result.append(chr(i + ord('a')) * freq)

        return "".join(result)

                
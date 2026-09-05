class Node:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Node()

        for word in strs:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
                cur.count += 1

        res = ""
        cur = root

        while len(cur.children) == 1:
            child = next(iter(cur.children.values()))

            if child.count != len(strs):
                break

            res += next(iter(cur.children.keys()))
            cur = child

        return res
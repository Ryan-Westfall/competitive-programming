class Trie:
    def __init__(self):
        self.end = False
        self.children = {}


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()

        # Build trie
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.end = True

        ans = ""

        # Check each word
        for word in words:
            cur = root
            valid = True

            for c in word:
                cur = cur.children[c]
                if not cur.end:
                    valid = False
                    break

            if valid:
                if (len(word) > len(ans) or
                    (len(word) == len(ans) and word < ans)):
                    ans = word

        return ans
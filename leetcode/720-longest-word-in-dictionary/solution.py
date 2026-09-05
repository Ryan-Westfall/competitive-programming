class Trie:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        root.end = True

        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.end = True

        ans = ""
        path = []

        def dfs(node):
            nonlocal ans

            if not node.end:
                return

            word = ''.join(path)
            if len(word) > len(ans):
                ans = word

            for c in sorted(node.children):
                path.append(c)
                dfs(node.children[c])
                path.pop()

        dfs(root)
        return ans
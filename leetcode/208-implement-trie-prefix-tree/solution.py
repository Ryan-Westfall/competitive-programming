
class Trie:

    class Node:
        def __init__(self):
            self.endOfWord = False
            self.branches = {}

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.branches:
                curr.branches[c] = self.Node()
            curr = curr.branches[c]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.branches:
                return False
            curr = curr.branches[c]
        
        return curr.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.branches:
                return False
            curr = curr.branches[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
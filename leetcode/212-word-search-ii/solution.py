class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        # Build Trie:
        root = Trie()
        for word in words:
            curTrie = root
            for c in word:
                if c not in curTrie.children:
                    curTrie.children[c] = Trie()
                curTrie = curTrie.children[c]
            curTrie.endOfWord = True

        def backtracking(r,c,cur,trieNode):
            if trieNode.endOfWord:
                res.append(''.join(cur))
                trieNode.endOfWord = False
            if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[r]) - 1 or board[r][c] not in trieNode.children:
                return
            
            cur.append(board[r][c])
            # temp = trieNode
            trieNode = trieNode.children[board[r][c]]
            board[r][c] = "#"
            backtracking(r + 1, c, cur, trieNode)
            backtracking(r - 1, c, cur, trieNode)
            backtracking(r, c + 1, cur, trieNode)
            backtracking(r, c - 1, cur, trieNode)
            board[r][c] = cur[-1]
            cur.pop()
            # trieNode = temp


        for r in range(len(board)):
            for c in range(len(board[r])):
                backtracking(r,c,[],root)

        return res
        
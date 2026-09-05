class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        root = TrieNode()

        # Build bit trie
        for num in nums:
            node = root

            for i in range(31, -1, -1):
                bit = (num >> i) & 1

                if not node.children[bit]:
                    node.children[bit] = TrieNode()

                node = node.children[bit]


        ans = 0

        # Query best xor partner
        for num in nums:
            node = root
            cur = 0

            for i in range(31, -1, -1):
                bit = (num >> i) & 1

                opposite = 1 - bit

                if node.children[opposite]:
                    cur |= (1 << i)
                    node = node.children[opposite]
                else:
                    node = node.children[bit]

            ans = max(ans, cur)

        return ans
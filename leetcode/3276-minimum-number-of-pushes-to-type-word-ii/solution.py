class Solution:
    def minimumPushes(self, word: str) -> int:
        count = collections.Counter(word)

        total = 0
        sort = sorted(count.values(), reverse=True)
        for i, freq in enumerate(sort):
            total += ((i // 8) + 1) * freq

        return total
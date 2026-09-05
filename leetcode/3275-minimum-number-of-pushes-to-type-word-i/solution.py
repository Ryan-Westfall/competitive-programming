class Solution:
    def minimumPushes(self, word: str) -> int:
        processed = len(word)
        total = 0
        mult = 1
        while processed:
            if processed >= 8:
                processed -= 8
                total += mult * 8
            else:
                rem = processed % 8
                processed -= rem
                total += mult * rem
            mult += 1

        return total
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left = right = 0
        leftQ = rightQ = 0

        for i, c in enumerate(num):
            if c == '?':
                if i < mid:
                    leftQ += 1
                else:
                    rightQ += 1
            else:
                if i < mid:
                    left += int(c)
                else:
                    right += int(c)

        diff = left - right
        qdiff = leftQ - rightQ

        return diff != -qdiff * 9 / 2
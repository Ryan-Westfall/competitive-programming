class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, letter in enumerate(s, start=1):
            positionVal = abs(ord('z') + 1 - ord(letter))
            total += (positionVal * i)

        return total
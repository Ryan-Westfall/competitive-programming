class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(1, len(s) + 1):
            letter = s[i-1]
            positionVal = abs(ord('z') + 1 - ord(letter))
            total += (positionVal * i)

        return total
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        targetX, targetY = target[0],target[1]

        if (source[0] + source[1]) % 2 != (target[0] + target[1]) % 2:
            return -1

        n = 8
        m = 8

        curX, curY = source[0], source[1]
        while curX <= n and curY >= 1:
            if curX == targetX and curY == targetY:
                return 1
            curX += 1
            curY -= 1

        curX, curY = source[0], source[1]
        while curX >= 1 and curY <= m:
            if curX == targetX and curY == targetY:
                return 1
            curX -= 1
            curY += 1

        curX, curY = source[0], source[1]
        while curX <= n and curY <= m:
            if curX == targetX and curY == targetY:
                return 1
            curX += 1
            curY += 1

        curX, curY = source[0], source[1]
        while curX >= 1 and curY >= 1:
            if curX == targetX and curY == targetY:
                return 1
            curX -= 1
            curY -= 1

        return 2
            
        
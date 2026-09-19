class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True
            
        closest = float('inf')
        startX, startY, endX, endY = x1, y1, x2, y2
        for x in range(startX, endX+1):
            startYEuclidianDistance = ((xCenter - x)**2 + (yCenter - startY) ** 2) ** (1/2)
            endYEuclidianDistance = ((xCenter - x)**2 + (yCenter - endY) ** 2) ** (1/2)
            closest = min(closest, startYEuclidianDistance, endYEuclidianDistance)        

        for y in range(startY, endY+1):
            startXEuclidianDistance = ((xCenter - startX)**2 + (yCenter - y) ** 2)**(1/2)
            endXEuclidianDistance = ((xCenter - endX)**2 + (yCenter - y) ** 2)**(1/2)
            closest = min(closest, startXEuclidianDistance, endXEuclidianDistance)
            
        return closest <= radius
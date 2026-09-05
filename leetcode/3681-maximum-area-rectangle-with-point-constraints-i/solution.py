class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        maxArea = float('-inf')
        pointSet = set(map(tuple, points))  # Store all points for O(1) lookup
    
        for x1, y1 in points:
            for x2, y2 in pointSet:
                # Skip if the points are the same or don't form a valid rectangle
                if x1 == x2 or y1 == y2:
                    continue
    
                # Check if the rectangle corners exist
                if (x1, y2) in pointSet and (x2, y1) in pointSet:
                    # Define bounds
                    lowerX = min(x1, x2)
                    higherX = max(x1, x2)
                    lowerY = min(y1, y2)
                    higherY = max(y1, y2)
    
                    # Check if any other point lies inside or on the rectangle boundary
                    valid = True
                    for x, y in points:
                        if (
                            lowerX <= x <= higherX and
                            lowerY <= y <= higherY and
                            (x, y) not in {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}
                        ):
                            valid = False
                            break
    
                    if valid:
                        size = (higherX - lowerX) * (higherY - lowerY)
                        maxArea = max(maxArea, size)
    
        return maxArea if maxArea != float('-inf') else -1
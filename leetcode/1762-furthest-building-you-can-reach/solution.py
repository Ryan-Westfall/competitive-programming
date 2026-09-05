
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []  # Min-heap to track where ladders are used

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(min_heap, diff)
            
            # If we exceed the ladder count, use bricks for the smallest height difference
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
            
            # If bricks are exhausted, we cannot move further
            if bricks < 0:
                return i
        
        return len(heights) - 1

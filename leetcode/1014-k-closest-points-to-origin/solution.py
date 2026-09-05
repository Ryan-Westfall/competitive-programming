class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # (distance, [x,y])

        for x,y in points:
            distance = ((x) ** 2 + (y) ** 2) ** .5
            heap.append((distance, (x,y)))

        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
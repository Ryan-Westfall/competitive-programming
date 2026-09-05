class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = [] # (value, row)
        for r in range(len(values)):
            heapq.heappush(heap, (values[r].pop(),r))

        spend = 0
        day = 1
        while heap:
            value, r = heapq.heappop(heap)
            spend += (value * day)

            if values[r]:
                heapq.heappush(heap, (values[r].pop(),r))
            day += 1

        return spend
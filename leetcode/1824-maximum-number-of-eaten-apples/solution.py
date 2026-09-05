class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq

        heap = []
        eaten = 0
        day = 0

        while day < len(apples) or heap:

            # Add today's apples
            if day < len(apples) and apples[day] > 0:
                expire = day + days[day]
                heapq.heappush(heap, (expire, apples[day]))

            # Remove rotten apples
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # Eat apple from batch expiring soonest
            if heap:
                expire, count = heapq.heappop(heap)

                eaten += 1
                count -= 1

                # Put remaining apples back
                if count > 0:
                    heapq.heappush(heap, (expire, count))

            day += 1

        return eaten
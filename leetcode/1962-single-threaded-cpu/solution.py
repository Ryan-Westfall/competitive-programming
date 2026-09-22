class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        notEnque = [(enqueTime, processingTime, i) for i, (enqueTime, processingTime) in enumerate(tasks)]
        heapq.heapify(notEnque)
        free = []

        ans = []
        curTime = 0
        while free or notEnque:
            while notEnque and curTime >= notEnque[0][0]:
                enqueTime, processingTime, i = heapq.heappop(notEnque)
                heapq.heappush(free, (processingTime, i))

            if free:
                processTime, i = heapq.heappop(free)
                curTime += processTime
                ans.append(i)
            
            # Speedup
            if notEnque and not free:
                curTime = max(notEnque[0][0], curTime)

        return ans
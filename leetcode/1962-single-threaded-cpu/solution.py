class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        notEnque = [(enqueueTime, processingTime, i) for i, (enqueueTime, processingTime) in enumerate(tasks)]
        heapq.heapify(notEnque)

        free = []
        ans = []
        curTime = 0

        while notEnque or free:
            while notEnque and curTime >= notEnque[0][0]:
                enqueueTime, processingTime, i = heapq.heappop(notEnque)
                heapq.heappush(free, (processingTime, i))

            if free:
                processingTime, i = heapq.heappop(free)
                curTime += processingTime
                ans.append(i)
            else:
                curTime = notEnque[0][0]

        return ans
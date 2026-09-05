class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        avaliable = [i for i in range(n)]
        used = [] # (endTime, roomId)
        count = [0] * n

        for start, end in meetings:
            # Meeting ended, give it back to avaliable
            while used and start >= used[0][0]:
                _, roomId = heapq.heappop(used)
                heapq.heappush(avaliable,roomId)

            # No more meetings, free up used
            if len(avaliable) == 0:
                endTime, roomId = heapq.heappop(used)
                end = endTime + (end - start)
                heapq.heappush(avaliable,roomId)

            # Asign room to meeting
            roomId = heapq.heappop(avaliable)
            heapq.heappush(used,(end, roomId))
            count[roomId] += 1

        maxCount = max(count)
        for i, c in enumerate(count):
            if c == maxCount:
                return i

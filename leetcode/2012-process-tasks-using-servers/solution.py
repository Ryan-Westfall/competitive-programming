
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)

        busy = []  # (finish_time, weight, index)
        res = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release servers that finished
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no servers are free, jump to next completion
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Assign task to best available server
            weight, idx = heapq.heappop(free)
            res.append(idx)

            heapq.heappush(busy, (time + duration, weight, idx))

        return res

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        time = 0
        i = 0
        free = [(w, idx) for idx, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, server_idx)
        ans = [0] * len(tasks)

        while i < len(tasks):
            time = max(time, i)  # task i arrives at i
            while busy and busy[0][0] <= time:
                _, s = heapq.heappop(busy)
                heapq.heappush(free, (servers[s], s))
            if free:
                _, s = heapq.heappop(free)
                ans[i] = s
                heapq.heappush(busy, (time + tasks[i], s))
                i += 1
            else:
                time = busy[0][0]  # fast-forward, don't +1 step

        return ans
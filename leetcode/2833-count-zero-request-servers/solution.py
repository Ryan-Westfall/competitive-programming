class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sortedQueries = sorted(enumerate(queries), key=lambda q: q[1])

        freq = defaultdict(int)
        res = [0] * len(queries)

        left = 0
        right = 0

        for idx, query in sortedQueries:

            # Add logs within query time
            while right < len(logs) and logs[right][1] <= query:
                serverId, time = logs[right]
                freq[serverId] += 1
                right += 1

            # Remove logs outside window
            while left < right and logs[left][1] < query - x:
                serverId, time = logs[left]
                freq[serverId] -= 1

                if freq[serverId] == 0:
                    del freq[serverId]

                left += 1

            res[idx] = n - len(freq)

        return res
class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = [(grid[0][0], 0, 0, 0, None)]
        visit = set()

        while queue:
            cost, turns, row, col, direction = heapq.heappop(queue)

            if turns > k:
                continue

            if row == n - 1 and col == m - 1:
                return cost

            if (row, col, direction, turns) in visit:
                continue
            visit.add((row, col, direction, turns))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < n and 0 <= newCol < m:
                    newDirection = (dr, dc)
                    turnCost = 0 if direction is None or direction == newDirection else 1

                    heapq.heappush(queue, (cost + grid[newRow][newCol], turns + turnCost, newRow, newCol, newDirection))

        return -1
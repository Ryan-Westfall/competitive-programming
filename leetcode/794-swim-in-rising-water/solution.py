from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # m = len(grid[0])
        
        # queue = [(grid[0][0],0,0, grid[0][0])]
        # seen = set((0,0))
        # while queue:
        #     curElevation, row, col, maxSeen = heappop(queue)

        #     if row == n - 1 and col == m - 1:
        #         return maxSeen

        #     for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        #         newRow, newCol = row + dr, col + dc
        #         if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and (newRow, newCol) not in seen:
        #             newElevation = grid[newRow][newCol]
        #             seen.add((newRow,newCol))
        #             heappush(queue, (newElevation, newRow, newCol, max(maxSeen, newElevation)))

        # return minSeen


        n = len(grid)
        m = len(grid[0])

        def isValid(x):
            if x < grid[0][0]:
                return False
                
            queue = deque([(0,0)])
            seen = set()
            while queue:
                row, col = queue.popleft()

                if row == n - 1 and col == m - 1:
                    return True    

                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newRow, newCol = row + dr, col + dc
                    if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and (newRow, newCol) not in seen and grid[newRow][newCol] <= x:
                        seen.add((newRow,newCol))
                        queue.append((newRow,newCol))

            return False

        left = 0
        right = max(max(row) for row in grid)

        while left < right:

            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1

        return left

        
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0,0,1)])

        directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        while queue:
            row, col, distance = queue.popleft()

            if grid[row][col] == 1:
                continue

            if row + 1 == len(grid) and col + 1 == len(grid[row]):
                return distance

            grid[row][col] = 1

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc


                if (newRow >= 0 and 
                    newCol >= 0 and 
                    newRow < len(grid) and 
                    newCol < len(grid[newRow]) and  
                    grid[newRow][newCol] != 1):
                    queue.append((newRow, newCol, distance + 1))

        return -1
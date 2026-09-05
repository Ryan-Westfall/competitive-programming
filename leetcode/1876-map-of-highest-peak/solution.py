class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        waterIndex = []
        height = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]

        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    waterIndex.append((row,col))
                    height[row][col] = 0

        queue = deque(waterIndex)
        elevation = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = row + dr, col + dc
                    if not (nr < 0 or nr >= len(isWater) or nc < 0 or nc >= len(isWater[0]) or height[nr][nc] != -1):
                        height[nr][nc] = elevation
                        queue.append((nr, nc))
            elevation += 1

        return height

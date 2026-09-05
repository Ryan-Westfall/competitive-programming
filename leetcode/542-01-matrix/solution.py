class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        output = [[-1] * m for _ in range(n)]

        queue = deque([])
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    output[r][c] = 0

        # print


        level = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                

                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newR, newC = row + dr, col + dc
                    if newR < n and newR >= 0 and newC < m and newC >= 0 and output[newR][newC] == -1:
                        output[newR][newC] = level + 1
                        queue.append((newR,newC))

            level += 1

        return output
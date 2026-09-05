class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n = len(classroom)
        m = len(classroom[0])
        fullMask = 0
        bit = 1
        maskId = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if classroom[r][c] == 'L':
                    maskId[r][c] = bit
                    fullMask |= bit
                    bit <<= 1
                if classroom[r][c] == 'S':
                    sr, sc = r, c

        bestEnergy = [[{i: -1 for i in range(fullMask, -1, -1)} for _ in range(m)] for _ in range(n)]
        queue = deque([(sr,sc,0,energy,0)])

        while queue:
            row, col, mask, curEnergy, step = queue.popleft()

            if classroom[row][col] == 'L':
                mask |= maskId[row][col]

            if mask == fullMask:
                return step

            if classroom[row][col] == 'R':
                curEnergy = energy
            

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow, newCol = row + dr, col + dc
                if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and bestEnergy[newRow][newCol][mask] < curEnergy and curEnergy > 0 and classroom[newRow][newCol] != 'X':
                    bestEnergy[newRow][newCol][mask] = curEnergy
                    queue.append((newRow, newCol, mask, curEnergy - 1, step + 1))

        return -1

                    
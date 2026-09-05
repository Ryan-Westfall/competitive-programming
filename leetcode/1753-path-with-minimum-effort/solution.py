from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        queue = [(0,0,0)]
        visit = set((0,0))

        while queue:
            maxAbsSeen, r, c = heappop(queue)

            if r == n - 1 and c == m - 1:
                return maxAbsSeen

            if (r,c) in visit:
                continue

            visit.add((r,c))



            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < n and nc >= 0 and nc < m:                    
                    heappush(queue, ((max(maxAbsSeen, abs(heights[r][c] - heights[nr][nc])), nr, nc)))

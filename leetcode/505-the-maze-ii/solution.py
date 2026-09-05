class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        queue = [(0, start[0], start[1])]
        stoppedLocations = set()

        while queue:
            curTraveled, r, c = heapq.heappop(queue)

            if [r,c] == destination:
                return curTraveled

            if (r,c) in stoppedLocations:
                continue

            stoppedLocations.add((r,c))

            # up
            nr = r
            count = 0
            while nr - 1 >= 0 and maze[nr-1][c] == 0:
                count += 1
                nr -= 1
            if count > 0:    
                heapq.heappush(queue, (curTraveled+count,nr,c))

            # down
            nr = r
            count = 0
            while nr + 1 < n and maze[nr+1][c] == 0:
                count += 1
                nr += 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,nr,c))

            # right
            nc = c
            count = 0
            while nc + 1 < m and maze[r][nc+1] == 0:
                count += 1
                nc += 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,r,nc))

            # left
            nc = c
            count = 0
            while nc - 1 >= 0 and maze[r][nc-1] == 0:
                count += 1
                nc -= 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,r,nc))

        return -1

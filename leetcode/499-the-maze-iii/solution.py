class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        n = len(maze)
        m = len(maze[0])

        queue = [(0, ball[0], ball[1], '')]
        stoppedLocations = set()

        while queue:
            curTraveled, r, c, path = heapq.heappop(queue)

            if [r,c] == hole:
                return path

            if (r,c) in stoppedLocations:
                continue

            stoppedLocations.add((r,c))

            # up
            nr = r
            count = 0
            while nr - 1 >= 0 and maze[nr-1][c] == 0 and [nr,c] != hole:
                count += 1
                nr -= 1
            if count > 0:    
                heapq.heappush(queue, (curTraveled+count,nr,c,path + 'u'))

            # down
            nr = r
            count = 0
            while nr + 1 < n and maze[nr+1][c] == 0 and [nr,c] != hole:
                count += 1
                nr += 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,nr,c,path + 'd'))

            # right
            nc = c
            count = 0
            while nc + 1 < m and maze[r][nc+1] == 0 and [r,nc] != hole:
                count += 1
                nc += 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,r,nc,path + 'r'))

            # left
            nc = c
            count = 0
            while nc - 1 >= 0 and maze[r][nc-1] == 0 and [r,nc] != hole:
                count += 1
                nc -= 1
            if count > 0: 
                heapq.heappush(queue, (curTraveled+count,r,nc,path + 'l'))

        return "impossible"
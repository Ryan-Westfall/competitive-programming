class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n = len(maze)
        m = len(maze[0])

        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return False

            if [r, c] == destination:
                return True

            visited.add((r, c))

            # UP
            nr, nc = r, c
            while nr - 1 >= 0 and maze[nr - 1][nc] == 0:
                nr -= 1

            if dfs(nr, nc):
                return True

            # RIGHT
            nr, nc = r, c
            while nc + 1 < m and maze[nr][nc + 1] == 0:
                nc += 1

            if dfs(nr, nc):
                return True

            # DOWN
            nr, nc = r, c
            while nr + 1 < n and maze[nr + 1][nc] == 0:
                nr += 1

            if dfs(nr, nc):
                return True

            # LEFT
            nr, nc = r, c
            while nc - 1 >= 0 and maze[nr][nc - 1] == 0:
                nc -= 1

            if dfs(nr, nc):
                return True

            return False

        return dfs(start[0], start[1])
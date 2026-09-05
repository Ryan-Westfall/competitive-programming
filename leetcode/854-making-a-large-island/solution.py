class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        size_dict = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        identifier = -1

        # Precalculate all island sizes and assign them to identifier within dict
        def dfs(r,c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid) or grid[r][c] != 1:
                return 0

            grid[r][c] = identifier
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = 0
                    area += dfs(r,c)
                    size_dict[identifier] = area
                    identifier -= 1

        # Flip all 0's to 1 and lookup 4 directions by referencing dict
        print(size_dict)

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    seen = set()
                    area = 1

                    for dr, dc in directions:
                        nxt_r = r + dr
                        nxt_c = c + dc
                        if nxt_r >= 0 and nxt_r < len(grid) and nxt_c >= 0 and nxt_c < len(grid[nxt_r]) and grid[nxt_r][nxt_c] != 0:
                            seen.add(grid[nxt_r][nxt_c])

                    for numIdentifer in seen:
                        area += size_dict[numIdentifer]

                    
                    maxArea = max(maxArea, area)

        
        return maxArea if maxArea else len(grid) ** 2


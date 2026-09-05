class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        queue = deque([(sr,sc)])
        fillColor = image[sr][sc]
        image[sr][sc] = color
        while queue:
            row, col = queue.popleft()

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow, newCol = row + dr, col + dc
                if newRow >= 0 and newRow < len(image) and newCol >= 0 and newCol < len(image[0]) and image[newRow][newCol] == fillColor:
                    image[newRow][newCol] = color
                    queue.append((newRow,newCol))

        return image


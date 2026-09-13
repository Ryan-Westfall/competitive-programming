class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        img1List = []
        img2Set = set()
        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    img2Set.add((r,c))
                if img1[r][c] == 1:
                    img1List.append((r,c))

        maxCount = 0

        coordinates = [(i, j) for i in range(-n, n + 1) for j in range(-n, n + 1)]

        for dr, dc in coordinates:
            count = 0
            for r, c in img1List:
                if (r+dr,c+dc) in img2Set:
                    count += 1

            maxCount = max(maxCount, count)

        return maxCount


            

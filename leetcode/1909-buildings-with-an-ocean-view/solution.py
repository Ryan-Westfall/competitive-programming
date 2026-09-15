class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        maxSeen = float('-inf')
        ans = []
        for r in range(n - 1, -1, -1):
            if heights[r] > maxSeen:
                ans.append(r)
                maxSeen = heights[r]

        return ans[::-1]
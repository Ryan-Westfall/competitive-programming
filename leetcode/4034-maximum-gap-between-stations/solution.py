class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        m = len(station)

        if n <= 1:
            return 0

        left = [0] * n
        stationIndex = 0
        for i in range(n):
            while stationIndex < m and station[stationIndex] != skill[i]:
                stationIndex += 1
            left[i] = stationIndex
            stationIndex += 1

        right = [0] * n
        stationIndex = m - 1
        for i in range(n-1, -1, -1):
            while stationIndex >= 0 and station[stationIndex] != skill[i]:
                stationIndex -= 1
            right[i] = stationIndex
            stationIndex -= 1

        maxGap = 0
        for i in range(1, n):
            maxGap = max(maxGap, right[i] - left[i-1])

        return maxGap
        
        
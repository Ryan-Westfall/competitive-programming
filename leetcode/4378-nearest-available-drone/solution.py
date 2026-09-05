class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minDistance = float('inf')
        index = -1

        for i, (x, y, range) in enumerate(drones):
            distance = abs(target[0] - x) + abs(target[1] - y)

            if range >= distance:
                if distance < minDistance:
                    minDistance = distance
                    index = i
            else:
                continue

        return index
        
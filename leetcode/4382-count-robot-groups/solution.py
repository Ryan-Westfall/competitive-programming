class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        groups = 1

        group_pos = position[-1]
        group_speed = speed[-1]

        for i in range(n - 2, -1, -1):
            gap = group_pos - position[i]

            if gap <= distance or speed[i] > group_speed:
                group_pos = position[i]
            else:
                groups += 1
                group_pos = position[i]
                group_speed = speed[i]

        return groups
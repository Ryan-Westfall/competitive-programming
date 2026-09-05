class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            visited.add(room)

            for nei in rooms[room]:
                if nei not in visited:
                    queue.append(nei)

        return len(rooms) == len(visited)
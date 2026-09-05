class Solution:
    def minJumps(self, arr: List[int]) -> int:
        numToIndex = defaultdict(list)
        for i, num in enumerate(arr):
            numToIndex[num].append(i)

        queue = deque([0])
        visited = {0}
        usedValues = set()
        moves = 0

        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()

                if index == len(arr) - 1:
                    return moves

                # Move left
                if index > 0 and index - 1 not in visited:
                    visited.add(index - 1)
                    queue.append(index - 1)

                # Move right
                if index + 1 < len(arr) and index + 1 not in visited:
                    visited.add(index + 1)
                    queue.append(index + 1)

                # Jump to all indices with the same value.
                if arr[index] not in usedValues:
                    usedValues.add(arr[index])

                    for newIndex in numToIndex[arr[index]]:
                        if newIndex not in visited:
                            visited.add(newIndex)
                            queue.append(newIndex)

            moves += 1

        return -1
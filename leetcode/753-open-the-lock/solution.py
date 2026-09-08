class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if '0000' in visit:
            return -1
        queue = deque(['0000'])
        visit.add('0000')
        totalMoves = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return totalMoves

                for i in range(4):
                    digits = list(node)

                    for change in (-1, 1):
                        digits[i] = str((int(node[i]) + change) % 10)
                        next_node = ''.join(digits)

                        if next_node not in visit:
                            visit.add(next_node)
                            queue.append(next_node)
            
            totalMoves += 1

        return -1

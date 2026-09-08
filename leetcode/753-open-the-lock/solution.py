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

                # print()

                if node == target:
                    return totalMoves

                for i in range(4):
                    # 1. Left Move (Subtract 1)
                    left_digit = str((int(node[i]) - 1) % 10)
                    leftMove = node[:i] + left_digit + node[i+1:]
                    
                    if leftMove not in visit:
                        visit.add(leftMove)
                        queue.append(leftMove)
                        
                    # 2. Right Move (Add 1)
                    right_digit = str((int(node[i]) + 1) % 10)
                    rightMove = node[:i] + right_digit + node[i+1:]
                    
                    if rightMove not in visit:
                        visit.add(rightMove)           
                        queue.append(rightMove)
            
            totalMoves += 1

        return -1




        
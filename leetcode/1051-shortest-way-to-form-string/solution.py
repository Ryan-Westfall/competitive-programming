class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        curTarget = 0
        total = 0
        while curTarget != len(target):
            prev = curTarget

            for i in range(len(source)):
                if curTarget < len(target) and target[curTarget] == source[i]:
                    curTarget += 1

            if prev == curTarget:
                return -1
                
            total += 1
        
        return total
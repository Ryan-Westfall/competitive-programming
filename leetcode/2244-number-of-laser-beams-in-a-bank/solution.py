class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevNodes = 0
        currentConnections = 0
        
        for i in bank:
            currentNodes = i.count("1")
            currentConnections += prevNodes * currentNodes
            
            if currentNodes == 0:
                continue
            prevNodes = currentNodes
            
        return currentConnections
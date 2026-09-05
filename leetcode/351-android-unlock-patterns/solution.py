class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.count = 0

        numPad = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

        def valid(r,c,nr,nc,seen):
            if (nr,nc) in seen:
                return False

            absRow = abs(r-nr)
            absCol = abs(c-nc)

            if absRow == 2 and absCol == 2:
                return (1,1) in seen
            if absRow == 0 and absCol == 2:
                if r == 0:
                    return (0,1) in seen
                elif r == 1:
                    return (1,1) in seen
                else:
                    return (2,1) in seen
            if absRow == 2 and absCol == 0:
                if c == 0:
                    return (1,0) in seen
                elif c == 1:
                    return (1,1) in seen
                else:
                    return (1,2) in seen

            return True

        
        def backtrackValidCounter(r,c,cur):
            if len(cur) >= m and len(cur) <= n:
                self.count += 1
                if len(cur) == n:
                    return

            for nr, nc in numPad:
                if valid(r,c,nr,nc,cur):
                    cur.add((nr,nc))
                    backtrackValidCounter(nr,nc,cur)
                    cur.remove((nr,nc))

        seen = set()
        for r in range(3):
            for c in range(3):
                seen.add((r,c))
                backtrackValidCounter(r,c, seen)
                seen.clear()


        return self.count
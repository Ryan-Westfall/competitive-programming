class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        p1, p2 = 0, 0
        while p1 < len(g):
            while p2 < len(s) and g[p1] > s[p2]:
                p2 += 1
            if p2 == len(s):
                break
            p1 += 1
            p2 += 1

        return p1

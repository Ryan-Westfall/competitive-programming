class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        for c in s1:
            s1dict[c] = 1 + s1dict.get(c, 0)
        
        l = 0 
        s2dict= {}
        for r in range(len(s2)):
            s2dict[s2[r]] = 1 + s2dict.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                if s2dict[s2[l]] > 1:
                    s2dict[s2[l]] -= 1
                else:
                    del s2dict[s2[l]]
                l += 1
            if s1dict == s2dict:
                return True

        return False

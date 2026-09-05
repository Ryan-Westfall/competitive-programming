class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        res = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == ' ' and not res:
                continue
            elif s[i] == ' ' and res:
                return res
            else:
                res += 1

        return res


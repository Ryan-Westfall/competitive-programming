class Solution:
    def countRotations(self, s: str, k: int) -> int:
        sLen = len(s)
        s += s
        i = 0

        equalK = 0
        while i < len(s) - sLen:
            points = 0
            for l, r in pairwise(s[i:i+sLen]):
                if l == r:
                    points += 1

            if points == k:
                equalK += 1


            i += 1

        return equalK
                
            
        
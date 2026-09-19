class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []
        def backtracking(i, j, cur):
            if j == n or i == n:
                if "".join(cur) == s:
                    ans.append(cur[:])
                return

            noTake = backtracking(i, j+1, cur)
            
            curTake = s[i:j+1]
            if curTake == curTake[::-1]:
                cur.append(curTake)
                take = backtracking(j+1, j+1, cur)
                cur.pop()

            return 

        backtracking(0,0,[])
        return ans
        
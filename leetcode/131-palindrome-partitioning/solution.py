class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []

        def backtracking(i, cur):
            if i == n:
                ans.append(cur[:])
                return

            for j in range(i, n):
                curStr = s[i:j+1]

                if curStr == curStr[::-1]:
                    cur.append(curStr)
                    backtracking(j + 1, cur)
                    cur.pop()

        backtracking(0, [])
        return ans
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCnt = 0
        res = collections.deque([])

        for c in s:
            if c == '(':
                openCnt += 1
            if c == ')':
                if openCnt:
                    openCnt -= 1
                else:
                    continue
            res.append(c)


        final = collections.deque([])
        for i in range(len(res) - 1, -1, -1):
            c = res[i]
            if openCnt and c == '(':
                openCnt -= 1
                continue
            final.appendleft(c)
        
        return "".join(final)
        
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""

        for c in s:
            if c == '(':
                if not stack:
                    stack.append(c)
                else:
                    res += c
                    stack.append(c)
            else:
                if not len(stack) == 1:
                    res += c
                stack.pop()

        return res
                

            
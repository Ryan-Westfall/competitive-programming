class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        result = 0
        cur = 0

        for c in s + '+':
            if c.isdigit():
                cur = cur * 10 + int(c)
                # print(cur)
            
            elif c == '+' or c == '-':
                result += sign * cur
                sign = 1 if c == '+' else -1
                cur = 0

            elif c == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif c == ')':
                result += sign * cur
                cur = 0

                sign = stack.pop()
                tResult = stack.pop()
                result = tResult + (sign * result)


        return result
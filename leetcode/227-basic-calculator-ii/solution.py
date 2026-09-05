class Solution:
    def calculate(self, s: str) -> int:
        curOperator = '+'
        i = 0
        curSum = 0
        prevSum = -1

        while i < len(s):
            if s[i].isdigit():
                curNum = 0
                while i < len(s) and s[i].isdigit():
                    curNum = (curNum * 10) + int(s[i])
                    i += 1
                i -= 1

                if curOperator == '+':
                    prevSum = curSum
                    curSum += curNum
                elif curOperator == '-':
                    prevSum = curSum
                    curSum -= curNum
                elif curOperator == '*':
                    temp = curSum - prevSum
                    curSum = temp * curNum + prevSum
                elif curOperator == '/':
                    temp = curSum - prevSum
                    curSum = (int(temp / curNum)) + prevSum
                
            elif s[i] in ['+', '-', '*', '/']:
                curOperator = s[i]
            i += 1

        return curSum

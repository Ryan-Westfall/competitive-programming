class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        q = collections.deque([])

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            curI = int(num1[i]) if i >= 0 else 0
            curJ = int(num2[j]) if j >= 0 else 0

            curSum = curI + curJ + carry

            q.appendleft(str(curSum % 10))
            carry = curSum // 10

            i -= 1
            j -= 1

        if carry:
            q.appendleft('1')

        return "".join(q)
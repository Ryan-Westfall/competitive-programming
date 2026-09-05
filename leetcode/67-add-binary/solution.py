class Solution:
    def addBinary(self, a: str, b: str) -> str:
        q = collections.deque([])

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            curI = int(a[i]) if i >= 0 else 0
            curJ = int(b[j]) if j >= 0 else 0

            curSum = curI + curJ + carry

            q.appendleft(str(curSum % 2))
            carry = curSum // 2

            i -= 1
            j -= 1

        if carry:
            q.appendleft('1')

        return "".join(q)
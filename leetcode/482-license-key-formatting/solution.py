class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        output = deque()
        segment = k
        for i in range(len(s) - 1, -1, -1):
            if segment == 0 and s[i] != '-':
                output.appendleft('-')
                segment = k
            if s[i] != '-':
                output.appendleft(s[i].upper())
                segment -= 1


        return "".join(output)
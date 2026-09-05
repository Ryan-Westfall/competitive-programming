class Solution:
    def isNumber(self, s: str) -> bool:
        isNumber = False
        isDecimal = False
        isExponent = False

        i = 0
        while i < len(s):
            if s[i].isdigit():
                isNumber = True
            elif s[i] in ['e', 'E']:
                if isExponent or not isNumber:
                    return False
                isExponent = True
                isNumber = False
            elif s[i] == '.':
                if isDecimal or isExponent:
                    return False
                isDecimal = True
            elif s[i] in ['+', '-']:
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                isNumber = False
            else:
                return False

            i += 1


        return isNumber
        
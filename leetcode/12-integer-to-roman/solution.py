class Solution:
    def intToRoman(self, num: int) -> str:
        # romanMap = {1: I, 5: V, 10: X, 50: L, 100: C, 500: D, 1000: M}

        output = ""

        numStr = str(num)
        pos = len(numStr)
        for c in numStr:
            if pos == 4:
                output += 'M' * int(c)
            elif pos == 3:
                if c == '9':
                    output += 'CM'
                elif c == '4':
                    output += 'CD'
                else:
                    inputC = int(c)
                    while inputC:
                        if inputC >= 5:
                            inputC -= 5
                            output += 'D'
                        else:
                            inputC -= 1
                            output += 'C'
            elif pos == 2:
                if c == '9':
                    output += 'XC'
                elif c == '4':
                    output += 'XL'
                else:
                    inputC = int(c)
                    while inputC:
                        if inputC >= 5:
                            inputC -= 5
                            output += 'L'
                        else:
                            inputC -= 1
                            output += 'X'
            elif pos == 1:
                if c == '9':
                    output += 'IX'
                elif c == '4':
                    output += 'IV'
                else:
                    inputC = int(c)
                    while inputC:
                        if inputC >= 5:
                            inputC -= 5
                            output += 'V'
                        else:
                            inputC -= 1
                            output += 'I'
            pos -= 1

        return output
            
